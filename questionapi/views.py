from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_GET
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Employer
from django.utils import timezone
from datetime import timedelta
from django.contrib import messages
import re
FREE_EMAIL_DOMAINS = [
    'gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com',
    'protonmail.com', 'icloud.com', 'mail.com', 'yandex.com', 'zoho.com',
    'gmx.com', 'inbox.com', 'live.com', 'msn.com', 'rediffmail.com',
    'web.de', 't-online.de', 'laposte.net', 'orange.fr', 'free.fr',
    'wanadoo.fr', 'libero.it', 'virgilio.it', 'abv.bg', 'mail.ru',
    'rambler.ru', 'ukr.net', 'wp.pl', 'o2.pl', 'onet.pl', 'interia.pl',
    'seznam.cz', 'centrum.cz', 'email.cz', 'terra.com', 'bol.com.br',
    'uol.com.br', 'qq.com', '163.com', '126.com', 'sina.com', 'sohu.com',
    'daum.net', 'naver.com', 'hanmail.net', 'korea.com', 'nate.com',
    'gawab.com', # Add more as needed
]
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        email = request.POST.get('email').strip().lower()
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        organization_name = request.POST.get('organizationName')
        role = request.POST.get('role')
        organization_name_raw = request.POST.get('organizationName')
        organization_name = organization_name_raw.strip().lower() 
        
        role = request.POST.get('role')
        # Confirm password match validation
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'register.html')

        # Server-Side Validation
        if any(char.isdigit() for char in first_name) or any(char.isdigit() for char in (last_name or "")):
            messages.error(request, "First name and last name cannot contain numbers.")
            return render(request, 'register.html')

        if len(password) < 8 or not re.search(r'[A-Z]', password) or not re.search(r'[0-9]', password) or not re.search(r'[!@#$%^&*()]', password):
            messages.error(request, "Password must meet the complexity requirements.")
            return render(request, 'register.html')
        
        # email_domain = email.split('@')[1].lower()
        # if Employer.objects.filter(email__endswith='@' + email_domain).exists():
        #     messages.error(request, "An account with this organization domain already exists.")
        #     return render(request, 'register.html')
        
        # Check if the email domain is a free email domain
        email_domain = email.split('@')[1].lower()
        if Employer.objects.filter(email__endswith='@' + email_domain).count() >= 100:
            messages.error(request, "Registration limit reached for this organization ")
            return render(request, 'register.html')
        
        email_domain = email.split('@')[-1] # Get the domain part
        if email_domain in FREE_EMAIL_DOMAINS:
            messages.error(request, "Please use your organization's email address. Free email domains are not allowed.")
            return render(request, 'register.html')

        if Employer.objects.filter(email=email).exists():
            messages.error(request, "This email address is already registered.")
            return render(request, 'register.html')

        # Limit registrations per organization to 10 users (case-insensitive, trimmed)
        # if Employer.objects.filter(organization_name__iexact=organization_name.strip()).count() >= 10:
        #     messages.error(request, "Registration limit reached for this organization (max 10 users).")
        #     return render(request, 'register.html')

        Employer.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            organization_name=organization_name,
            password=password,
            role=role
        )
        subject = 'Welcome to Face D Interview!'
        message_body = f"Hi {first_name},\n\nThank you for registering on FDI."
        send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, [email])
        
        return render(request, 'registration_success.html')

    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email').strip().lower()
        password = request.POST.get('password')
        try:
            employer = Employer.objects.get(email=email)
        except Employer.DoesNotExist:
            messages.error(request, 'Invalid email or password.')
            return render(request, 'login.html')

        now = timezone.now()
        # Account blocked check for password failure lockout
        if (employer.account_blocked_until and now < employer.account_blocked_until):
            messages.error(request, 'This account is temporarily blocked.')
            return render(request, 'login.html')

        if employer.password == password:
            employer.failed_login_attempts = 0
            employer.failed_otp_attempts = 0
            employer.last_login_timestamp = timezone.now()
            employer.save()
            employer.generate_login_otp()

            subject = 'Your Two-Step Verification Code'
            message_body = f"Hi {employer.first_name},\n\nYour login verification code is: {employer.login_otp}"
            send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, [email])
            request.session['verification_email'] = employer.email
            messages.info(request, 'Please check your registered mail for the OTP.')
            return redirect('verify_login_otp')
        else:
            employer.failed_login_attempts += 1
            if employer.failed_login_attempts >= 3:
                # Block account for 24 hours after 3 failed password attempts
                employer.account_blocked_until = now + timedelta(hours=24)
                subject = 'Account Blocked: Failed Login Attempts'
                message_body = "Your account has been blocked for 24 hours due to multiple failed login attempts."
                send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, [employer.email])
                messages.error(request, 'Your account is now blocked for 24 hours.')
            else:
                remaining_attempts = 3 - employer.failed_login_attempts
                messages.error(request, f'Invalid email or password. You have {remaining_attempts} attempts remaining.')
            employer.save()
            
    return render(request, 'login.html')


