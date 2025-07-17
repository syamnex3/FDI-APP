
from django.urls import path, re_path
from . import views
from .views import (
    automatic_assignment_view, company_profile_page, delete_selected_questions, javascript_fundamentals_view, question_library_page, get_assessments,
    java_advanced_assessment_view, advanced_devops_view, python_advanced_assessment_view,
    python_fundamentals_assessment_view, devops_assessment_view,
    cybersecurity_assessment_view, cybersecurity_advanced_assessment_view,
    dashboard_page, assessment_summary, assessment_library_page,
    assessments_page, configuration_page, invite_options_page, setting_page, team_members_page,
    assessment_questions_view
)

urlpatterns = [

    path('', views.main_page, name='main_page'),
    path('register/', views.register, name='register'),

    # --- CHANGE THIS LINE ---
    # This is for your 'main login' that expects email and password via traditional form/request.POST
    path('employer-login/', views.login, name='employer_login'), # <--- CHANGED THE PATH AND NAME
    path('login/', views.login_page_view, name='login_page'),  # <-- handles GET
    path('api/login/', views.login_view, name='login_api'),

    path('login/', views.login_page_view, name='login'),
 


    path('logout/', views.logout, name='logout'),
    
    path('verify_login_otp/', views.verify_login_otp, name='verify_login_otp'),
    path('resend_login_otp/', views.resend_login_otp, name='resend_login_otp'),

    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('verify_reset_otp/', views.verify_reset_otp, name='verify_reset_otp'),
    path('resend_reset_otp/', views.resend_reset_otp, name='resend_reset_otp'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('assessments/', get_assessments),

    path('home/', views.home, name='home'),

    # All other specific views
    path('question-library/', question_library_page, name='question_library'),
    path('java-advanced-assessment/', java_advanced_assessment_view),
    path('advanced-devops-assessment/', advanced_devops_view),
    path('python-advanced-assessment/', python_advanced_assessment_view),
    path('python-fundamentals-assessment/', python_fundamentals_assessment_view),
    path('javascript-fundamentals/', javascript_fundamentals_view),
    path('devops-assessment/', devops_assessment_view),
    path('cybersecurity-assessment/', cybersecurity_assessment_view),
    path('cybersecurity-advanced-assessment/', cybersecurity_advanced_assessment_view),
    path('dashboard/', dashboard_page, name='dashboard_page'),
    path('assessment-summary/', assessment_summary, name='assessment_summary'),
    path('assessment-library/', assessment_library_page, name='assessment_library'),
    path('assessments-page/', assessments_page, name='assessments_page'),
    path('configuration/', configuration_page, name='configuration_page'),
    path('invite-options/', invite_options_page, name='invite_options_page'),
    
    # URLs for dynamically generated public/private invites (e.g., /assess/20250711/)
    re_path(r'^assess/(?P<date_str>\d{8})/$', views.login_view, name='public_invite_login'),
    re_path(r'^invite/(?P<date_str>\d{8})/$', views.login_view, name='private_invite_login'),
 
 
    # --- KEEP THIS LINE AS IS ---
    # This URL is specifically for the POST request from your login.html (invite flow)
    # It routes to login_view which correctly processes JSON and expects only password.


    # NEW URLs for the post-login flow (as previously defined)
    path('welcome/', views.welcome_view, name='welcome'),
    path('instructions/', views.instructions_view, name='instructions'),
    path('system-setup/', views.system_setup_view, name='system_setup'),
    path('join-interview/', views.join_interview_view, name='join_interview'),
    path('team-members/', team_members_page, name='team_members_page'),
    path('company-profile/', company_profile_page, name='company_profile_page'),
    path('setting/', setting_page, name='setting_page'),
    path('automatic/', automatic_assignment_view, name='automatic'),
    path('assessment-questions/', assessment_questions_view, name='assessment_questions'),
    path('delete-selected-questions/', delete_selected_questions, name='delete_selected_questions'),
    path('manual-testing-assessment/', views.manual_testing_assessment_view, name='manual_testing_assessment'),
    path('advanced-manual-testing-assessment/', views.advanced_manual_testing_assessment_view, name='advanced_manual_testing_assessment'),
    path('delete-selected-questions/', views.delete_selected_questions, name='delete_selected_questions'),
    path('invite-candidates/', views.invite_candidates_view, name='invite-candidates'),
    path('candidate-preview/', views.candidate_preview_view, name='candidate_preview'),
    path('classic-question-type/', views.classic_question_type, name='classic_question_type'),
    path('check_answers/', views.check_answers, name='check_answers'),
    path('send-invite-email/', views.send_invite_email, name='send_invite_email'),
    path('invite/<str:invite_code>/', views.private_invite_login, name='private_invite'), # This seems to be a new invite URL for a code, ensure it doesn't conflict with date-based one if not intended
]