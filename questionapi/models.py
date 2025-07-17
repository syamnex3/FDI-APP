from django.db import models
from django.utils import timezone
import random
from datetime import timedelta


class Employer(models.Model):
    # Registration Fields
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    organization_name = models.CharField(max_length=50)
    registration_timestamp = models.DateTimeField(auto_now_add=True)
    old_password = models.CharField(max_length=50, blank=True, null=True)

    # Login and OTP Fields
    last_login_timestamp = models.DateTimeField(null=True, blank=True)
    login_otp = models.CharField(max_length=6, null=True, blank=True)
    login_otp_sent_timestamp = models.DateTimeField(null=True, blank=True)
    login_otp_expiry_timestamp = models.DateTimeField(null=True, blank=True)

    # Password Reset Fields
    forgot_password_timestamp = models.DateTimeField(null=True, blank=True)
    reset_otp = models.CharField(max_length=6, null=True, blank=True)
    reset_otp_sent_timestamp = models.DateTimeField(null=True, blank=True)
    reset_otp_expiry_timestamp = models.DateTimeField(null=True, blank=True)
    password_reset_timestamp = models.DateTimeField(null=True, blank=True)

    # Security Fields
    failed_login_attempts = models.IntegerField(default=0)
    failed_otp_attempts = models.IntegerField(default=0)
    account_blocked_until = models.DateTimeField(null=True, blank=True)
    otp_blocked_until = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.email

    def generate_login_otp(self):
        self.login_otp = str(random.randint(100000, 999999))
        self.login_otp_sent_timestamp = timezone.now()
        self.login_otp_expiry_timestamp = timezone.now() + timedelta(minutes=1)
        self.save()

    def generate_reset_otp(self):
        self.reset_otp = str(random.randint(100000, 999999))
        self.reset_otp_sent_timestamp = timezone.now()
        self.reset_otp_expiry_timestamp = timezone.now() + timedelta(minutes=2)
        self.save()


class Assessment(models.Model):
    ASSESSMENT_TYPE_CHOICES = [
        ("manual", "Manual"),
        ("automatic", "Automatic"),
    ]

    BUILDER_CHOICES = [
        ("pre-built", "Use Pre-Built Assessment"),
        ("library-questions", "Start Using Library Questions"),
    ]

    LEVEL_CHOICES = [
        ("fresher", "Fresher (0-1 Year)"),
        ("intermediate", "Intermediate (1-3 Years)"),
        ("experience", "Experience (3+ Years)"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=50, choices=ASSESSMENT_TYPE_CHOICES, default="manual")
    builder = models.CharField(max_length=50, choices=BUILDER_CHOICES, blank=True, null=True)
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES, blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    tags = models.CharField(max_length=255, blank=True)
    total_time = models.DurationField(default="00:30:00")
    total_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Question(models.Model):
    QUESTION_TYPES = [
        ("MCQ", "Multiple Choice"),
        ("MSQ", "Multiple Selection"),
        ("Text", "Text Entry"),
        ("Code", "Coding"),
        ("Upload", "File Upload"),
    ]

    DIFFICULTY_LEVELS = [
        ("Basic", "Basic"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced"),
    ]

    DEPTH_OF_KNOWLEDGE = [
        ("Recall", "Recall & Reproduction"),
        ("Skill", "Skills/Concepts"),
        ("Strategic", "Strategic Thinking"),
        ("Extended", "Extended Thinking"),
    ]

    DOMAIN_CHOICES = [
        ("TECH", "TECH"),
        ("NON-TECH", "NON-TECH"),
    ]

    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name="questions")
    question_text = models.TextField()
    topic = models.CharField(max_length=255)
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES, default="MCQ")
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_LEVELS, default="Intermediate")
    depth_of_knowledge = models.CharField(max_length=20, choices=DEPTH_OF_KNOWLEDGE, default="Skill")
    domain = models.CharField(max_length=10, choices=DOMAIN_CHOICES, default="TECH")
    time_limit = models.DurationField(default="00:05:00")
    points = models.PositiveIntegerField(default=2)

    def __str__(self):
        return self.question_text[:80]


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="options")
    text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Reviewer(models.Model):
    REVIEWER_TYPE_CHOICES = [
        ("external", "External Reviewer"),
        ("team", "Team Member"),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    reviewer_type = models.CharField(max_length=20, choices=REVIEWER_TYPE_CHOICES)
    assigned_assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name="reviewers")

    def __str__(self):
        return f"{self.name} ({self.email})"

 
 