def verify_login_otp(request):
    email = request.session.get('verification_email')
    if not email: 
        return redirect('login')
    
    employer = Employer.objects.get(email=email)
    
    if request.method == 'POST':
        otp = request.POST.get('otp')
        now = timezone.now()
        
        if employer.otp_blocked_until and now < employer.otp_blocked_until:
            messages.error(request, 'Account is blocked for 30 minutes due to multiple failed OTP attempts.')
            return render(request, 'verify.html', {'employer': employer})

        if employer.login_otp == otp and employer.login_otp_expiry_timestamp > now:
            employer.failed_otp_attempts = 0
            employer.save()
            request.session['user_email'] = email
            del request.session['verification_email']
            return redirect('home')
        else:
            employer.failed_otp_attempts += 1
            if employer.failed_otp_attempts >= 3:
                # Block for 30 mins after 3 failed OTP attempts
                employer.otp_blocked_until = now + timedelta(minutes=30)
                subject = 'Account Blocked: Login Verification Failed'
                message_body = "Your account is blocked for 30 minutes due to multiple failed OTP attempts during login."
                send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, [employer.email])
                messages.error(request, 'Account blocked for 30 minutes.')
            else:
                remaining_attempts = 3 - employer.failed_otp_attempts
                messages.error(request, f'Invalid or expired OTP. You have {remaining_attempts} attempts remaining.')
            employer.save()
            
    context = {'otp_expiry_timestamp': employer.login_otp_expiry_timestamp.isoformat() if employer.login_otp_expiry_timestamp else None}
    return render(request, 'verify.html', context)



def resend_login_otp(request):
    email = request.session.get('verification_email')
    if not email: return redirect('login')
    employer = Employer.objects.get(email=email)
    employer.generate_login_otp()
    subject = 'Your New Verification Code'
    message_body = f"Your new login verification code is: {employer.login_otp}"
    send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, [email])
    messages.success(request, 'A new OTP has been sent to your email.')
    return redirect('verify_login_otp')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email').strip().lower()
        try:
            employer = Employer.objects.get(email=email)
            employer.failed_otp_attempts = 0
            employer.forgot_password_timestamp = timezone.now()
            employer.save()
            employer.generate_reset_otp()
            subject = 'Your Password Reset Code'
            message_body = f"Hi {employer.first_name},\n\nYour password reset code is: {employer.reset_otp}"
            send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, [email])
            request.session['reset_email'] = email
            messages.info(request, 'Please check your registered mail for the password reset OTP.')
            return redirect('verify_reset_otp')
        except Employer.DoesNotExist:
            messages.error(request, 'Email not registered.')
    return render(request, 'forgot_password.html')


