from django.core.management.base import BaseCommand
from questionapi.models import JavaScriptQuestion

QUESTIONS = [
    {
        "question_id": "js_mcq_1",
        "question_text_full": "In JavaScript, which option is used to invoke a function defined using an expression?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "JavaScript",
        "points": "10",
        "time": "1-00",
        "topic": "Functions",
        "options": [
            "Function literal",
            "Function prototype",
            "Function declaration",
            "Function calling"
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "js_mcq_2",
        "question_text_full": "The phrase “that can appear legally on the left-hand side of an assignment” typically describes variables, array elements, and object properties. These are collectively referred to as __________:",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "JavaScript",
        "points": "10",
        "time": "1-00",
        "topic": "Variables & Expressions",
        "options": [
            "Prototypes",
            "Properties",
            "Lvalue",
            "Definition"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "js_mcq_3",
        "question_text_full": "Which of the following symbols is used to write single-line comments in JavaScript?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "JavaScript",
        "points": "5",
        "time": "0-30",
        "topic": "Syntax",
        "options": [
            "//",
            "\\",
            "* */",
            "* *\\"
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "js_mcq_4",
        "question_text_full": "In JavaScript, which of the following is used to invoke or call a function or method?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "JavaScript",
        "points": "8",
        "time": "0-45",
        "topic": "Functions",
        "options": [
            "Functional Expression",
            "Property Access Expression",
            "Primary Expression",
            "Invocation Expression"
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "js_mcq_5",
        "question_text_full": "The execution of a function halts when the program encounters which of the following statements within its body?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "JavaScript",
        "points": "5",
        "time": "0-30",
        "topic": "Control Flow",
        "options": [
            "goto statement",
            "break statement",
            "continue statement",
            "return statement"
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "js_mcq_6",
        "question_text_full": "What will be the output in the console when the following code is executed?\nconsole.log(1 < 2 < 3); \nconsole.log(3 > 2 > 1);",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Application",
        "domain": "JavaScript",
        "points": "12",
        "time": "1-30",
        "topic": "Operators & Type Coercion",
        "options": [
            "true, true",
            "true, false",
            "false, true",
            "false, false"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "js_mcq_7",
        "question_text_full": "What output will be displayed in the console when the following JavaScript code is executed?\nlet x = 10; \nlet y = (x++, x + 1, x * 2); \nconsole.log(y);",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Application",
        "domain": "JavaScript",
        "points": "12",
        "time": "1-30",
        "topic": "Operators & Expressions",
        "options": [
            "22",
            "12",
            "21",
            "20"
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "js_mcq_8",
        "question_text_full": "Which of the following values are treated as falsy in JavaScript?",
        "question_type": "Multiple Selection",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "JavaScript",
        "points": "10",
        "time": "1-00",
        "topic": "Truthiness & Falsiness",
        "options": [
            "The boolean value false",
            "The numeric value 0",
            "An empty string ''",
            "The value undefined"
        ],
        "correct_answers": [0, 1, 2, 3]
    },
    {
        "question_id": "js_mcq_9",
        "question_text_full": "Which of the following options are valid methods for creating an object in JavaScript?",
        "question_type": "Multiple Selection",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "JavaScript",
        "points": "10",
        "time": "1-00",
        "topic": "Objects",
        "options": [
            "var obj = new Object();",
            "var obj = {};",
            "var obj = Object.create(null);",
            "var obj = object();"
        ],
        "correct_answers": [0, 1, 2]
    },
    {
        "question_id": "js_mcq_10",
        "question_text_full": "Which of the following JavaScript methods can be used to iterate over elements in an array?",
        "question_type": "Multiple Selection",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "JavaScript",
        "points": "8",
        "time": "0-45",
        "topic": "Arrays",
        "options": [
            "forEach()",
            "map()",
            "filter()",
            "reduce()"
        ],
        "correct_answers": [0, 1, 2, 3]
    },
    {
        "question_id": "js_mcq_11",
        "question_text_full": "Which of the following statements about == and === in JavaScript are correct?",
        "question_type": "Multiple Selection",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "JavaScript",
        "points": "10",
        "time": "1-00",
        "topic": "Equality",
        "options": [
            "=== compares both value and data type",
            "== performs type coercion before making a comparison",
            "=== is slower than ==",
            "== represents strict equality"
        ],
        "correct_answers": [0, 1]
    },
    {
        "question_id": "js_mcq_12",
        "question_text_full": "Which of the following are valid keywords for declaring variables in JavaScript?",
        "question_type": "Multiple Selection",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "JavaScript",
        "points": "7",
        "time": "0-30",
        "topic": "Variables",
        "options": [
            "var",
            "let",
            "const",
            "define"
        ],
        "correct_answers": [0, 1, 2]
    },
    {
        "question_id": "js_mcq_13",
        "question_text_full": "Which of the following methods modify (mutate) the original array in JavaScript?",
        "question_type": "Multiple Selection",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "JavaScript",
        "points": "10",
        "time": "1-00",
        "topic": "Arrays",
        "options": [
            "push()",
            "pop()",
            "slice()",
            "splice()"
        ],
        "correct_answers": [0, 1, 3]
    },
    {
        "question_id": "js_mcq_14",
        "question_text_full": "Which of the following statements accurately describe the behavior of arrow functions in JavaScript?",
        "question_type": "Multiple Selection",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "JavaScript",
        "points": "12",
        "time": "1-30",
        "topic": "Functions & 'this'",
        "options": [
            "Arrow functions have their own this binding",
            "Arrow functions do not bind this",
            "Arrow functions cannot be used as constructors",
            "Arrow functions have access to the arguments object"
        ],
        "correct_answers": [1, 2]
    },
    {
        "question_id": "js_mcq_15",
        "question_text_full": "What will be printed to the console when the following code is executed?\nlet a = [1, 2, 3]; \nlet b = a; \nb.push(4); \nconsole.log(a); \nconsole.log(b);",
        "question_type": "Multiple Selection",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "JavaScript",
        "points": "10",
        "time": "1-00",
        "topic": "Arrays & References",
        "options": [
            "[1, 2, 3]",
            "[1, 2, 3, 4]",
            "Error",
            "Both a and b output the same array"
        ],
        "correct_answers": [1, 3]
    },
    {
        "question_id": "js_mcq_16",
        "question_text_full": "Which of the following functions or features in JavaScript operate asynchronously?",
        "question_type": "Multiple Selection",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "JavaScript",
        "points": "10",
        "time": "1-00",
        "topic": "Asynchronous JavaScript",
        "options": [
            "setTimeout()",
            "fetch()",
            "console.log()",
            "Promise"
        ],
        "correct_answers": [0, 1, 3]
    },
    {
        "question_id": "js_mcq_17",
        "question_text_full": "Which of the following statements can cause a JavaScript function to terminate execution before reaching its end?",
        "question_type": "Multiple Selection",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "JavaScript",
        "points": "7",
        "time": "0-45",
        "topic": "Control Flow",
        "options": [
            "break",
            "continue",
            "return",
            "throw"
        ],
        "correct_answers": [2, 3]
    },
    {
        "question_id": "js_mcq_18",
        "question_text_full": "Which of the following are considered valid values in a JSON structure?",
        "question_type": "Multiple Selection",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "JavaScript",
        "points": "10",
        "time": "1-00",
        "topic": "JSON",
        "options": [
            "true",
            "undefined",
            "\"string\"",
            "{}"
        ],
        "correct_answers": [0, 2, 3]
    },
    {
        "question_id": "js_mcq_19",
        "question_text_full": "Which of the following statements accurately describe the behavior and characteristics of closures in JavaScript?",
        "question_type": "Multiple Selection",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "JavaScript",
        "points": "12",
        "time": "1-30",
        "topic": "Closures",
        "options": [
            "Closures can access variables from their outer (enclosing) functions.",
            "Closures are created exclusively by arrow functions.",
            "Closures can be used to encapsulate and protect data.",
            "Closures only work when defined in the global scope."
        ],
        "correct_answers": [0, 2]
    }
]

class Command(BaseCommand):
    help = 'Import JavaScript Questions'

    def handle(self, *args, **kwargs):
        for q in QUESTIONS:
            JavaScriptQuestion.objects.update_or_create(
                question_id=q["question_id"],
                defaults=q
            )
        self.stdout.write(self.style.SUCCESS('JavaScript questions imported!'))