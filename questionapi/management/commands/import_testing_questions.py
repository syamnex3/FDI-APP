from django.core.management.base import BaseCommand
from questionapi.models import TestingQuestion

QUESTIONS = [
    {
        "question_id": "st_beg_1",
        "question_text_full": "Which fundamental testing principle asserts that successful test execution can only identify defects under the specific conditions tested and cannot guarantee their complete absence?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Testing Principles",
        "points": "5",
        "time": "0-45",
        "topic": "Testing Principles",
        "options": [
            "Exhaustive testing is unattainable",
            "Defect clustering",
            "Testing demonstrates the presence of defects, not their absence",
            "Testing is influenced by context"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "st_beg_2",
        "question_text_full": "Which testing principle supports the application of test design techniques to select a manageable subset of test cases rather than evaluating every possible input combination?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Testing Principles",
        "points": "5",
        "time": "0-45",
        "topic": "Testing Principles",
        "options": [
            "Early testing saves time and money",
            "Exhaustive testing is infeasible",
            "Absence-of-errors fallacy",
            "Defects tend to cluster together"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "st_beg_3",
        "question_text_full": "Which fundamental testing principle illustrates a situation where software is technically free of defects but fails to meet the user's business needs or requirements?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Testing Principles",
        "points": "5",
        "time": "0-45",
        "topic": "Testing Principles",
        "options": [
            "Pesticide Paradox",
            "Defect Clustering",
            "Absence-of-Errors Fallacy",
            "Testing Is Context-Dependent"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "st_beg_4",
        "question_text_full": "What differentiates the primary objective of User Acceptance Testing (UAT) from System Testing?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Test Levels",
        "points": "7",
        "time": "1-00",
        "topic": "UAT, System Testing",
        "options": [
            "System Testing is performed by developers, while UAT is conducted by end-users or testers",
            "System Testing verifies that the system meets its specifications, whereas UAT assesses the system's fitness for its intended business purpose",
            "System Testing utilizes black-box testing methods, in contrast to UAT, which employs white-box methods",
            "System Testing focuses on evaluating non-functional requirements, while UAT primarily examines functional requirements"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "st_beg_5",
        "question_text_full": "What is the primary objective of integration testing when performed on a system composed of multiple independently developed modules or services?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Test Levels",
        "points": "7",
        "time": "1-00",
        "topic": "Integration Testing",
        "options": [
            "To evaluate each module individually, ensuring its correct functionality in isolation",
            "To confirm that the complete application meets business requirements from a holistic perspective",
            "To examine the interfaces and data exchange between the integrated modules, with the aim of identifying interaction errors",
            "To enable end-users to assess whether the combined services adequately meet their needs"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "st_beg_6",
        "question_text_full": "How are tests that verify specific software actions (e.g., user login) classified differently from tests that measure system attributes (e.g., performance under load)?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Test Types",
        "points": "7",
        "time": "1-00",
        "topic": "Functional vs Non-Functional Testing",
        "options": [
            "Action-based tests are classified as functional, while attribute-based tests are categorized as non-functional",
            "Action-based tests fall under system testing, whereas attribute-based tests are classified as integration testing",
            "Action-based tests are identified as white-box tests, while attribute-based tests are regarded as black-box tests",
            "Action-based tests are designated as regression tests, and attribute-based tests are recognized as usability tests"
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "st_beg_7",
        "question_text_full": "Which of the following best describes a \"defect\" according to the standard ISTQB definition?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "Defect Management",
        "points": "5",
        "time": "0-45",
        "topic": "Defect Definition",
        "options": [
            "An error introduced by a developer due to misunderstanding a requirement",
            "An unexpected event that leads to a software crash in the live environment",
            "An issue or fault in a software component that may prevent it from fulfilling its intended function",
            "A user’s personal view that a feature lacks usability"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "st_beg_8",
        "question_text_full": "Which of the following activities best demonstrates the \"Early Testing\" principle in the Software Development Life Cycle (SDLC)?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Application",
        "domain": "Testing Principles",
        "points": "7",
        "time": "1-00",
        "topic": "Early Testing",
        "options": [
            "Conducting detailed regression tests right before a product release",
            "Reviewing requirements and design documents to identify issues before development starts",
            "Implementing automation during system testing to accelerate test execution",
            "Postponing test planning until after the development phase is complete"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "st_beg_9",
        "question_text_full": "When applying the \"Defect Clustering\" principle, which testing strategy is most effective under time and resource constraints?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Application",
        "domain": "Testing Principles",
        "points": "7",
        "time": "1-00",
        "topic": "Defect Clustering",
        "options": [
            "Randomly testing various components to achieve wide functional coverage",
            "Prioritizing testing on modules with a history of high defect density",
            "Limiting testing to new features since existing ones have already been validated",
            "Allocating equal testing effort to all parts of the application for fairness"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "st_beg_10",
        "question_text_full": "In software testing, what does the \"Pesticide Paradox\" refer to?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Testing Principles",
        "points": "5",
        "time": "0-45",
        "topic": "Pesticide Paradox",
        "options": [
            "Fixing one defect results in the introduction of a more critical defect",
            "Repeated use of the same test cases leads to reduced effectiveness in uncovering new defects",
            "Assuming a defect-free system is ready for release, even if user expectations aren't met",
            "Tailoring the testing process to align with the unique context of the software"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "st_int_11",
        "question_text_full": "Which of the following input sets best applies the Equivalence Partitioning technique for testing a 2-character alphabetic field accepting valid ISO country codes?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "Test Design Techniques",
        "points": "10",
        "time": "1-30",
        "topic": "Equivalence Partitioning",
        "options": [
            "A valid input (\"FR\"), an invalid 2-letter code (\"XX\"), a string with a number (\"A1\"), a too-long string (\"USA\"), and an empty string",
            "Ten valid country codes (\"US\", \"GB\", \"CA\", etc.) to ensure a wide range of coverage",
            "One valid code (\"JP\") and one invalid code with incorrect length (\"USA\")",
            "Inputs in various cases: lowercase (\"de\"), uppercase (\"DE\"), and mixed case (\"De\")"
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "st_int_12",
        "question_text_full": "Using two-point Boundary Value Analysis for a numeric input field with a valid range of $10.00 to $100.00 (inclusive), which set of test values best targets the boundary conditions?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "Test Design Techniques",
        "points": "10",
        "time": "1-30",
        "topic": "Boundary Value Analysis",
        "options": [
            "$10.00, $50.00, $100.00",
            "$9.99, $10.00, $100.00, $100.01",
            "$0.00, $10.00, $100.00, $101.00",
            "$9.99, $10.01, $99.99, $100.01"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "st_int_13",
        "question_text_full": "In decision table testing, how many rules are needed to cover all possible combinations of three independent binary (True/False) conditions that influence a single outcome?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "Test Design Techniques",
        "points": "10",
        "time": "1-00",
        "topic": "Decision Table Testing",
        "options": [
            "3",
            "6",
            "8",
            "9"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "st_int_14",
        "question_text_full": "In the context of State Transition Testing, which of the following transitions should be identified as invalid and verified to be blocked, given that an order can only be cancelled from the 'Pending' or 'Confirmed' states?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "Test Design Techniques",
        "points": "10",
        "time": "1-30",
        "topic": "State Transition Testing",
        "options": [
            "Transition from Pending to Confirmed",
            "Transition from Confirmed to Cancelled",
            "Transition from Preparing to Out for Delivery",
            "Transition from Preparing to Cancelled"
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "st_int_15",
        "question_text_full": "Which of the following sequences correctly represents the standard progression of a defect from the time it is reported by a tester to the point where it is ready for re-testing?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Recall",
        "domain": "Defect Management",
        "points": "8",
        "time": "0-45",
        "topic": "Defect Life Cycle",
        "options": [
            "New → Open → Assigned → Fixed",
            "New → Assigned → Open → In Progress",
            "New → Assigned → Open → Fixed",
            "New → In Triage → In Development → Resolved"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "st_int_16",
        "question_text_full": "What is the main objective of a bug triage meeting during the software development process?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Defect Management",
        "points": "8",
        "time": "1-00",
        "topic": "Bug Triage",
        "options": [
            "To instantly assign the bug to the developer best suited to fix it",
            "To collectively evaluate the bug’s severity and priority to decide if and when it should be addressed",
            "To create a detailed technical plan for resolving the bug",
            "To determine which developer is responsible for introducing the defect"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "st_int_17",
        "question_text_full": "Which black-box test design technique is best suited for systematically validating a feature that involves a complex set of business rules with multiple interdependent conditions?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "Test Design Techniques",
        "points": "10",
        "time": "1-30",
        "topic": "Black-box Testing",
        "options": [
            "State Transition Testing",
            "Boundary Value Analysis",
            "Equivalence Partitioning",
            "Decision Table Testing"
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "st_int_18",
        "question_text_full": "After identifying valid and invalid partitions using Equivalence Partitioning, what is the most appropriate next step when applying Boundary Value Analysis (BVA)?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "Test Design Techniques",
        "points": "10",
        "time": "1-30",
        "topic": "Equivalence Partitioning, BVA",
        "options": [
            "Select one random value from each partition",
            "Create test cases that target the boundary values at and just outside the partition limits",
            "Test several values from the middle of the valid input range",
            "Consult a developer to understand the internal validation logic"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "st_int_19",
        "question_text_full": "In the context of State Transition Testing, what do the terms \"event\" and \"action\" refer to?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Test Design Techniques",
        "points": "8",
        "time": "1-00",
        "topic": "State Transition Testing",
        "options": [
            "Event: The current state of the system; Action: The next state of the system",
            "Event: A user's opinion of the system; Action: The system's performance",
            "Event: A trigger that initiates a state change; Action: The system's response to that change",
            "Event: A system failure; Action: Filing a bug report"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "st_int_20",
        "question_text_full": "In defect management, how is Severity different from Priority?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Defect Management",
        "points": "8",
        "time": "1-00",
        "topic": "Severity vs Priority",
        "options": [
            "Severity defines how urgently a defect should be fixed, while Priority reflects how much it affects the system",
            "Severity measures the impact of the defect on system functionality; Priority indicates how urgently it should be addressed based on business need",
            "Severity is assigned by testers; Priority is assigned by developers",
            "Severity and Priority are synonymous and used interchangeably"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "st_adv_21",
        "question_text_full": "When testing a system feature that includes a numeric input range, a categorical input, and a state-based input—all contributing to outcomes based on complex business rules—which test design strategy provides the most thorough coverage?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "Test Design Strategy",
        "points": "15",
        "time": "2-00",
        "topic": "Combined Test Techniques",
        "options": [
            "Rely solely on Exploratory Testing to explore various combinations freely",
            "Apply Equivalence Partitioning and Boundary Value Analysis for the numeric input and use a Decision Table to cover rule combinations involving the categorical and state-based inputs",
            "Use only State Transition Testing to represent the state-based behavior",
            "Use Boundary Value Analysis for the numeric input and manually test every combination of other inputs"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "st_adv_22",
        "question_text_full": "What is the most notable change in a tester’s role when transitioning from a traditional Waterfall model to an Agile development environment?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Agile Testing",
        "points": "12",
        "time": "1-30",
        "topic": "Agile Role",
        "options": [
            "Moving from approving final requirements to creating fixed test plans for each sprint",
            "Shifting from starting tests after coding ends to signing off user stories",
            "Transitioning from acting as a final-phase quality gatekeeper to becoming a continuous, collaborative quality advocate throughout the process",
            "Changing focus from manual testing to working solely on test automation"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "st_adv_23",
        "question_text_full": "Which statement best differentiates between a lightweight and a formal Risk-Based Testing (RBT) approach?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Risk-Based Testing",
        "points": "12",
        "time": "1-30",
        "topic": "RBT Approaches",
        "options": [
            "Lightweight RBT considers only the business impact, while formal RBT assesses both impact and probability of failure",
            "Lightweight RBT uses informal expert opinions and qualitative judgment, while formal RBT involves structured techniques like FMEA and comprehensive documentation",
            "Lightweight RBT is strictly for Agile environments, whereas formal RBT is limited to Waterfall projects",
            "Lightweight RBT occurs after test execution, while formal RBT is conducted during the planning phase"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "st_adv_24",
        "question_text_full": "Which combination of usability testing methods provides both quantitative data on user navigation paths and qualitative insights into users’ reasoning behind their actions?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Application",
        "domain": "Usability Testing",
        "points": "12",
        "time": "1-30",
        "topic": "Usability Methods",
        "options": [
            "A/B Testing and Guerrilla Testing",
            "Clickstream Analysis and Think-Aloud Protocol",
            "Eye Tracking and A/B Testing",
            "Moderated Testing and Unmoderated Testing"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "st_adv_25",
        "question_text_full": "Which test estimation technique is most appropriate for a new project characterized by uncertainty, unclear requirements, and a lack of historical data—where expert consensus is the primary input?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "Test Estimation",
        "points": "12",
        "time": "1-30",
        "topic": "Estimation Techniques",
        "options": [
            "Function Point Analysis (FPA)",
            "Test Point Analysis (TPA)",
            "Wideband Delphi",
            "Percentage Distribution"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "st_adv_26",
        "question_text_full": "In software quality terminology, what is the correct cause-and-effect relationship among Error, Defect, and Failure?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Quality Terminology",
        "points": "10",
        "time": "1-00",
        "topic": "Error, Defect, Failure",
        "options": [
            "A Defect in the code causes a human Error, which leads to a system Failure",
            "A human Error leads to a Defect in the software, which, when executed, may result in a Failure",
            "A system Failure causes a Defect in the code, which is the result of a human Error",
            "Error, Defect, and Failure are unrelated and occur independently"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "st_adv_27",
        "question_text_full": "If an application's core functionality behaves correctly across all browsers but the user interface layout appears broken specifically in one browser (e.g., Safari), what is the most likely cause?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Analysis",
        "domain": "Cross-Browser Testing",
        "points": "12",
        "time": "1-30",
        "topic": "Browser Compatibility",
        "options": [
            "A critical JavaScript error affecting only Safari",
            "A server-side logic issue in the application’s backend",
            "A network connectivity problem isolated to the Safari browser",
            "A CSS property or value that is unsupported or rendered differently by Safari’s rendering engine"
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "st_adv_28",
        "question_text_full": "Which of the following are non-linguistic defects that should be detected during localization testing for a German market? (Select all that apply)",
        "question_type": "Multiple Selection",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Application",
        "domain": "Localization Testing",
        "points": "15",
        "time": "1-45",
        "topic": "Localization Defects",
        "options": [
            "Displaying the date format as MM/DD/YYYY",
            "Showing prices in US Dollars ($) instead of Euros (€)",
            "Using a blue color scheme that a tester finds unappealing",
            "Listing product dimensions in inches instead of centimeters",
            "Using a grammatically correct but unnatural-sounding translation for a button"
        ],
        "correct_answers": [0, 1, 3]
    },
    {
        "question_id": "st_adv_29",
        "question_text_full": "A reported bug describes behavior that conflicts with the tester’s expectations but actually aligns with the product’s intended (though undocumented) design. What is the most appropriate resolution for this bug?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "Defect Management",
        "points": "10",
        "time": "1-00",
        "topic": "Defect Resolution",
        "options": [
            "Fixed",
            "Deferred",
            "Duplicate",
            "Rejected (or As Designed)"
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "st_adv_30",
        "question_text_full": "An Agile team has an 8-hour automated regression suite but must support a 15-minute CI/CD feedback loop. What is the most effective long-term strategy?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "Agile Testing",
        "points": "15",
        "time": "2-00",
        "topic": "CI/CD & Automation",
        "options": [
            "Run the full 8-hour regression suite overnight and review results the next day",
            "Manually run only the most critical test cases during each 15-minute interval",
            "Use a risk-based approach to develop a targeted smoke test suite for fast CI/CD feedback, while running the full suite periodically",
            "Retire the automated suite and rely solely on exploratory testing"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "st_adv_31",
        "question_text_full": "What is the primary purpose of exploratory testing within an Agile sprint?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Agile Testing",
        "points": "10",
        "time": "1-00",
        "topic": "Exploratory Testing",
        "options": [
            "To replace the need for automated regression testing",
            "To verify that the pre-scripted test cases are correct",
            "To discover defects and edge cases not anticipated in formal requirements or scripted tests by leveraging tester creativity and intuition",
            "To provide a formal report of test coverage to stakeholders"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "st_adv_32",
        "question_text_full": "Which end-of-cycle test metric provides the strongest direct indication that the software may not be ready for release?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Analysis",
        "domain": "Test Metrics",
        "points": "12",
        "time": "1-30",
        "topic": "Release Readiness",
        "options": [
            "The number of unexecuted test cases",
            "The amount of test environment downtime",
            "The test case pass rate",
            "The number of open critical defects"
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "st_adv_33",
        "question_text_full": "In risk identification, which of the following is a functional product risk rather than a project or process risk?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Risk Management",
        "points": "10",
        "time": "1-00",
        "topic": "Product vs Project Risk",
        "options": [
            "The lead developer might leave the project",
            "The testing budget might be cut",
            "An incorrect interest calculation could cause users to be overcharged",
            "The new testing methodology might not be adopted correctly"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "st_adv_34",
        "question_text_full": "Test Point Analysis (TPA) and its variants primarily derive effort estimates based on which factor?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Test Estimation",
        "points": "12",
        "time": "1-30",
        "topic": "TPA",
        "options": [
            "The number of lines of code in the application",
            "The number and complexity of the test cases required",
            "The number of developers on the project team",
            "The number of pages in the requirements specification document"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "st_adv_35",
        "question_text_full": "What is the primary characteristic of \"robust\" boundary value testing that distinguishes it from standard Boundary Value Analysis (BVA)?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Test Design Techniques",
        "points": "12",
        "time": "1-30",
        "topic": "Robust BVA",
        "options": [
            "It tests values further away from the boundaries",
            "It combines boundary value testing with equivalence partitioning for different data types or classes at the boundaries",
            "It requires testing every value within the valid range",
            "It is only performed by senior testers"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "st_adv_36",
        "question_text_full": "In a decision table, if two rules have identical actions and differ by only one condition, what optimization can be applied?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "Test Design Techniques",
        "points": "10",
        "time": "1-00",
        "topic": "Decision Table Optimization",
        "options": [
            "The two rules can be collapsed into a single rule using a \"don't care\" (–) entry for the differing condition",
            "One of the rules must be deleted as it is redundant",
            "A new action must be created to handle this specific case",
            "The conditions must be reordered to prevent this from happening"
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "st_adv_37",
        "question_text_full": "What is the most significant mindset shift for a tester moving from a Waterfall to an Agile model?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Agile Testing",
        "points": "12",
        "time": "1-30",
        "topic": "Agile Mindset",
        "options": [
            "Shifting focus from writing bug reports to writing automated test scripts",
            "Shifting from being a \"quality gate\" at the end of the process to being a \"quality coach\" embedded throughout the process",
            "Shifting from testing the UI to testing the API",
            "Shifting from a fixed schedule to a more flexible schedule"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "st_adv_38",
        "question_text_full": "Scenario: A critical defect was discovered in the production environment. The issue only occurs under low-memory conditions, which were not emulated in the high-performance test environment during testing.\nThis situation highlights a gap in which area of test management?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Analysis",
        "domain": "Test Management",
        "points": "12",
        "time": "1-45",
        "topic": "Test Environment",
        "options": [
            "Test Case Design",
            "Defect Reporting",
            "Test Environment Provisioning and Management",
            "Test Team Skill and Training"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "st_adv_39",
        "question_text_full": "Which of the following task instructions is the most neutral and user-focused, avoiding bias while evaluating usability during a test?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Application",
        "domain": "Usability Testing",
        "points": "10",
        "time": "1-15",
        "topic": "Usability Task Design",
        "options": [
            "Test the fund transfer feature by entering an amount and clicking 'Submit’",
            "We've made the transfer process simple. Show us how you would send $50 to John",
            "You owe your friend Sarah $25 for lunch. Using the app, send her the money",
            "First, find the 'Transfer' button. Then, select a recipient. After that, enter $100 and confirm"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "st_adv_40",
        "question_text_full": "At which levels of software testing could a defect caused by an integer overflow in a specific function potentially be detected? (Select all that apply)",
        "question_type": "Multiple Selection",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "Test Levels",
        "points": "15",
        "time": "1-45",
        "topic": "Defect Detection",
        "options": [
            "Unit Testing",
            "Integration Testing",
            "System Testing",
            "Usability Testing"
        ],
        "correct_answers": [0, 1, 2]
    }
]

class Command(BaseCommand):
    help = 'Import Testing Questions'

    def handle(self, *args, **kwargs):
        for q in QUESTIONS:
            TestingQuestion.objects.update_or_create(
                question_id=q["question_id"],
                defaults=q
            )
        self.stdout.write(self.style.SUCCESS('Testing questions imported!'))