def verify_reset_otp(request):
    email = request.session.get('reset_email')
    if not email: return redirect('forgot_password')
    
    employer = Employer.objects.get(email=email)
    now = timezone.now()
    
    if request.method == 'POST':
        otp = request.POST.get('otp')
        now = timezone.now()
        
        if employer.otp_blocked_until and now < employer.otp_blocked_until:
            messages.error(request, 'Account is blocked for 24 hours due to multiple failed password reset attempts.')
            return render(request, 'verify.html', {'employer': employer})

        if employer.reset_otp == otp and employer.reset_otp_expiry_timestamp > now:
            employer.failed_otp_attempts = 0
            employer.save()
            request.session['reset_verified'] = True
            return redirect('reset_password')
        else:
            employer.failed_otp_attempts += 1
            if employer.failed_otp_attempts >= 3:
                employer.otp_blocked_until = now + timedelta(hours=24)
                subject = 'Account Blocked: Password Reset Attempts'
                message_body = "Your account is blocked for 24 hours due to multiple failed password reset attempts."
                send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, [employer.email])
                messages.error(request, 'Account blocked for 24 hours.')
            else:
                remaining_attempts = 3 - employer.failed_otp_attempts
                messages.error(request, f'Invalid or expired OTP. You have {remaining_attempts} attempts remaining.')
            employer.save()
            
    context = {'otp_expiry_timestamp': employer.reset_otp_expiry_timestamp.isoformat() if employer.reset_otp_expiry_timestamp else None}
    return render(request, 'verify.html', context)


def resend_reset_otp(request):
    email = request.session.get('reset_email')
    if not email: return redirect('forgot_password')
    employer = Employer.objects.get(email=email)
    employer.generate_reset_otp()
    subject = 'Your New Password Reset Code'
    message_body = f"Your new password reset code is: {employer.reset_otp}"
    send_mail(subject, message_body, settings.DEFAULT_FROM_EMAIL, [email])
    messages.success(request, 'A new OTP has been sent.')
    return redirect('verify_reset_otp')

def reset_password(request):
    if not request.session.get('reset_verified'):
        return redirect('forgot_password')
    
    email = request.session.get('reset_email')
    employer = Employer.objects.get(email=email)
    
    if request.method == 'POST':
        new_password = request.POST.get('newPassword')
        confirm_password = request.POST.get('confirmPassword')

        # Check if new password and confirm password match
        if new_password != confirm_password:
            messages.error(request, "New password and confirm password do not match.")
            return render(request, 'reset_password.html')

        # Check that new password is not the same as current or old
        if new_password == employer.password or new_password == employer.old_password:
            messages.error(request, "New password cannot be the same as your current or previous password.")
            return render(request, 'reset_password.html')

        # Check password complexity (optional, but recommended)
        if len(new_password) < 8 or not re.search(r'[A-Z]', new_password) or not re.search(r'[0-9]', new_password) or not re.search(r'[!@#$%^&*()]', new_password):
            messages.error(request, "Password must meet the complexity requirements.")
            return render(request, 'reset_password.html')

        # Update password
        employer.old_password = employer.password
        employer.password = new_password
        employer.password_reset_timestamp = timezone.now()
        employer.save()

        # Clean up session
        del request.session['reset_email']
        del request.session['reset_verified']

        messages.success(request, 'Password has been reset. Please log in.')
        return redirect('login')

    return render(request, 'reset_password.html')

@never_cache
def logout(request):
    request.session.flush()
    messages.success(request, "You have been logged out successfully.")
    return redirect('main_page')



@never_cache
def home(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, 'dashboard.html')

@never_cache
def dashboard_page(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, "dashboard.html")

@never_cache
def question_library_page(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, "question_library.html")

@never_cache
def java_advanced_assessment_view(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, "java_advanced_assessment.html")

@never_cache
def advanced_devops_view(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, 'advanced_devops_assessment.html')

@never_cache
def python_advanced_assessment_view(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, 'python_advanced_assessment.html')

@never_cache
def python_fundamentals_assessment_view(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, 'python_fundamentals_assessment.html')

@never_cache
def javascript_fundamentals_view(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, 'javascript_fundamentals.html')

@never_cache
def devops_assessment_view(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, 'devops_assessment.html')

@never_cache
def cybersecurity_assessment_view(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, 'cybersecurity_assessment.html')

@never_cache
def cybersecurity_advanced_assessment_view(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, 'cybersecurity_advanced_assessment.html')

@never_cache
def assessment_summary(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, "assessment_summary.html")

@never_cache
def assessment_library_page(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, "assessment_library.html")

@never_cache
def assessments_page(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, "assessments.html")

@never_cache
def configuration_page(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, "configuration.html")

@never_cache
def invite_options_page(request):
    if not request.session.get('user_email'):
        return redirect('login')
    
    return render(request, "invite_options.html")

