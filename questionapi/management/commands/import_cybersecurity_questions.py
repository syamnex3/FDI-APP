from django.core.management.base import BaseCommand
from questionapi.models import CybersecurityQuestion

QUESTIONS = [
    {
        "question_id": "cs_adv_1",
        "question_text_full": "When analyzing a potential zero-day exploit in a PDF file, which of the following actions is LEAST useful in the initial triage phase?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "TECH",
        "points": "15",
        "time": "5-00",
        "topic": "Malware Analysis",
        "options": [
            "Running 'strings' on the file to look for suspicious keywords like '/JavaScript' or '/Launch'",
            "Using a PDF parser to examine the document's object structure for anomalies",
            "Opening the PDF on a fully patched, isolated virtual machine to observe its behavior",
            "Submitting the file's hash to VirusTotal to check for existing detections"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "cs_adv_2",
        "question_text_full": "Which phase of the Advanced Persistent Threat (APT) lifecycle is MOST critical for an attacker to maintain long-term access to a compromised network?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "TECH",
        "points": "12",
        "time": "4-00",
        "topic": "Threat Intelligence",
        "options": [
            "Initial Compromise",
            "Command & Control (C2)",
            "Persistence",
            "Lateral Movement"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "cs_adv_3",
        "question_text_full": "How can a security analyst reliably detect a kernel-level rootkit that hooks the System Service Descriptor Table (SSDT)?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Extended Thinking",
        "domain": "TECH",
        "points": "18",
        "time": "6-00",
        "topic": "Forensics",
        "options": [
            "By running a standard antivirus scan in normal boot mode.",
            "By comparing the in-memory SSDT pointers to the pointers from the on-disk ntoskrnl.exe file.",
            "By checking the integrity of user-mode application files in C:\\Windows\\System32.",
            "By monitoring outbound network traffic for anomalies."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "cs_adv_4",
        "question_text_full": "In digital steganography, what is the Least Significant Bit (LSB) insertion technique primarily used for?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "TECH",
        "points": "10",
        "time": "3-30",
        "topic": "Cryptography",
        "options": [
            "To encrypt the hidden message with a strong algorithm.",
            "To make the hidden data resistant to image compression.",
            "To hide data within an image or audio file with minimal perceptible distortion.",
            "To significantly increase the file size of the cover medium."
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "cs_adv_5",
        "question_text_full": "What is a primary security challenge unique to SCADA (Supervisory Control and Data Acquisition) and Industrial Control Systems (ICS)?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "TECH",
        "points": "14",
        "time": "4-30",
        "topic": "OT Security",
        "options": [
            "The widespread use of strong, end-to-end encryption.",
            "The need to prioritize system availability and safety over confidentiality, often preventing timely patching.",
            "The frequent and mandatory use of multi-factor authentication for all operator actions.",
            "The systems are typically air-gapped and have no connection to external networks."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "cs_adv_6",
        "question_text_full": "When reverse-engineering packed or obfuscated malware, what is the purpose of a debugger's 'hardware breakpoint'?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "TECH",
        "points": "16",
        "time": "5-00",
        "topic": "Reverse Engineering",
        "options": [
            "To pause execution when a specific API function is called.",
            "To stop execution when a section of memory is read, written to, or executed, which is useful for unpacking.",
            "To automatically analyze and de-obfuscate encrypted strings within the binary.",
            "To trace the malware's network communication with its C2 server."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "cs_adv_7",
        "question_text_full": "A company uses a multi-cloud strategy (AWS and Azure). What is the MOST effective tool or concept for managing access permissions consistently across both environments?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "TECH",
        "points": "15",
        "time": "5-00",
        "topic": "Cloud Security",
        "options": [
            "AWS IAM Roles",
            "Azure Active Directory",
            "A Cloud Security Posture Management (CSPM) tool",
            "Terraform Infrastructure as Code (IaC)"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "cs_adv_8",
        "question_text_full": "What is the primary threat that quantum computing poses to current-day public-key cryptography (like RSA and ECC)?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Recall",
        "domain": "TECH",
        "points": "15",
        "time": "4-00",
        "topic": "Cryptography",
        "options": [
            "It can brute-force symmetric encryption keys (like AES-256) almost instantly.",
            "It can efficiently solve the integer factorization and discrete logarithm problems.",
            "It allows for the creation of unbreakable symmetric encryption algorithms.",
            "It can intercept and decrypt encrypted data in transit without being detected."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "cs_adv_9",
        "question_text_full": "In the context of AI/ML in cybersecurity, what is an 'adversarial attack'?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "TECH",
        "points": "12",
        "time": "4-00",
        "topic": "AI in Security",
        "options": [
            "An attack where AI is used to automate the process of finding software vulnerabilities.",
            "A physical attack against the data center hosting an AI model.",
            "A technique to fool a machine learning model by providing deceptive, specially crafted input.",
            "Using an AI-powered chatbot to perform social engineering on employees."
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "cs_adv_10",
        "question_text_full": "The SolarWinds Orion hack is a prime example of which type of sophisticated attack?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Recall",
        "domain": "TECH",
        "points": "10",
        "time": "3-00",
        "topic": "Threat Intelligence",
        "options": [
            "A zero-day exploit",
            "A DDoS attack",
            "A supply chain attack",
            "A ransomware attack"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "cs_adv_11",
        "question_text_full": "When mitigating a large-scale DDoS attack, what is the primary function of a 'scrubbing center'?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "TECH",
        "points": "14",
        "time": "4-00",
        "topic": "Network Security",
        "options": [
            "To absorb the attack traffic and pass only legitimate traffic to the origin server.",
            "To identify the geographical source of the attack and block the corresponding countries.",
            "To shut down the target's web server to prevent damage.",
            "To negotiate with the attackers to stop the DDoS campaign."
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "cs_adv_12",
        "question_text_full": "What is the fundamental difference between a heap spray attack and a classic stack buffer overflow?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "TECH",
        "points": "15",
        "time": "5-00",
        "topic": "Exploit Development",
        "options": [
            "Heap sprays target kernel memory, while stack overflows target user memory.",
            "Stack overflows overwrite a return address, while heap sprays fill memory with shellcode to increase the chance of landing on it.",
            "Heap sprays only work on 64-bit systems.",
            "Stack overflows are easier to detect with canaries, while heap sprays are not."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "cs_adv_13",
        "question_text_full": "The Spectre and Meltdown vulnerabilities are examples of what class of hardware-based attacks?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Recall",
        "domain": "TECH",
        "points": "16",
        "time": "4-30",
        "topic": "Hardware Security",
        "options": [
            "Rowhammer attacks",
            "Side-channel attacks",
            "Firmware rootkits",
            "Evil maid attacks"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "cs_adv_14",
        "question_text_full": "Which technique is most effective for a state-level actor to potentially de-anonymize a user on the Tor network?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "TECH",
        "points": "18",
        "time": "6-00",
        "topic": "Network Security",
        "options": [
            "Using a simple packet sniffer on the user's local network.",
            "Controlling a large number of Tor entry and exit nodes to perform traffic correlation.",
            "Launching a DDoS attack against the Tor directory authorities.",
            "Blocking all known Tor exit node IP addresses."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "cs_adv_15",
        "question_text_full": "During a forensic investigation, what is the primary challenge posed by 'fileless malware'?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "TECH",
        "points": "15",
        "time": "5-00",
        "topic": "Forensics",
        "options": [
            "It is too heavily encrypted to be analyzed.",
            "It leaves minimal to no artifacts on the hard disk, existing primarily in RAM.",
            "It only infects network devices like routers and switches.",
            "It self-deletes immediately after execution, leaving no traces whatsoever."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "cs_adv_16",
        "question_text_full": "Which of the following BEST describes the goal of 'threat hunting'?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "TECH",
        "points": "12",
        "time": "4-00",
        "topic": "SOC Operations",
        "options": [
            "Reacting to alerts generated by SIEM and EDR tools.",
            "Proactively and iteratively searching through networks to detect and isolate advanced threats that evade existing security solutions.",
            "Conducting penetration tests to find vulnerabilities.",
            "Developing new signatures for antivirus software based on known malware samples."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "cs_adv_17",
        "question_text_full": "What is the primary purpose of Resource Public Key Infrastructure (RPKI) in preventing BGP hijacking?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "TECH",
        "points": "17",
        "time": "5-30",
        "topic": "Network Security",
        "options": [
            "To encrypt BGP update messages between routers.",
            "To allow network operators to create cryptographically signed statements about which Autonomous System (AS) is authorized to originate a specific IP prefix.",
            "To mandate the use of multi-factor authentication for router administrators.",
            "To provide a real-time reputation score for every AS on the internet."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "cs_adv_18",
        "question_text_full": "In software security testing, what is 'fuzzing'?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "TECH",
        "points": "12",
        "time": "4-00",
        "topic": "Secure Development",
        "options": [
            "A manual code review technique to find logical flaws.",
            "A static analysis method that scans source code for known vulnerability patterns.",
            "An automated testing technique that provides invalid, unexpected, or random data as inputs to a program to find crashes and bugs.",
            "A formal verification method to mathematically prove the correctness of a program's logic."
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "cs_adv_19",
        "question_text_full": "What is a major security risk when running containers (e.g., Docker) in 'privileged' mode?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "TECH",
        "points": "14",
        "time": "4-30",
        "topic": "Cloud Security",
        "options": [
            "It slightly increases the container's CPU and memory usage.",
            "It prevents the container from accessing the network.",
            "It effectively disables all security isolation, allowing a compromised container to gain root access to the host machine.",
            "It requires a special license from the container runtime provider."
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "cs_adv_20",
        "question_text_full": "In the context of blockchain and smart contracts, what is a 'reentrancy attack'?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "TECH",
        "points": "18",
        "time": "6-00",
        "topic": "Blockchain Security",
        "options": [
            "An attack that floods the blockchain network with spam transactions.",
            "An attack where an external malicious contract repeatedly calls back into the victim contract's function before the first invocation is finished, often to drain funds.",
            "An attack that attempts to guess the private key of a cryptocurrency wallet.",
            "An attack that modifies the timestamp of a block to gain an advantage."
        ],
        "correct_answers": [1]
    }
]

class Command(BaseCommand):
    help = 'Import advanced cybersecurity questions'

    def handle(self, *args, **kwargs):
        for q in QUESTIONS:
            CybersecurityQuestion.objects.update_or_create(
                question_id=q["question_id"],
                defaults={
                    "question_text_full": q["question_text_full"],
                    "question_type": q["question_type"],
                    "difficulty": q["difficulty"],
                    "depth_of_knowledge": q["depth_of_knowledge"],
                    "domain": q["domain"],
                    "points": q["points"],
                    "time": q["time"],
                    "topic": q["topic"],
                    "options": q["options"],
                    "correct_answers": q["correct_answers"],
                }
            )
        self.stdout.write(self.style.SUCCESS('All cybersecurity questions imported!'))