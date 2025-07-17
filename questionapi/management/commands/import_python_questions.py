from django.core.management.base import BaseCommand
from questionapi.models import PythonQuestion

QUESTIONS = [
    {
        "question_id": "py_mcq_1",
        "question_text_full": "When would you use loop.run_in_executor() in an asyncio application?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "Python",
        "points": "10",
        "time": "3-00",
        "topic": "Asyncio",
        "options": [
            "To create a custom Future object for fine-grained control over asynchronous results.",
            "To schedule another coroutine to run concurrently on the same event loop.",
            "To run a CPU-bound or blocking I/O function in a separate thread or process pool, preventing it from blocking the event loop.",
            "To set a timeout for a long-running coroutine."
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "py_mcq_2",
        "question_text_full": "What is the primary role of the LOAD_FAST opcode in CPython bytecode?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Recall",
        "domain": "Python",
        "points": "10",
        "time": "3-00",
        "topic": "CPython Internals",
        "options": [
            "It loads a constant value, like a number or string, from the constants pool.",
            "It loads a global variable onto the value stack.",
            "It retrieves a local variable from the fast locals array and pushes it onto the value stack.",
            "It retrieves an attribute from an object."
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "py_mcq_3",
        "question_text_full": "What is the primary purpose of the weakref module in Python?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "Python",
        "points": "8",
        "time": "2-30",
        "topic": "Memory Management",
        "options": [
            "To create thread-safe references to objects.",
            "To serialize objects into a byte stream more efficiently than pickle.",
            "To create deeply nested copies of objects.",
            "To create references to objects that don't increase their reference count, allowing them to be garbage collected."
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "py_mcq_4",
        "question_text_full": "When using itertools.groupby(), what is a critical pre-condition for the function to group all identical consecutive items correctly?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "Python",
        "points": "8",
        "time": "2-30",
        "topic": "Itertools",
        "options": [
            "The input iterable must be sorted by the same key that is used for grouping.",
            "The key function must always return a string.",
            "The input iterable must not contain duplicate items.",
            "The input iterable must be a list."
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "py_mcq_5",
        "question_text_full": "In Python's typing module, what does typing.Protocol enable?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "Python",
        "points": "10",
        "time": "3-00",
        "topic": "Typing",
        "options": [
            "It defines a new data type that is distinct from its underlying base type at type-checking time.",
            "It enforces that a class must inherit from a specific base class.",
            "It is a decorator for creating asynchronous classes.",
            "It allows a class to implicitly satisfy a type hint by having the correct methods and attributes, without explicit inheritance."
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "py_mcq_6",
        "question_text_full": "Why is unpickling data from an untrusted source a major security vulnerability?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "Python",
        "points": "9",
        "time": "2-30",
        "topic": "Security",
        "options": [
            "It can cause denial-of-service by consuming excessive memory (a 'pickle bomb').",
            "It can corrupt the Python interpreter's memory, leading to a crash.",
            "It bypasses the Global Interpreter Lock (GIL), causing race conditions.",
            "It can execute arbitrary code, as the pickle format can contain instructions to import modules and call functions."
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "py_mcq_7",
        "question_text_full": "In a metaclass, what is the difference between the operations performed in __new__ versus __init__?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "Python",
        "points": "12",
        "time": "4-00",
        "topic": "Metaclasses",
        "options": [
            "__new__ handles class attributes, and __init__ handles instance attributes.",
            "There is no functional difference; they are interchangeable in metaclasses.",
            "__new__ is called before the class is created and __init__ is called after an instance of the class is created.",
            "__new__ constructs the class object and must return it, while __init__ receives the newly created class object to initialize it."
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "py_mcq_8",
        "question_text_full": "What happens if a class inherits from multiple base classes that each have a different, custom metaclass?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Recall",
        "domain": "Python",
        "points": "12",
        "time": "4-00",
        "topic": "Metaclasses",
        "options": [
            "The metaclass of the first base class in the inheritance list is used.",
            "Python automatically creates a new composite metaclass that inherits from all the base metaclasses.",
            "The class will have no metaclass and will default to type.",
            "It results in a TypeError because Python cannot determine a single, appropriate metaclass."
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "py_mcq_9",
        "question_text_full": "What is the primary advantage of using yield from instead of a direct for loop with yield?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "Python",
        "points": "9",
        "time": "3-00",
        "topic": "Generators",
        "options": [
            "It is the only way to yield items from a tuple.",
            "It provides a direct, two-way channel between the outermost caller and the innermost sub-generator, forwarding send() and throw() calls.",
            "It is purely syntactic sugar with no performance or functional difference.",
            "It consumes less memory than a standard for loop."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "py_mcq_10",
        "question_text_full": "What does the functools.singledispatch decorator enable?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "Python",
        "points": "9",
        "time": "3-00",
        "topic": "Functools",
        "options": [
            "It automatically converts all function arguments to a single, specified type.",
            "It allows a function to have different implementations based on the type of its first argument (generic functions).",
            "It ensures a function is only called once, similar to a singleton pattern.",
            "It dispatches function execution to a background thread pool."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "py_mcq_11",
        "question_text_full": "What problem does the Global Interpreter Lock (GIL) solve, despite its performance implications for multithreading?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "Python",
        "points": "10",
        "time": "3-30",
        "topic": "Concurrency",
        "options": [
            "It prevents race conditions when accessing database connections.",
            "It simplifies CPython's memory management by protecting it from concurrent access, making C extensions easier to write.",
            "It ensures that asynchronous code in asyncio runs in the correct order.",
            "It synchronizes file system operations across different processes."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "py_mcq_12",
        "question_text_full": "In typing, what is the difference between typing.NewType and a simple type alias (e.g., UserId = int)?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "Python",
        "points": "10",
        "time": "3-30",
        "topic": "Typing",
        "options": [
            "There is no difference; NewType is the deprecated syntax for a type alias.",
            "NewType can only be used for classes, whereas a type alias can be used for any type.",
            "NewType creates a distinct type that a static type checker treats as a unique subclass, preventing accidental mixing, while a type alias is interchangeable with the original type.",
            "NewType adds runtime type checking, while a type alias only works for static analysis."
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "py_mcq_13",
        "question_text_full": "What is a __slots__ conflict, and what happens when a base class has __slots__ and a derived class tries to define __dict__?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "Python",
        "points": "12",
        "time": "4-00",
        "topic": "Memory Management",
        "options": [
            "Instances of the derived class will not have a __dict__ unless '__dict__' is explicitly added to the derived class's __slots__ definition.",
            "The derived class __dict__ overrides the base class __slots__, and all instances will have a __dict__.",
            "If __dict__ is not added to the derived class's __slots__, a TypeError will be raised.",
            "The __slots__ from the base class are ignored in the derived class."
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "py_tough_1",
        "question_text_full": "You’re implementing a custom dictionary. What approach allows two separate keys to reflect the same internal value such that changing one key's value changes the other's?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "Python",
        "points": "20",
        "time": "15-00",
        "topic": "Python Internals",
        "options": [
            "Override __getitem__ and __setitem__ using a shared value map",
            "Use defaultdict with a lambda reference",
            "Use weak references in keys",
            "Use tuple keys as aliases"
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "py_tough_2",
        "question_text_full": "How can a class behave differently depending on the variable name it’s assigned to?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Extended Thinking",
        "domain": "Python",
        "points": "25",
        "time": "20-00",
        "topic": "Metaprogramming",
        "options": [
            "Override __init_subclass__",
            "Use a metaclass and override __call__",
            "Intercept assignment via sys._getframe() to determine LHS name",
            "Use __new__ to store variable names globally"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "py_tough_3",
        "question_text_full": "You want to make a decorator @reverse_time that makes output behave as if printed backward in time. What’s a possible trick?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "Python",
        "points": "18",
        "time": "12-00",
        "topic": "Decorators & IO",
        "options": [
            "Modify sys.stdout to buffer and replay in reverse",
            "Delay all prints by 1 second",
            "Use asyncio to reverse log output",
            "Monkeypatch built-in print globally"
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "py_tough_4",
        "question_text_full": "Which method best helps detect and resolve import name collisions due to local scope shadowing?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "Python",
        "points": "15",
        "time": "10-00",
        "topic": "Code Analysis",
        "options": [
            "Using dir() comparison",
            "AST parsing of the script and resolving symbol tables",
            "Analyzing globals() manually",
            "Dynamically overriding __import__"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "py_tough_5",
        "question_text_full": "How can a function change its own behavior on the second call without using a global counter?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Extended Thinking",
        "domain": "Python",
        "points": "22",
        "time": "18-00",
        "topic": "Metaprogramming",
        "options": [
            "Store state in a closure",
            "Modify its own __code__ object",
            "Override __call__ on the function",
            "Use a class with a counter attribute"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "py_tough_6",
        "question_text_full": "How can a function appear fine but raise a custom error on third use without using any counters?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Extended Thinking",
        "domain": "Python",
        "points": "25",
        "time": "20-00",
        "topic": "AST Manipulation",
        "options": [
            "Use a function decorator with nonlocal",
            "Use AST transformation to embed logic at definition time",
            "Raise error based on function name hash",
            "Use an internal list that exhausts after 3 pops"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "py_tough_7",
        "question_text_full": "What tool allows rewriting the source code after execution of a context manager?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "Python",
        "points": "20",
        "time": "15-00",
        "topic": "Code Analysis",
        "options": [
            "inspect.getsource() + ast.parse()",
            "tokenize + source file rewriting",
            "Monkeypatching __exit__ to open file and rewrite code",
            "All of the above"
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "py_tough_8",
        "question_text_full": "What’s the most memory-efficient way to implement deeply recursive generators?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "Python",
        "points": "22",
        "time": "18-00",
        "topic": "Generators",
        "options": [
            "Use recursion with yield from",
            "Use stack and loop manually",
            "Use trampoline-style generator dispatch",
            "Set recursion limit higher"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "py_tough_9",
        "question_text_full": "How can a Python object appear immutable but still track internal state?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "Python",
        "points": "18",
        "time": "12-00",
        "topic": "Data Model",
        "options": [
            "Override __getattr__, hide state in closures",
            "Use __slots__ to restrict attribute creation",
            "Store state in a hidden file",
            "Use metaclass to freeze __dict__"
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "py_tough_10",
        "question_text_full": "How could a function raise an error that can't be traced?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "Python",
        "points": "15",
        "time": "10-00",
        "topic": "Exception Handling",
        "options": [
            "Raise inside a compiled C extension",
            "Raise inside a thread and suppress traceback",
            "Use exception masking via contextlib",
            "Use sys.excepthook = lambda *args: None"
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "py_tough_11",
        "question_text_full": "How can a function change its behavior after 3 days without using system time?",
        "question_type": "Multiple Selection",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Extended Thinking",
        "domain": "Python",
        "points": "25",
        "time": "20-00",
        "topic": "Advanced Concepts",
        "options": [
            "Use hidden file access timestamps",
            "Use uuid entropy",
            "Store hash of system entropy over time",
            "Encode temporal behavior in function call patterns"
        ],
        "correct_answers": [1, 2, 3]
    },
    {
        "question_id": "py_tough_12",
        "question_text_full": "What techniques can enable hiding method names but still allow use via indirect access?",
        "question_type": "Multiple Selection",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "Python",
        "points": "22",
        "time": "18-00",
        "topic": "Metaprogramming",
        "options": [
            "Custom __getattr__ with natural language matching",
            "Using encrypted strings and a mapping",
            "Proxy object that maps keywords to method calls",
            "Decorator that exposes names via reflection"
        ],
        "correct_answers": [0, 1, 2]
    },
    {
        "question_id": "py_tough_13",
        "question_text_full": "How can a single object evaluate as both True and False depending on context?",
        "question_type": "Multiple Selection",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "Python",
        "points": "20",
        "time": "15-00",
        "topic": "Data Model",
        "options": [
            "Override __bool__ with conditional logic",
            "Return different values based on stack inspection",
            "Implement both __bool__ and __len__ with conflicting logic",
            "Use a random generator in __bool__"
        ],
        "correct_answers": [0, 1, 2]
    },
    {
        "question_id": "py_tough_14",
        "question_text_full": "What techniques allow implicit state preservation across a stateless pipeline?",
        "question_type": "Multiple Selection",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Extended Thinking",
        "domain": "Python",
        "points": "22",
        "time": "18-00",
        "topic": "Advanced Design",
        "options": [
            "Closures with mutable default args",
            "Thread-local storage",
            "Monkeypatching built-in operators",
            "Descriptors tied to call chains"
        ],
        "correct_answers": [0, 1, 3]
    },
    {
        "question_id": "py_tough_15",
        "question_text_full": "Which methods could be used to hijack another function's return value without modifying it directly?",
        "question_type": "Multiple Selection",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Extended Thinking",
        "domain": "Python",
        "points": "25",
        "time": "20-00",
        "topic": "Metaprogramming",
        "options": [
            "sys.settrace to intercept return values",
            "Proxy the function via a wrapper class",
            "Overwrite built-in return keyword",
            "Manipulate bytecode to rewire return"
        ],
        "correct_answers": [0, 1, 3]
    }
]


class Command(BaseCommand):
    help = 'Import Python Questions'

    def handle(self, *args, **kwargs):
        for q in QUESTIONS:
            PythonQuestion.objects.update_or_create(
                question_id=q["question_id"],
                defaults=q
            )
        self.stdout.write(self.style.SUCCESS('Python questions imported!'))