def login_page_view(request):
    return render(request, 'login.html')  # Make sure login.html exists


from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import JsonResponse
import json
 
@csrf_exempt
def login_view(request, date_str=None):
    """
    Handles both GET and POST for candidate login. 
    GET -> render login.html
    POST -> process password login
    """
    if request.method == 'GET':
        # Render candidate login page with date if needed
        return render(request, 'candidate_pages/login.html', {'invite_date': date_str})

    elif request.method == 'POST':
        try:
            data = json.loads(request.body)
            password = data.get('password')
            redirect_url = data.get('redirectUrl', '/')

            if password == "FDI@123":
                return JsonResponse({'success': True, 'redirectUrl': '/welcome/'})
            else:
                return JsonResponse({'success': False, 'message': 'Invalid password.'}, status=401)

        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON.'}, status=400)

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)


def welcome_view(request):
    return render(request, 'candidate_pages/welcome.html')

def instructions_view(request):
    return render(request, 'candidate_pages/instructions.html')

def system_setup_view(request):
    return render(request, 'candidate_pages/system-setup.html')

def join_interview_view(request):
    return render(request, 'candidate_pages/join-interview.html')


@never_cache
def manual_testing_assessment_view(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, "manual_testing_assessment.html")

@never_cache
def advanced_manual_testing_assessment_view(request):   
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, "advanced_manual_testing_assessment.html")

@never_cache
def team_members_page(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, "team_members.html")

@never_cache
def company_profile_page(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, "company_profile.html")

@never_cache
def setting_page(request):
    if not request.session.get('user_email'):
        return redirect('login')
    return render(request, "setting.html")

def private_invite_login(request, invite_code):
    # This view is for handling private invites
    # You can implement your logic here to verify the invite code
    # and redirect to the appropriate page or render a template.
    if not request.session.get('user_email'):
        return redirect('login')
    
    # Example logic: if invite_code is valid, redirect to home
    if invite_code == "valid-invite-code":  # Replace with actual validation logic
        return redirect('home')
    
    messages.error(request, "Invalid invite code.")
    return redirect('login')

@never_cache
def automatic_assignment_view(request):
    if not request.session.get('user_email'):
        return redirect('login')
    if request.method == 'POST':
        name = request.POST.get('assignmentName')
        language = request.POST.get('language')
        level = request.POST.get('level')
        assessment_type = request.POST.get('type')
        builder = request.POST.get('builder')
        # Save in session if needed
        request.session['assessment_language'] = language
        request.session['assessment_level'] = level
        request.session['assessment_name'] = name
        # Pass language and level as GET params to assessment_questions
        return redirect(f"/assessment-questions/?language={language}&level={level}")
    return render(request, 'automatic.html')

@never_cache
def candidate_preview_view(request):
    language = request.session.get('assessment_language')
    level = request.session.get('assessment_level')
    removed_questions = request.session.get('removed_questions', [])
    level_map = {
        "fresher": "Beginner",
        "intermediate": "Intermediate",
        "experience": "Advanced",
    }
    model_map = {
        "cybersecurity": CybersecurityQuestion_Adv,
        "cybersecurity-adv": CybersecurityQuestion,
        "devops": AdvancedDevOpsQuestion,
        "javascript": JavaScriptQuestion,
        "testing": TestingQuestion,
        "sql": SQLQuestion,
        "python": PythonQuestion,
        "sap": SAPSDQuestion,
    }
    questions = []
    total_seconds = 0
    if language and level:
        mapped_level = level_map.get(level, "")
        model = model_map.get(language.lower())
        if model and mapped_level:
            questions = model.objects.filter(difficulty__iexact=mapped_level).exclude(question_id__in=removed_questions)
            # Sum up the time for all questions (assuming time is stored as string in minutes)
            for q in questions:
                try:
                    total_seconds += int(float(q.time)) * 60
                except Exception:
                    total_seconds += 60  # fallback: 1 min if invalid
    return render(request, 'candidate_preview.html', {
        'questions': questions,
        'total_seconds': total_seconds if questions else 0  # fallback to 0 if no questions
    })

