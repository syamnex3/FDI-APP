import json
from django.core.management.base import BaseCommand
from questionapi.models import JavaQuestion
QUESTIONS =[
    {
        "question_id": "java_mcq_1",
        "question_text_full": "Consider a custom `Employee` class with `equals()` and `hashCode()` implemented solely based on the `employeeId` field. If you create a `HashMap<Employee, String>` and add multiple `Employee` objects with the same `employeeId` but different names, what will be the final state of the map?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "Java",
        "points": "15",
        "time": "5-00",
        "topic": "Collections",
        "options": [
            "The map will contain all Employee objects, as they are distinct instances.",
            "Only the first Employee object added for that `employeeId` will be stored.",
            "The map will store only the last Employee object added for that `employeeId`, overwriting previous ones.",
            "A `java.util.ConcurrentModificationException` will be thrown."
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "java_msq_2",
        "question_text_full": "Which of the following statements about Java's Stream API are true?\n\nList<String> list = Arrays.asList(\"a\", \"b\", \"c\");\nString result = list.stream().parallel().reduce(\"\", (s1, s2) -> s1 + s2);",
        "question_type": "Multiple Selection",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "Java",
        "points": "18",
        "time": "7-00",
        "topic": "Lambda & Streams",
        "options": [
            "The result is guaranteed to be 'abc'.",
            "The use of string concatenation in a parallel stream's reducer is highly inefficient.",
            "The identity element `\"\"` ensures the result is predictable regardless of thread execution order.",
            "The result is not guaranteed to be 'abc' due to the non-associative nature of string concatenation in this parallel context."
        ],
        "correct_answers": [1, 3]
    },
    {
        "question_id": "java_pseudo_1",
        "question_text_full": "Analyze the following pseudo-code which aims to find the kth smallest element in an unsorted array. What is the primary issue with this approach in terms of performance and correctness?\n\nfunction findKthSmallest(array, k):\n  // Sort the array in ascending order\n  sort(array)\n  \n  // Return the element at the k-1 index\n  return array[k-1]",
        "question_type": "Pseudo Code",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Extended Thinking",
        "domain": "Java",
        "points": "12",
        "time": "6-00",
        "topic": "Algorithms",
        "options": [
            "It's inefficient because sorting the entire array (O(n log n)) is unnecessary; a selection algorithm like Quickselect could do it in O(n) on average.",
            "It will fail if the array contains duplicate elements.",
            "The index should be `array[k]` instead of `array[k-1]`.",
            "It correctly finds the element but modifies the original input array, which might be an undesirable side effect."
        ],
        "correct_answers": [0, 3]
    },
    {
        "question_id": "java_mcq_3",
        "question_text_full": "When using `CopyOnWriteArrayList`, which statement is most accurate regarding its iterator?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "Java",
        "points": "14",
        "time": "5-00",
        "topic": "Concurrency",
        "options": [
            "The iterator will throw a `ConcurrentModificationException` if the list is modified after the iterator is created.",
            "The iterator reflects a snapshot of the list at the time the iterator was created and will not see subsequent modifications.",
            "The iterator's `remove()` method is fully supported and thread-safe.",
            "The iterator provides a real-time view of the list, immediately reflecting any additions or removals from other threads."
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "java_coding_1",
        "question_text_full": "What is the output of the following Java code?\n\nimport java.util.stream.IntStream;\n\npublic class Test {\n    public static void main(String[] args) {\n        int[] count = {0};\n        IntStream.range(0, 5).forEach(i -> {\n            count[0]++;\n        });\n        System.out.println(count[0]);\n    }\n}",
        "question_type": "Coding",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "Java",
        "points": "12",
        "time": "4-00",
        "topic": "Lambda & Streams",
        "options": [
            "The code will not compile.",
            "It prints 0.",
            "It prints 5.",
            "It throws an `ArrayIndexOutOfBoundsException`."
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "java_mcq_4",
        "question_text_full": "Given the following method signature, which of the provided method calls is INVALID inside the method body?\n\npublic void processElements(List<? extends Number> list) {\n    // method body\n}",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Extended Thinking",
        "domain": "Java",
        "points": "16",
        "time": "6-00",
        "topic": "Generics",
        "options": [
            "processElements(new ArrayList<Integer>()); // External call",
            "list.add(Integer.valueOf(5)); // Inside the method",
            "Number n = list.get(0); // Inside the method",
            "list.add(null); // Inside the method"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "java_msq_5",
        "question_text_full": "Consider the following CompletableFuture chain. Which statements are true?\n\nCompletableFuture<String> future = CompletableFuture.supplyAsync(() -> \"Hello\")\n    .thenApply(s -> s + \" World\")\n    .thenApply(s -> s + \"!\");\n",
        "question_type": "Multiple Selection",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "Java",
        "points": "18",
        "time": "8-00",
        "topic": "Concurrency",
        "options": [
            "`supplyAsync` executes the task in a separate thread from the common ForkJoinPool (by default).",
            "`thenApply` executes synchronously in the same thread if the previous stage is already complete.",
            "If the first stage throws an exception, `future.get()` will block forever.",
            "`thenCompose` would be more appropriate if the second stage returned another `CompletableFuture`."
        ],
        "correct_answers": [0, 3]
    },
    {
        "question_id": "java_mcq_6",
        "question_text_full": "What is the output of this code?\n\nString s1 = \"Java\";\nString s2 = new String(\"Java\");\nString s3 = s2.intern();\n\nSystem.out.print(s1 == s2);\nSystem.out.print(\", \");\nSystem.out.print(s1 == s3);\n",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "Java",
        "points": "10",
        "time": "3-00",
        "topic": "JVM & Memory",
        "options": [
            "true, true",
            "true, false",
            "false, true",
            "false, false"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "java_mcq_7",
        "question_text_full": "Given a NavigableMap<Integer, String> populated with keys {10, 20, 30, 40}. What will map.floorEntry(25) return?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Skill/Concept",
        "domain": "Java",
        "points": "12",
        "time": "4-00",
        "topic": "Collections",
        "options": [
            "The entry for key 20",
            "The entry for key 30",
            "null",
            "It will throw an `IllegalArgumentException`."
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "java_msq_8",
        "question_text_full": "Due to Java's type erasure, which of the following code snippets will fail to compile?",
        "question_type": "Multiple Selection",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Strategic Thinking",
        "domain": "Java",
        "points": "15",
        "time": "6-00",
        "topic": "Generics",
        "options": [
            "public <T> T createInstance() { return new T(); }",
            "List<Integer> li = new ArrayList<>(); List<String> ls = new ArrayList<>(); if(li.getClass() == ls.getClass()) { ... }",
            "public void doSomething(List<String> list) {}",
            "if (obj instanceof List<String>) { ... }"
        ],
        "correct_answers": [0, 3]
    },
    {
        "question_id": "java_mcq_9",
        "question_text_full": "Given a List<Person>, how would you create a Map<Department, Long> that counts the number of people in each department using the Stream API?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Extended Thinking",
        "domain": "Java",
        "points": "20",
        "time": "8-00",
        "topic": "Lambda & Streams",
        "options": [
            "people.stream().collect(Collectors.groupingBy(Person::getDepartment, Collectors.counting()));",
            "people.stream().collect(Collectors.toMap(Person::getDepartment, p -> 1L, Long::sum));",
            "people.stream().groupBy(Person::getDepartment).count();",
            "Both A and B are correct and functionally equivalent."
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "java_mcq_10",
        "question_text_full": "Which feature is provided by 'ReentrantLock' but NOT by the 'synchronized' keyword in Java?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Recall",
        "domain": "Java",
        "points": "10",
        "time": "3-00",
        "topic": "Concurrency",
        "options": [
            "Reentrancy (a thread can re-acquire a lock it already holds).",
            "Mutual exclusion for critical sections.",
            "The ability to specify a fairness policy.",
            "Visibility of changes to shared variables across threads."
        ],
        "correct_answers": [2]
    }
]


class Command(BaseCommand):
    help = 'Import Java questions from the QUESTIONS list'

    def handle(self, *args, **kwargs):
        for item in QUESTIONS:
            JavaQuestion.objects.update_or_create(
                question_id=item['question_id'],
                defaults={
                    'question_text_full': item['question_text_full'],
                    'question_type': item['question_type'],
                    'difficulty': item['difficulty'],
                    'depth_of_knowledge': item['depth_of_knowledge'],
                    'domain': item['domain'],
                    'points': item['points'],
                    'time': item['time'],
                    'topic': item['topic'],
                    'options': item['options'],
                    'correct_answers': item['correct_answers'],
                }
            )
        self.stdout.write(self.style.SUCCESS('Successfully imported Java questions'))