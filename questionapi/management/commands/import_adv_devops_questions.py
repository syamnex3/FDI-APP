from django.core.management.base import BaseCommand
from questionapi.models import AdvancedDevOpsQuestion

QUESTIONS = [
    {
        "question_id": "adv_devops_1",
        "question_text_full": "What is the primary purpose of a Service Mesh in a microservices architecture?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "TECH",
        "points": "10",
        "time": "2-00",
        "topic": "Service Mesh",
        "options": [
            "To manage container orchestration",
            "To provide a dedicated infrastructure layer for handling service-to-service communication",
            "To automate the deployment of microservices",
            "To monitor application performance"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "adv_devops_2",
        "question_text_full": "In the context of DevSecOps, what is the 'Shift Left' principle?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Skills/Concepts",
        "domain": "TECH",
        "points": "8",
        "time": "2-00",
        "topic": "DevSecOps",
        "options": [
            "Moving security-related activities to the right side of the SDLC",
            "Integrating security into the earliest possible stages of the development lifecycle",
            "Focusing on security only during the production phase",
            "Automating security testing after deployment"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "adv_devops_3",
        "question_text_full": "Which of the following are key metrics for measuring the effectiveness of a CI/CD pipeline?",
        "question_type": "Multiple Selection",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Skills/Concepts",
        "domain": "TECH",
        "points": "9",
        "time": "2-00",
        "topic": "CI/CD Metrics",
        "options": [
            "Deployment Frequency",
            "Lead Time for Changes",
            "Change Failure Rate",
            "Mean Time to Recovery (MTTR)"
        ],
        "correct_answers": [0, 1, 2, 3]
    },
    {
        "question_id": "adv_devops_4",
        "question_text_full": "What is the role of a sidecar container in a Kubernetes pod?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skills/Concepts",
        "domain": "TECH",
        "points": "10",
        "time": "2-00",
        "topic": "Kubernetes",
        "options": [
            "To run the main application logic",
            "To enhance or extend the functionality of the main container",
            "To store persistent data for the pod",
            "To manage network traffic for the pod"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "adv_devops_5",
        "question_text_full": "Which of the following tools is NOT primarily used for Infrastructure as Code (IaC)?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall & Reproduction",
        "domain": "TECH",
        "points": "5",
        "time": "2-00",
        "topic": "IaC Tools",
        "options": [
            "Terraform",
            "Ansible",
            "Jenkins",
            "Pulumi"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "adv_devops_6",
        "question_text_full": "What are the three pillars of observability in a DevOps context?",
        "question_type": "Multiple Selection",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Skills/Concepts",
        "domain": "TECH",
        "points": "8",
        "time": "2-00",
        "topic": "Observability",
        "options": [
            "Metrics",
            "Logs",
            "Traces",
            "Alerts"
        ],
        "correct_answers": [0, 1, 2]
    },
    {
        "question_id": "adv_devops_7",
        "question_text_full": "What is GitOps?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "TECH",
        "points": "12",
        "time": "2-00",
        "topic": "GitOps",
        "options": [
            "A way of managing infrastructure and applications where Git is the single source of truth",
            "A tool for visualizing Git history",
            "A methodology for optimizing Git performance",
            "A set of best practices for writing clean code"
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "adv_devops_8",
        "question_text_full": "Which of the following are valid strategies for managing secrets in a Kubernetes environment?",
        "question_type": "Multiple Selection",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "TECH",
        "points": "11",
        "time": "2-00",
        "topic": "Kubernetes Secrets",
        "options": [
            "Using Kubernetes Secrets",
            "Storing secrets in a version control system",
            "Using a dedicated secrets management tool like HashiCorp Vault",
            "Hardcoding secrets in container images"
        ],
        "correct_answers": [0, 2]
    }
]

class Command(BaseCommand):
    help = 'Import Advanced DevOps Questions'

    def handle(self, *args, **kwargs):
        for q in QUESTIONS:
            AdvancedDevOpsQuestion.objects.update_or_create(
                question_id=q["question_id"],
                defaults=q
            )
        self.stdout.write(self.style.SUCCESS('Advanced DevOps questions imported!'))