@never_cache
def automatic_assessment_view(request):
    questions = []
    if request.method == "POST":
        language = request.POST.get("language")
        level = request.POST.get("level")
        assignment_name = request.POST.get("assignmentName")  # <-- Get assessment name
        start_time = request.POST.get("start_time")  # e.g. '2024-07-09 10:00'
        end_time = request.POST.get("end_time")
        time_limit = request.POST.get("time_limit")  # e.g. '60' (minutes)
        level_map = {
            "fresher": "Beginner",
            "intermediate": "Intermediate",
            "experience": "Advanced",
        }
        if not level or level not in level_map:
            return render(request, "Automatic.html", {"error": "Please select a candidate level."})
        mapped_level = level_map[level]
        model_map = {
            "cybersecurity": CybersecurityQuestion_Adv,
            "cybersecurity-adv": CybersecurityQuestion,
            "devops": AdvancedDevOpsQuestion,
            "javascript": JavaScriptQuestion,
            "testing": TestingQuestion,
            "sql": SQLQuestion,
            "python": PythonQuestion,
            "sap": SAPSDQuestion,
        }
        model = model_map.get(language.lower())
        removed_questions = request.session.get('removed_questions', [])
        if model:
            questions = model.objects.filter(difficulty__iexact=mapped_level).exclude(question_id__in=removed_questions)
        else:
            questions = []
 
        # --- CREATE AND SAVE THE ASSESSMENT OBJECT IF IT DOESN'T EXIST ---
        from .models import Assessment
        # You can set start_time, end_time, time_limit as needed (here set to None)
        from django.utils.dateparse import parse_datetime
        start_time_dt = parse_datetime(start_time) if start_time else None
        end_time_dt = parse_datetime(end_time) if end_time else None
        time_limit_int = int(time_limit) if time_limit else None
        assessment, created = Assessment.objects.get_or_create(
            name=assignment_name,
            defaults={
                'start_time': start_time_dt,
            'end_time': end_time_dt,
            'time_limit': time_limit_int,
            }
        )
        # ---------------------------------------------------------------
 
        # Save language, level, and assessment name in session for candidate preview and invite
        request.session['assessment_language'] = language
        request.session['assessment_level'] = level
        request.session['assessment_name'] = assignment_name  # <-- Save in session
        return render(request, "assessment_questions.html", {
            "questions": questions,
            "language": language,
            "level": level
        })
    request.session['removed_questions'] = []
    return render(request, "Automatic.html")


@never_cache
def assessment_questions_view(request):
    if not request.session.get('user_email'):
        return redirect('login')
    language = request.GET.get("language", "").lower()
    level = request.GET.get("level", "")
    level_map = {
        "fresher": "Beginner",
        "intermediate": "Intermediate",
        "experience": "Advanced",
    }
    mapped_level = level_map.get(level, "")
    model_map = {
        "cybersecurity": CybersecurityQuestion_Adv,
        "cybersecurity-adv": CybersecurityQuestion,
        "devops": AdvancedDevOpsQuestion,
        "javascript": JavaScriptQuestion,
        "testing": TestingQuestion,
        "sql": SQLQuestion,
        "python": PythonQuestion,
        "sap": SAPSDQuestion,
    }
    model = model_map.get(language)
    removed_questions = request.session.get('removed_questions', [])
    questions = []
    if model and mapped_level:
        questions = model.objects.filter(difficulty__iexact=mapped_level).exclude(question_id__in=removed_questions)
    return render(request, "assessment_questions.html", {
        "questions": questions,
        "language": language,
        "level": level,
    })  

 