class AdvancedDevOpsQuestion(models.Model):
    question_id = models.CharField(max_length=100, unique=True)
    question_text_full = models.TextField()
    question_type = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50)
    depth_of_knowledge = models.CharField(max_length=50)
    domain = models.CharField(max_length=50)
    points = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    topic = models.CharField(max_length=100)
    options = models.JSONField()
    correct_answers = models.JSONField()
 
    def __str__(self):
        return self.question_text_full
class CybersecurityQuestion(models.Model):
    question_id = models.CharField(max_length=100, unique=True)
    question_text_full = models.TextField()
    question_type = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    depth_of_knowledge = models.CharField(max_length=100)
    domain = models.CharField(max_length=50)
    points = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    topic = models.CharField(max_length=100)
    options = models.JSONField()
    correct_answers = models.JSONField()
 
    def __str__(self):
        return f"{self.question_id}: {self.question_text_full[:50]}"
class CybersecurityQuestion_Adv(models.Model):
    question_id = models.CharField(max_length=100, unique=True)
    question_text_full = models.TextField()
    question_type = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    depth_of_knowledge = models.CharField(max_length=100)
    domain = models.CharField(max_length=50)
    points = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    topic = models.CharField(max_length=100)
    options = models.JSONField(default=list)
    correct_answers = models.JSONField(default=list)
 
    def __str__(self):
            return f"{self.question_id}: {self.question_text_full[:50]}"
   
class JavaScriptQuestion(models.Model):
    question_id = models.CharField(max_length=100, unique=True)
    question_text_full = models.TextField()
    question_type = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    depth_of_knowledge = models.CharField(max_length=100)
    domain = models.CharField(max_length=50)
    points = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    topic = models.CharField(max_length=100)
    options = models.JSONField(default=list)
    correct_answers = models.JSONField(default=list)
 
    def __str__(self):
        return self.question_text_full
class TestingQuestion(models.Model):
    question_id = models.CharField(max_length=100, unique=True)
    question_text_full = models.TextField()
    question_type = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    depth_of_knowledge = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    points = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    topic = models.CharField(max_length=100)
    options = models.JSONField(default=list)
    correct_answers = models.JSONField(default=list)
 
    def __str__(self):
        return self.question_text_full
class SQLQuestion(models.Model):
    question_id = models.CharField(max_length=100, unique=True)
    question_text_full = models.TextField()
    question_type = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    depth_of_knowledge = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    points = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    topic = models.CharField(max_length=100)
    options = models.JSONField(default=list)
    correct_answers = models.JSONField(default=list)
 
    def __str__(self):
        return self.question_text_full
class PythonQuestion(models.Model):
    question_id = models.CharField(max_length=100, unique=True)
    question_text_full = models.TextField()
    question_type = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    depth_of_knowledge = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    points = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    topic = models.CharField(max_length=100)
    options = models.JSONField(default=list)
    correct_answers = models.JSONField(default=list)
 
    def __str__(self):
        return self.question_text_full
class SAPSDQuestion(models.Model):
    question_id = models.CharField(max_length=100, unique=True)
    question_text_full = models.TextField()
    question_type = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    depth_of_knowledge = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    points = models.CharField(max_length=10)
    time = models.CharField(max_length=20)
    topic = models.CharField(max_length=100)
    options = models.JSONField()
    correct_answers = models.JSONField()
 
    def __str__(self):
        return f"{self.question_id}: {self.question_text_full[:50]}"
class JavaQuestion(models.Model):
    question_id = models.CharField(max_length=100, unique=True)
    question_text_full = models.TextField()
    question_type = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    depth_of_knowledge = models.CharField(max_length=100)
    domain = models.CharField(max_length=100)
    points = models.CharField(max_length=10)
    time = models.CharField(max_length=20)
    topic = models.CharField(max_length=100)
    options = models.JSONField()
    correct_answers = models.JSONField()
 
    def __str__(self):
        return f"{self.question_id}: {self.question_text_full[:50]}"
   
 
# In your assessment creation view (example)
from .models import Assessment
 
def create_assessment(request):
    if request.method == "POST":
        name = request.POST.get("assignmentName")
        start_time = ...  # get from form or set default
        end_time = ...    # get from form or set default
        time_limit = ...  # get from form or set default
 
        # Create and save the assessment if it doesn't exist
        assessment, created = Assessment.objects.get_or_create(
            name=name,
            defaults={
                'start_time': start_time,
                'end_time': end_time,
                'time_limit': time_limit,
            }
        )
        # ...rest of your logic...