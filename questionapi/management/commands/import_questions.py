from django.core.management.base import BaseCommand
from questionapi.models import Question

QUESTIONS = [
    {
        "question_text": "How would you define cryptography?",
        "option_a": "A technique for compressing information for storage",
        "option_b": "A method for debugging code",
        "option_c": "A practice of securing communication and information",
        "option_d": "A tool for network traffic analysis",
        "answer": "c"
    },
    {
        "question_text": "How does symmetric encryption differ from asymmetric encryption?",
        "option_a": "Symmetric uses different keys; Asymmetric uses same key",
        "option_b": "Symmetric is slower; Asymmetric is faster",
        "option_c": "Symmetric uses same key for encryption and decryption; Asymmetric uses different keys",
        "option_d": "Both use the same keys for all operations",
        "answer": "c"
    },
    {
        "question_text": "In what ways do IDS and IPS differ?",
        "option_a": "IDS detects intrusions and prevents them; IPS only detects",
        "option_b": "IDS prevents intrusions; IPS only reports them",
        "option_c": "IDS only detects intrusions; IPS detects and prevents them",
        "option_d": "IDS blocks intrusions automatically; IPS requires manual action",
        "answer": "c"
    },
    {
        "question_text": "In cybersecurity, what does the acronym CIA represent?",
        "option_a": "Control, Identity, Access",
        "option_b": "Confidentiality, Integrity, Availability",
        "option_c": "Connectivity, Internet, Access",
        "option_d": "Compliance, Intrusion, Alert",
        "answer": "b"
    },
    {
        "question_text": "What makes encryption and hashing fundamentally different?",
        "option_a": "Both can be reversed",
        "option_b": "Encryption is irreversible; hashing is reversible",
        "option_c": "Encrypted data can be decrypted; hashed data cannot be reversed",
        "option_d": "Encryption is used to validate data integrity",
        "answer": "c"
    },
    {
        "question_text": "Why is a firewall important in cybersecurity?",
        "option_a": "Enhancing web page speed",
        "option_b": "Monitoring and controlling network traffic",
        "option_c": "Enabling remote access",
        "option_d": "Compressing database data",
        "answer": "b"
    },
    {
        "question_text": "How do penetration testing and vulnerability assessment differ?",
        "option_a": "PT finds and reports issues; VA fixes them",
        "option_b": "VA is done post-exploit; PT is proactive",
        "option_c": "VA finds flaws; PT tests exploitation of those flaws",
        "option_d": "VA fixes system configurations; PT updates firewalls",
        "answer": "c"
    },
    {
        "question_text": "What is the process of the TCP three-way handshake?",
        "option_a": "ACK → SYN → SYN-ACK",
        "option_b": "SYN → SYN-ACK → ACK",
        "option_c": "HELLO → ACK → SYN",
        "option_d": "CONNECT → LISTEN → SEND",
        "answer": "b"
    },
    {
        "question_text": "Which HTTP status codes indicate an error caused by the client?",
        "option_a": "1xx",
        "option_b": "2xx",
        "option_c": "3xx",
        "option_d": "4xx",
        "answer": "d"
    },
    {
        "question_text": "What information does the traceroute command provide?",
        "option_a": "To trace viruses in email",
        "option_b": "To identify the hops a packet takes to reach a destination",
        "option_c": "To secure the route of packets",
        "option_d": "To analyze encrypted network sessions",
        "answer": "b"
    },
    {
        "question_text": "In what way are HIDS and NIDS different?",
        "option_a": "HIDS works on networks; NIDS on hosts",
        "option_b": "HIDS monitors network traffic; NIDS monitors device behavior",
        "option_c": "HIDS monitors a specific host; NIDS monitors the entire network",
        "option_d": "HIDS is faster than NIDS",
        "answer": "c"
    },
    {
        "question_text": "Which option does not belong to the firewall configuration process?",
        "option_a": "Enabling remote administration",
        "option_b": "Changing default password",
        "option_c": "Setting up logging",
        "option_d": "Configuring firewall rules",
        "answer": "a"
    },
    {
        "question_text": "What is the primary purpose of SSL?",
        "option_a": "Analyze network traffic",
        "option_b": "Block spam emails",
        "option_c": "Create secure, encrypted browser-server connections",
        "option_d": "Optimize data transmission speeds",
        "answer": "c"
    },
    {
        "question_text": "Which of the following is NOT considered a best practice for server security?",
        "option_a": "Disabling root remote access",
        "option_b": "Creating new user accounts",
        "option_c": "Using weak passwords for admin",
        "option_d": "Configuring firewall rules",
        "answer": "c"
    },
    {
        "question_text": "What does the term 'data leakage' mean?",
        "option_a": "Data shared through encrypted channels",
        "option_b": "Authorized data transfer to cloud",
        "option_c": "Unauthorized or accidental transmission of sensitive data",
        "option_d": "Storing logs without permissions",
        "answer": "c"
    },
    {
        "question_text": "Identify the option that does NOT represent a form of cyberattack.",
        "option_a": "Malware",
        "option_b": "Man-in-the-middle",
        "option_c": "Wi-Fi extension",
        "option_d": "Phishing",
        "answer": "c"
    },
    {
        "question_text": "What is effective method to prevent brute force attacks?",
        "option_a": "Using CAPTCHA",
        "option_b": "Limiting login attempts",
        "option_c": "Using strong password policies",
        "option_d": "All of the above",
        "answer": "d"
    },
    {
        "question_text": "What does the term 'port scanning' mean in cybersecurity?",
        "option_a": "Closing all ports on a server",
        "option_b": "Checking server uptime",
        "option_c": "Identifying open ports and services on a host",
        "option_d": "Sending encrypted requests",
        "answer": "c"
    },
    {
        "question_text": "OSI model consists of how many layers?",
        "option_a": "5",
        "option_b": "6",
        "option_c": "7",
        "option_d": "4",
        "answer": "c"
    },
    {
        "question_text": "Why is a VPN used in networking?",
        "option_a": "Speeding up internet",
        "option_b": "Encrypting and securing network communication",
        "option_c": "Bypassing antivirus",
        "option_d": "Blocking websites",
        "answer": "b"
    },
    {
        "question_text": "Which of the following best explains the terms 'risk,' 'vulnerability,' and 'threat'?",
        "option_a": "Threat is a risk of vulnerability; vulnerability is harmless",
        "option_b": "Vulnerability is weakness; threat is potential harm; risk is result when exploited",
        "option_c": "Risk is random; vulnerability is secure; threat is not measurable",
        "option_d": "All terms mean the same",
        "answer": "b"
    },
    {
        "question_text": "Select the option that does NOT help protect against identity theft.",
        "option_a": "Using old browsers",
        "option_b": "Using antivirus software",
        "option_c": "Avoiding sharing sensitive data online",
        "option_d": "Using strong passwords",
        "answer": "a"
    },
    {
        "question_text": "What is the role of a white hat hacker?",
        "option_a": "Exploit systems for malicious purposes",
        "option_b": "Steal data and spread viruses",
        "option_c": "Test systems ethically for security holes",
        "option_d": "Spy on competitors",
        "answer": "c"
    },
    {
        "question_text": "In what situations should patching be prioritized?",
        "option_a": "Only after attacks",
        "option_b": "Never",
        "option_c": "As soon as patches are released",
        "option_d": "Every 6 months",
        "answer": "c"
    },
    {
        "question_text": "How can you reset a BIOS password?",
        "option_a": "Update antivirus software",
        "option_b": "Restart the system",
        "option_c": "Remove CMOS battery",
        "option_d": "Format the hard drive",
        "answer": "c"
    },
    {
        "question_text": "Which statement accurately defines a Man-in-the-Middle attack?",
        "option_a": "Hacker disrupts communication between client and server",
        "option_b": "Direct attack on firewall",
        "option_c": "Phishing email scam",
        "option_d": "Sending malware as attachments",
        "answer": "a"
    },
    {
        "question_text": "Which of the following is NOT an effective DDoS prevention method?",
        "option_a": "Load balancing",
        "option_b": "Using outdated firewalls",
        "option_c": "Anti-DDoS services",
        "option_d": "Configuring routers",
        "answer": "b"
    },
    {
        "question_text": "What is the primary purpose of an XSS attack?",
        "option_a": "Boosting website SEO",
        "option_b": "Injecting malicious scripts into websites",
        "option_c": "Encrypting user passwords",
        "option_d": "Authenticating remote users",
        "answer": "b"
    },
    {
        "question_text": "What function does the ARP protocol perform?",
        "option_a": "Mapping MAC address to IP address",
        "option_b": "Encrypting wireless traffic",
        "option_c": "Resetting DNS cache",
        "option_d": "Updating routing tables",
        "answer": "a"
    },
    {
        "question_text": "What is the function of port blocking in a LAN environment?",
        "option_a": "Allows all access to internal ports",
        "option_b": "Stops applications from using certain ports",
        "option_c": "Encrypts port data",
        "option_d": "Opens new firewall rules",
        "answer": "b"
    },
    {
        "question_text": "Which protocol operates at the Internet layer in the TCP/IP model?",
        "option_a": "FTP",
        "option_b": "TCP",
        "option_c": "IP",
        "option_d": "PPP",
        "answer": "c"
    },
    {
        "question_text": "What does the term 'botnet' refer to?",
        "option_a": "Malware that erases data",
        "option_b": "Group of bots used to automate cyberattacks",
        "option_c": "Antivirus software update tool",
        "option_d": "A Linux process monitor",
        "answer": "b"
    },
    {
        "question_text": "What purpose do salted hashes serve in cybersecurity?",
        "option_a": "To speed up encryption",
        "option_b": "To enable reversible encryption",
        "option_c": "To protect against dictionary and hash attacks",
        "option_d": "To log user activity",
        "answer": "c"
    },
    {
        "question_text": "How does TLS differ from SSL?",
        "option_a": "SSL is newer than TLS",
        "option_b": "TLS offers better security features than SSL",
        "option_c": "TLS is only used for FTP",
        "option_d": "SSL encrypts video only",
        "answer": "b"
    },
    {
        "question_text": "What does the term “data in transit” mean?",
        "option_a": "Stored data on local drive",
        "option_b": "Data being deleted",
        "option_c": "Data moving from one point to another",
        "option_d": "Archived files",
        "answer": "c"
    },
    {
        "question_text": "Which of the following best describes 2FA?",
        "option_a": "A backup server",
        "option_b": "Anti-virus software",
        "option_c": "Multi-layer authentication requiring extra verification step",
        "option_d": "Cloud storage method",
        "answer": "c"
    },
    {
        "question_text": "What does Cognitive Cybersecurity involve?",
        "option_a": "Manual security updates",
        "option_b": "Data mining and AI to simulate human threat detection",
        "option_c": "Keyboard encryption",
        "option_d": "File compression and backups",
        "answer": "b"
    },
    {
        "question_text": "Which of the following distinguishes VPN from VLAN?",
        "option_a": "Encrypting data in transit",
        "option_b": "Grouping workstations physically",
        "option_c": "Using MAC filtering",
        "option_d": "Allowing only wireless communication",
        "answer": "a"
    },
    {
        "question_text": "How would you define phishing in cybersecurity?",
        "option_a": "Encrypting passwords using hashes",
        "option_b": "Masking URLs for speed",
        "option_c": "Tricking users to disclose sensitive information",
        "option_d": "Optimizing server connections",
        "answer": "c"
    },
    {
        "question_text": "Which of the following helps prevent SQL Injection attacks?",
        "option_a": "Allowing direct SQL access",
        "option_b": "Using prepared statements and input validation",
        "option_c": "Sending raw queries from UI",
        "option_d": "Storing passwords in plain text",
        "answer": "b"
    }
]

class Command(BaseCommand):
    help = 'Import cybersecurity questions'

    def handle(self, *args, **kwargs):
        for q in QUESTIONS:
            Question.objects.create(
                question_text=q["question_text"],
                option_a=q["option_a"],
                option_b=q["option_b"],
                option_c=q["option_c"],
                option_d=q["option_d"],
                answer=q["answer"]
            )
        self.stdout.write(self.style.SUCCESS('All 40 questions imported!'))