def delete_selected_questions(request):
    if request.method == "POST":
        ids_to_remove = request.POST.getlist("selected_questions")
        language = request.POST.get("language", "").lower()
        level = request.POST.get("level", "")
        level_map = {
            "fresher": "Beginner",
            "intermediate": "Intermediate",
            "experience": "Advanced",
        }
        mapped_level = level_map.get(level, "")
        model_map = {
            "cybersecurity": CybersecurityQuestion_Adv,
            "cybersecurity-adv": CybersecurityQuestion,
            "devops": AdvancedDevOpsQuestion,
            "javascript": JavaScriptQuestion,
            "testing": TestingQuestion,
            "sql": SQLQuestion,
            "python": PythonQuestion,
            "sap": SAPSDQuestion,
        }
        model = model_map.get(language)
        # Get and update removed questions in session
        removed_questions = request.session.get('removed_questions', [])
        removed_questions += [qid for qid in ids_to_remove if qid not in removed_questions]
        request.session['removed_questions'] = removed_questions
        questions = []
        if model and mapped_level:
            questions = model.objects.filter(difficulty__iexact=mapped_level).exclude(question_id__in=removed_questions)
        return render(request, "assessment_questions.html", {
            "questions": questions,
            "language": language,
            "level": level,
        })
    return redirect('dashboard_page')
 
def invite_candidates_view(request):
    # Get language and level from session (set during assessment creation)
    language = request.session.get('assessment_language')
    level = request.session.get('assessment_level')
    removed_questions = request.session.get('removed_questions', [])
    assessment_name = request.session.get('assessment_name', '')
 
    level_map = {
        "fresher": "Beginner",
        "intermediate": "Intermediate",
        "experience": "Advanced",
    }
    model_map = {
        "cybersecurity": CybersecurityQuestion_Adv,
        "cybersecurity-adv": CybersecurityQuestion,
        "devops": AdvancedDevOpsQuestion,
        "javascript": JavaScriptQuestion,
        "testing": TestingQuestion,
        "sql": SQLQuestion,
        "python": PythonQuestion,
        "sap": SAPSDQuestion,
    }
 
    questions = []
    total_time = 0
    num_questions = 0
    if language and level:
        mapped_level = level_map.get(level, "")
        model = model_map.get(language.lower())
        if model and mapped_level:
            questions = model.objects.filter(difficulty__iexact=mapped_level).exclude(question_id__in=removed_questions)
            num_questions = questions.count()
            for q in questions:
                try:
                    total_time += int(float(q.time))
                except Exception:
                    total_time += 1  # fallback: 1 min if invalid
 
    return render(request, 'InviteCandidates.html', {
        'assessment_name': assessment_name,
        'number_of_questions': num_questions,
        'time_limit': f"{total_time} minutes",
        # ...other context...
    })
 
def classic_question_type(request):
    return render(request, 'classic_question_type.html')
 
from .models import AdvancedDevOpsQuestion  # or the correct model
from .models import SAPSDQuestion
from .models import CybersecurityQuestion_Adv
from .models import CybersecurityQuestion
from .models import JavaScriptQuestion
from .models import TestingQuestion
from .models import SQLQuestion
from .models import PythonQuestion
from .models import Assessment
import ast

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
 
