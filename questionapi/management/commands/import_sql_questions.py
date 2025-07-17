from django.core.management.base import BaseCommand
from questionapi.models import SQLQuestion

QUESTIONS = [
    {
        "question_id": "sql_1",
        "question_text_full": "Identify the correct SQL query to retrieve FIRST_NAME from the Worker table using the alias WORKER_NAME?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SQL",
        "points": "5",
        "time": "2-00",
        "topic": "Aliases",
        "options": [
            "SELECT WORKER_NAME FROM worker;",
            "SELECT first_name AS WORKER_NAME FROM worker;",
            "SELECT first_name FROM worker AS WORKER_NAME;",
            "SELECT first_name TO WORKER_NAME FROM worker;"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sql_2",
        "question_text_full": "Determine the appropriate SQL query to retrieve FIRST_NAME in uppercase from the Worker table?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SQL",
        "points": "5",
        "time": "2-00",
        "topic": "String Functions",
        "options": [
            "SELECT UCASE (first_name) FROM worker;",
            "SELECT TOUPPER (first_name) FROM worker;",
            "SELECT UPPER (first_name) FROM worker;",
            "SELECT CAPS (first_name) FROM worker;"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sql_3",
        "question_text_full": "Select the SQL query that returns unique values from the DEPARTMENT column in the Worker table?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SQL",
        "points": "5",
        "time": "2-00",
        "topic": "DISTINCT Keyword",
        "options": [
            "SELECT ALL department FROM worker;",
            "SELECT UNIQUE department FROM worker;",
            "SELECT department FROM worker;",
            "SELECT DISTINCT department FROM worker;"
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "sql_4",
        "question_text_full": "Identify the SQL query that extracts the first three characters from the FIRST_NAME column?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "8",
        "time": "2-00",
        "topic": "String Functions",
        "options": [
            "SELECT LEFT(first_name, 3) FROM worker;",
            "SELECT SUBSTRING(first_name, 1, 3) FROM worker;",
            "SELECT SUBSTR(first_name, 0, 3) FROM worker;",
            "SELECT MID(first_name, 1, 3) FROM worker;"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sql_5",
        "question_text_full": "Ascertain the SQL query that returns the position of the character 'b' in FIRST_NAME where FIRST_NAME = 'Amitabh'?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "8",
        "time": "2-00",
        "topic": "String Functions",
        "options": [
            "SELECT POSITION('b' IN first_name) FROM worker;",
            "SELECT LOCATE('b', first_name) FROM worker WHERE first_name = 'Amitabh';",
            "SELECT INSTR(first_name, 'B') FROM worker WHERE first_name = 'Amitabh';",
            "SELECT CHARINDEX('b', first_name) FROM worker;"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sql_6",
        "question_text_full": "Determine the correct query to eliminate trailing spaces from FIRST_NAME in the Worker table?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SQL",
        "points": "5",
        "time": "2-00",
        "topic": "String Functions",
        "options": [
            "SELECT TRIM(first_name) FROM worker;",
            "SELECT LTRIM(first_name) FROM worker;",
            "SELECT RIGHTTRIM(first_name) FROM worker;",
            "SELECT RTRIM(first_name) FROM worker;"
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "sql_7",
        "question_text_full": "Identify the appropriate SQL statement to remove leading spaces from FIRST_NAME?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SQL",
        "points": "5",
        "time": "2-00",
        "topic": "String Functions",
        "options": [
            "SELECT LTRIM(first_name) FROM worker;",
            "SELECT RTRIM(first_name) FROM worker;",
            "SELECT TRIMLEFT(first_name) FROM worker;",
            "SELECT STRIP(first_name) FROM worker;"
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "sql_8",
        "question_text_full": "Determine the correct query to retrieve unique DEPARTMENT values along with their character lengths?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "8",
        "time": "2-00",
        "topic": "DISTINCT, String Functions",
        "options": [
            "SELECT DISTINCT department, LENGTH(department) FROM worker;",
            "SELECT department, LEN(department) FROM worker;",
            "SELECT department, LENGTH(department) FROM worker;",
            "SELECT UNIQUE department, LENGTH(department) FROM worker;"
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "sql_9",
        "question_text_full": "Identify the correct SQL query that replaces lowercase 'a' with uppercase 'A' in FIRST_NAME?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "8",
        "time": "2-00",
        "topic": "String Functions",
        "options": [
            "SELECT REPLACE(first_name, 'A', 'a') FROM worker;",
            "SELECT REPLACE(first_name, 'a', 'A') FROM worker;",
            "SELECT SUBSTITUTE(first_name, 'a', 'A') FROM worker;",
            "SELECT CHANGE(first_name, 'a', 'A') FROM worker;"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sql_10",
        "question_text_full": "Ascertain the correct SQL query to display FIRST_NAME and LAST_NAME as COMPLETE_NAME, separated by a space?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SQL",
        "points": "5",
        "time": "2-00",
        "topic": "String Concatenation",
        "options": [
            "SELECT first_name || last_name AS COMPLETE_NAME FROM worker;",
            "SELECT first_name + last_name AS COMPLETE_NAME FROM worker;",
            "SELECT CONCAT(first_name, ' ', last_name) AS COMPLETE_NAME FROM worker;",
            "SELECT CONCAT_WS(' ', first_name, last_name) FROM worker;"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sql_11",
        "question_text_full": "Determine the query that retrieves all worker records ordered by FIRST_NAME in ascending order?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SQL",
        "points": "5",
        "time": "2-00",
        "topic": "ORDER BY",
        "options": [
            "SELECT * FROM worker ORDER BY department;",
            "SELECT * FROM worker ORDER BY salary;",
            "SELECT * FROM worker ORDER BY first_name;",
            "SELECT * FROM worker ORDER BY last_name;"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sql_12",
        "question_text_full": "Select the query that lists worker details ordered by FIRST_NAME in ascending order and DEPARTMENT in descending order?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "8",
        "time": "2-00",
        "topic": "ORDER BY Multiple Columns",
        "options": [
            "SELECT * FROM worker ORDER BY department, first_name DESC;",
            "SELECT * FROM worker ORDER BY first_name ASC, department DESC;",
            "SELECT * FROM worker ORDER BY department ASC, first_name DESC;",
            "SELECT * FROM worker ORDER BY first_name;"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sql_13",
        "question_text_full": "Identify the SQL query that returns records for workers whose FIRST_NAME is either 'Vipul' or 'Satish'?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SQL",
        "points": "5",
        "time": "2-00",
        "topic": "IN Operator",
        "options": [
            "SELECT * FROM worker WHERE first_name IN ('Vipul', 'Satish');",
            "SELECT * FROM worker WHERE first_name = 'Vipul' AND 'Satish';",
            "SELECT * FROM worker WHERE first_name LIKE 'Vipul' AND 'Satish';",
            "SELECT * FROM worker WHERE first_name NOT IN ('Vipul', 'Satish');"
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "sql_14",
        "question_text_full": "Determine the correct query that excludes records for workers named 'Vipul' and 'Satish'?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SQL",
        "points": "5",
        "time": "2-00",
        "topic": "NOT IN Operator",
        "options": [
            "SELECT * FROM worker WHERE first_name = 'Vipul' OR first_name = 'Satish';",
            "SELECT * FROM worker WHERE first_name NOT IN ('Vipul', 'Satish');",
            "SELECT * FROM worker WHERE NOT first_name = 'Vipul' AND 'Satish';",
            "SELECT * FROM worker WHERE first_name IS NOT ('Vipul', 'Satish');"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sql_15",
        "question_text_full": "Determine the query that retrieves workers belonging to departments beginning with 'Admin'?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SQL",
        "points": "5",
        "time": "2-00",
        "topic": "LIKE Operator",
        "options": [
            "SELECT * FROM worker WHERE department = 'Admin';",
            "SELECT * FROM worker WHERE department CONTAINS 'Admin';",
            "SELECT * FROM worker WHERE department LIKE 'Admin%';",
            "SELECT * FROM worker WHERE department STARTS WITH 'Admin';"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sql_16",
        "question_text_full": "Select the appropriate query that extracts workers whose FIRST_NAME contains the character 'a'?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SQL",
        "points": "5",
        "time": "2-00",
        "topic": "LIKE Operator",
        "options": [
            "SELECT * FROM worker WHERE first_name HAS 'a';",
            "SELECT * FROM worker WHERE first_name LIKE '%a%';",
            "SELECT * FROM worker WHERE first_name INCLUDES 'a';",
            "SELECT * FROM worker WHERE first_name STARTS WITH 'a';"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sql_17",
        "question_text_full": "Ascertain the query that retrieves workers whose FIRST_NAME terminates with the letter 'a'?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SQL",
        "points": "5",
        "time": "2-00",
        "topic": "LIKE Operator",
        "options": [
            "SELECT * FROM worker WHERE first_name ENDS WITH 'a';",
            "SELECT * FROM worker WHERE first_name LIKE 'a%';",
            "SELECT * FROM worker WHERE first_name LIKE '%a';",
            "SELECT * FROM worker WHERE first_name = '*a';"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sql_18",
        "question_text_full": "Identify the query that returns workers whose FIRST_NAME consists of six characters and ends in 'h'?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "8",
        "time": "2-00",
        "topic": "LIKE Operator",
        "options": [
            "SELECT * FROM worker WHERE first_name LIKE '_____h';",
            "SELECT * FROM worker WHERE LENGTH(first_name) = 6 AND first_name LIKE '%h';",
            "SELECT * FROM worker WHERE first_name LIKE '%_____h';",
            "SELECT * FROM worker WHERE first_name = '_____h';"
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "sql_19",
        "question_text_full": "Determine the SQL query that retrieves workers with a SALARY between 100,000 and 500,000?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SQL",
        "points": "5",
        "time": "0-30",
        "topic": "BETWEEN Operator",
        "options": [
            "SELECT * FROM worker WHERE salary >= 100000 AND salary <= 500000;",
            "SELECT * FROM worker WHERE salary IN (100000, 500000);",
            "SELECT * FROM worker WHERE salary = 100000 TO 500000;",
            "SELECT * FROM worker WHERE salary RANGE 100000-500000;"
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "sql_20",
        "question_text_full": "Identify the query that returns workers who joined in February 2014?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "8",
        "time": "0-45",
        "topic": "Date Functions",
        "options": [
            "SELECT * FROM worker WHERE MONTH(joining_date) = 'Feb' AND YEAR(joining_date) = 2014;",
            "SELECT * FROM worker WHERE joining_date = '2014-02';",
            "SELECT * FROM worker WHERE YEAR(joining_date) = 2014 AND MONTH(joining_date) = 02;",
            "SELECT * FROM worker WHERE joining_date LIKE '2014-02%';"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sql_21",
        "question_text_full": "Select the query that provides the count of employees within the 'Admin' department?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SQL",
        "points": "5",
        "time": "0-30",
        "topic": "Aggregate Functions, WHERE",
        "options": [
            "SELECT department, COUNT() FROM worker;",
            "SELECT COUNT() FROM worker WHERE department = 'Admin';",
            "SELECT department, COUNT(*) FROM worker WHERE department = 'Admin';",
            "SELECT * FROM worker WHERE department = 'Admin';"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sql_22",
        "question_text_full": "Determine the query that retrieves full names of workers earning between 50,000 and 100,000?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "8",
        "time": "0-45",
        "topic": "String Concatenation, BETWEEN",
        "options": [
            "SELECT CONCAT(first_name, last_name) FROM worker WHERE salary BETWEEN 50000 AND 100000;",
            "SELECT full_name FROM worker WHERE salary BETWEEN 50000 AND 100000;",
            "SELECT CONCAT(first_name, ' ', last_name) FROM worker WHERE salary BETWEEN 50000 AND 100000;",
            "SELECT CONCAT_WS(' ', first_name, last_name) FROM worker WHERE salary >= 50000 AND salary <= 100000;"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sql_23",
        "question_text_full": "Ascertain the query that returns the number of workers per department, sorted in descending order?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "10",
        "time": "1-00",
        "topic": "GROUP BY, ORDER BY",
        "options": [
            "SELECT department, COUNT(*) FROM worker GROUP BY department;",
            "SELECT department, COUNT(worker_id) AS no_of_worker FROM worker GROUP BY department ORDER BY no_of_worker DESC;",
            "SELECT department, COUNT(worker_id) FROM worker ORDER BY department DESC;",
            "SELECT * FROM worker GROUP BY department DESC;"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sql_24",
        "question_text_full": "Identify the query that retrieves workers who also serve as managers?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "12",
        "time": "1-30",
        "topic": "JOINs",
        "options": [
            "SELECT * FROM worker WHERE title = 'Manager';",
            "SELECT w.* FROM worker w JOIN title t ON w.worker_id = t.worker_id WHERE t.title = 'Manager';",
            "SELECT w.* FROM worker w INNER JOIN title t ON w.worker_id = t.worker_ref_id WHERE t.worker_title = 'Manager';",
            "SELECT * FROM worker WHERE worker_title = 'Manager';"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sql_25",
        "question_text_full": "Identify the SQL query that retrieves titles appearing more than once?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "10",
        "time": "1-00",
        "topic": "GROUP BY, HAVING",
        "options": [
            "SELECT worker_title, COUNT() FROM title GROUP BY worker_title;",
            "SELECT title, COUNT() FROM worker GROUP BY title HAVING COUNT > 1;",
            "SELECT worker_title, COUNT() AS count FROM title GROUP BY worker_title HAVING count > 1;",
            "SELECT worker_title FROM title GROUP BY worker_title HAVING COUNT() > 1;"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sql_26",
        "question_text_full": "Determine the query that extracts only rows with odd worker_id values from the worker table?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "5",
        "time": "0-30",
        "topic": "Modulo Operator",
        "options": [
            "SELECT * FROM worker WHERE MOD(worker_id, 2) = 0;",
            "SELECT * FROM worker WHERE MOD(worker_id, 2) != 0;",
            "SELECT * FROM worker WHERE worker_id % 2 = 0;",
            "SELECT * FROM worker WHERE ISODD(worker_id);"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sql_27",
        "question_text_full": "Ascertain the query that returns only even-numbered rows from the worker table?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "5",
        "time": "0-30",
        "topic": "Modulo Operator",
        "options": [
            "SELECT * FROM worker WHERE MOD(worker_id, 2) = 0;",
            "SELECT * FROM worker WHERE MOD(worker_id, 2) <> 0;",
            "SELECT * FROM worker WHERE worker_id % 2! = 0;",
            "SELECT * FROM worker WHERE ISEVEN(worker_id);"
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "sql_28",
        "question_text_full": "Determine the query that creates a clone of the worker table and copies its data?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "10",
        "time": "1-00",
        "topic": "Table Creation, Copying Data",
        "options": [
            "CREATE worker_clone FROM worker; COPY DATA;",
            "SELECT * INTO worker_clone FROM worker;",
            "CREATE TABLE worker_clone LIKE worker; INSERT INTO worker_clone SELECT * FROM worker;",
            "CLONE TABLE worker TO worker_clone;"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sql_29",
        "question_text_full": "Identify the query that retrieves intersecting records from worker and worker_clone?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "10",
        "time": "1-00",
        "topic": "JOINs, INTERSECT",
        "options": [
            "SELECT * FROM worker INTERSECT worker_clone;",
            "SELECT worker.* FROM worker JOIN worker_clone ON worker.worker_id = worker_clone.worker_id;",
            "SELECT worker.* FROM worker INNER JOIN worker_clone USING(worker_id);",
            "SELECT * FROM worker WHERE EXISTS IN worker_clone;"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sql_30",
        "question_text_full": "Ascertain the query that returns rows from worker not present in worker_clone?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "10",
        "time": "1-00",
        "topic": "LEFT JOIN, EXCEPT, MINUS",
        "options": [
            "SELECT * FROM worker MINUS SELECT * FROM worker_clone;",
            "SELECT worker.* FROM worker LEFT JOIN worker_clone USING(worker_id) WHERE worker_clone.worker_id IS NULL;",
            "SELECT * FROM worker WHERE NOT EXISTS (SELECT * FROM worker_clone);",
            "SELECT * FROM worker EXCEPT SELECT * FROM worker_clone;"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sql_31",
        "question_text_full": "Determine the query that retrieves the current date and time?",
        "question_type": "Multiple Choice",
        "difficulty": "Beginner",
        "depth_of_knowledge": "Recall",
        "domain": "SQL",
        "points": "5",
        "time": "0-30",
        "topic": "Date/Time Functions",
        "options": [
            "SELECT CURRENT_TIMESTAMP();",
            "SELECT NOW();",
            "SELECT CURDATE();",
            "All of the above"
        ],
        "correct_answers": [3]
    },
    {
        "question_id": "sql_32",
        "question_text_full": "Identify the query that fetches the top 5 records ordered by salary in descending order?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "8",
        "time": "0-45",
        "topic": "LIMIT, TOP",
        "options": [
            "SELECT TOP 5 * FROM worker ORDER BY salary DESC;",
            "SELECT * FROM worker ORDER BY salary LIMIT 5;",
            "SELECT * FROM worker ORDER BY salary DESC LIMIT 5;",
            "SELECT FIRST 5 * FROM worker ORDER BY salary DESC;"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sql_33",
        "question_text_full": "Determine the SQL query that retrieves the fifth highest salary using the LIMIT clause?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "12",
        "time": "1-30",
        "topic": "LIMIT, OFFSET",
        "options": [
            "SELECT salary FROM worker ORDER BY salary LIMIT 5;",
            "SELECT salary FROM worker ORDER BY salary DESC LIMIT 5;",
            "SELECT * FROM worker ORDER BY salary DESC LIMIT 4,1;",
            "SELECT salary FROM worker ORDER BY salary DESC OFFSET 4 LIMIT 1;"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sql_34",
        "question_text_full": "Identify the query that retrieves the fifth highest salary without using the LIMIT clause?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "15",
        "time": "2-00",
        "topic": "Subqueries, Ranking",
        "options": [
            "SELECT salary FROM worker WHERE salary = (SELECT salary FROM worker ORDER BY salary DESC LIMIT 4,1);",
            "SELECT salary FROM worker WHERE salary = (SELECT DISTINCT salary FROM worker ORDER BY salary DESC LIMIT 4,1);",
            "SELECT salary FROM worker w1 WHERE 4 = (SELECT COUNT(DISTINCT w2.salary) FROM worker w2 WHERE w2.salary >= w1.salary);",
            "SELECT * FROM worker ORDER BY salary DESC OFFSET 4 ROWS FETCH NEXT 1 ROWS ONLY;"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sql_35",
        "question_text_full": "Ascertain the query that identifies employees with identical salary values?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "10",
        "time": "1-00",
        "topic": "Self-Join, GROUP BY",
        "options": [
            "SELECT * FROM worker WHERE salary IN (SELECT salary FROM worker GROUP BY salary HAVING COUNT() > 1);",
            "SELECT * FROM worker w1, worker w2 WHERE w1.salary = w2.salary AND w1.worker_id != w2.worker_id;",
            "SELECT salary FROM worker GROUP BY salary HAVING COUNT() > 1;",
            "SELECT * FROM worker WHERE salary MATCH salary;"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sql_36",
        "question_text_full": "Determine the query that finds the second highest salary using a subquery?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "12",
        "time": "1-30",
        "topic": "Subqueries, MAX",
        "options": [
            "SELECT MAX(salary) FROM worker WHERE salary NOT IN (SELECT MAX(salary) FROM worker);",
            "SELECT MAX(salary) FROM worker WHERE salary < (SELECT MAX(salary) FROM worker);",
            "SELECT MAX(salary) FROM (SELECT DISTINCT salary FROM worker ORDER BY salary DESC LIMIT 2) AS temp;",
            "SELECT MAX(salary) FROM worker WHERE salary != (SELECT MAX(salary) FROM worker);"
        ],
        "correct_answers": [0]
    },
    {
        "question_id": "sql_37",
        "question_text_full": "Identify the query that displays a single row twice in the output?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Conceptual Understanding",
        "domain": "SQL",
        "points": "8",
        "time": "0-45",
        "topic": "UNION ALL",
        "options": [
            "SELECT * FROM worker UNION SELECT * FROM worker;",
            "SELECT * FROM worker UNION ALL SELECT * FROM worker;",
            "SELECT * FROM worker CROSS JOIN worker;",
            "SELECT * FROM worker JOIN worker;"
        ],
        "correct_answers": [1]
    },
    {
        "question_id": "sql_38",
        "question_text_full": "Determine the query that lists workers who did not receive any bonus?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "10",
        "time": "1-00",
        "topic": "Subqueries, NOT IN",
        "options": [
            "SELECT * FROM worker WHERE bonus IS NULL;",
            "SELECT * FROM worker WHERE NOT EXISTS (SELECT * FROM bonus);",
            "SELECT worker_id FROM worker WHERE worker_id NOT IN (SELECT worker_ref_id FROM bonus);",
            "SELECT * FROM worker EXCEPT SELECT * FROM bonus;"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sql_39",
        "question_text_full": "Ascertain the query that retrieves the first 50% of records from a table?",
        "question_type": "Multiple Choice",
        "difficulty": "Advanced",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "12",
        "time": "1-30",
        "topic": "LIMIT, PERCENT",
        "options": [
            "SELECT * FROM worker WHERE worker_id < (SELECT COUNT(*)/2 FROM worker);",
            "SELECT * FROM worker LIMIT 50 PERCENT;",
            "SELECT * FROM worker WHERE worker_id <= (SELECT COUNT(worker_id)/2 FROM worker);",
            "SELECT TOP 50 PERCENT * FROM worker;"
        ],
        "correct_answers": [2]
    },
    {
        "question_id": "sql_40",
        "question_text_full": "Identify the SQL query that fetches departments having fewer than 4 employees?",
        "question_type": "Multiple Choice",
        "difficulty": "Intermediate",
        "depth_of_knowledge": "Application",
        "domain": "SQL",
        "points": "10",
        "time": "1-00",
        "topic": "GROUP BY, HAVING",
        "options": [
            "SELECT department FROM worker WHERE COUNT() < 4;",
            "SELECT department, COUNT() FROM worker GROUP BY department HAVING COUNT() < 4;",
            "SELECT department FROM worker GROUP BY department HAVING COUNT() < 4;",
            "SELECT * FROM worker WHERE department_count < 4;"
        ],
        "correct_answers": [1]
    }
]


class Command(BaseCommand):
    help = 'Import SQL Questions'

    def handle(self, *args, **kwargs):
        for q in QUESTIONS:
            SQLQuestion.objects.update_or_create(
                question_id=q["question_id"],
                defaults=q
            )
        self.stdout.write(self.style.SUCCESS('SQL questions imported!'))