@csrf_exempt
def check_answers(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_answers = data.get("answers", [])
            question_ids = data.get("question_ids", [])
            language = request.session.get('assessment_language')
 
            model_map = {
                "cybersecurity": CybersecurityQuestion_Adv,
                "cybersecurity-adv": CybersecurityQuestion,
                "devops": AdvancedDevOpsQuestion,
                "javascript": JavaScriptQuestion,
                "testing": TestingQuestion,
                "sql": SQLQuestion,
                "python": PythonQuestion,
                "sap": SAPSDQuestion,
            }
 
            model = model_map.get(language.lower()) if language else None
            if not model:
                return JsonResponse({"results": [False] * len(user_answers), "correct_answers": []})
 
            # Fetch questions
            questions = list(model.objects.filter(question_id__in=question_ids))
            questions_dict = {str(q.question_id): q for q in questions}
 
            results = []
            correct_answers_for_response = []
 
            for ua, qid in zip(user_answers, question_ids):
                q = questions_dict.get(str(qid))
                if not q:
                    results.append(False)
                    correct_answers_for_response.append("N/A")
                    continue
 
                # Parse correct_answers from string to list
                raw_ca = getattr(q, 'correct_answers', None)
                try:
                    ca = ast.literal_eval(raw_ca) if isinstance(raw_ca, str) else raw_ca
                except Exception as e:
                    print(f"Error parsing correct_answers for qid {qid}: {e}")
                    ca = []
 
                # Ensure it's a list
                if not isinstance(ca, list):
                    ca = [ca]
 
                # Convert user answer to int
                try:
                    ua_int = int(ua)
                except (ValueError, TypeError):
                    ua_int = None
                    print(f"[DEBUG] QID={qid} | UA={ua_int} | CA={ca}")  # ✅ this will help
 
                # Get option text(s)
                options = getattr(q, 'options', [])
                try:
                    correct_texts = [options[int(i)] for i in ca if isinstance(i, int) and i < len(options)]
                    ca_str = ", ".join(correct_texts)
                except Exception as e:
                    print(f"Error resolving correct option texts: {e}")
                    ca_str = "Unavailable"
 
                correct_answers_for_response.append(ca_str)
 
                # Match logic
                is_correct = ua_int in ca
                results.append(is_correct)
 
            return JsonResponse({
                "results": results,
                "correct_answers": correct_answers_for_response
            })
 
        except Exception as e:
            print("Error in check_answers:", e)
            return JsonResponse({"error": "Something went wrong on the server."}, status=500)
 
    return JsonResponse({"error": "Invalid request method"}, status=405)
 
@csrf_exempt
def send_invite_email(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            candidates = data.get("candidates", [])
            assessment_name = data.get("assessment_name", "")
            email_content = data.get("email_content", "")
 
            # Fetch the assessment object
            try:
                assessment = Assessment.objects.get(name=assessment_name)
            except Assessment.DoesNotExist:
                return JsonResponse({"success": False, "error": "Assessment not found."})
 
            # Try to get language and level from session (or elsewhere)
            language = request.session.get('assessment_language')
            level = request.session.get('assessment_level')
 
            model_map = {
                "cybersecurity": CybersecurityQuestion_Adv,
                "cybersecurity-adv": CybersecurityQuestion,
                "devops": AdvancedDevOpsQuestion,
                "javascript": JavaScriptQuestion,
                "testing": TestingQuestion,
                "sql": SQLQuestion,
                "python": PythonQuestion,
                "sap": SAPSDQuestion,
            }
 
            num_questions = 0
            total_time = 0
            if language and level:
                model = model_map.get(language.lower())
                level_map = {
                    "fresher": "Beginner",
                    "intermediate": "Intermediate",
                    "experience": "Advanced",
                }
                mapped_level = level_map.get(level)
                if model and mapped_level:
                    questions = model.objects.filter(difficulty__iexact=mapped_level)
                    num_questions = questions.count()
                    # Sum up the time for all questions (assuming time is stored as string in minutes)
                    for q in questions:
                        try:
                            total_time += int(float(q.time))
                        except Exception:
                            total_time += 1  # fallback: 1 min if invalid
 
            context = {
                'assessment_name': assessment.name,
                'number_of_questions': num_questions,
                'start_time': assessment.start_time,
                'end_time': assessment.end_time,
                'time_limit': f"{total_time} minutes",
            }
 
            subject = f"Invitation for {assessment.name}"
 
            for candidate in candidates:
                send_mail(
                    subject,
                    '',  # Plain text version (optional)
                    'no-reply@yourdomain.com',
                    [candidate['email']],
                    html_message=email_content  # Or use html_message if you render a template
                )
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    return JsonResponse({"success": False, "error": "Invalid request"}, status=400)
 


@never_cache
def main_page(request):
    return render(request, 'MainPage.html')

@api_view(["GET"])
def get_assessments(request):
    data = [
        {
            "id": "javaFullStack",
            "title": "Java Full stack",
            "description": "Covers full Java stack including Spring Boot & React.",
            "cardIconText": "FD",
            "cardIconBgColor": "#305598",
            "domain": "Tech",
            "imageUrl": "https://placehold.co/280x120/A52A2A/FFFFFF?text=Java+FS",
            "techTagsOverlay": ["JavaScript", "Oops", "Spring"],
            "isPremium": False,
            "createdDate": "2024-03-15",
            "viewLink": "java_advanced_assessment.html",
            "customizeLink": "java_advanced_assessment.html",
            "assessmentType": "Coding",
            "difficulty": "Intermediate",
            "ownedBy": "My Organization",
            "filterTags": ["JavaScript", "General", "Tech", "Java"],
            "humanLanguage": "English"
        },
    ]
    return Response(data)