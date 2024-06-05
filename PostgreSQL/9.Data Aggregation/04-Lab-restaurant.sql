-- Grouping Syntax
SELECT column_one,
column_two
FROM table_name
GROUP BY column_one,
column_two;
-- Get each separate group to use an "aggregate" function over it
SELECT column_one,
aggregate_function(column_two)
FROM table_name
GROUP BY column_one;
/* Aggregate Functions
Used to operate over one or more groups performing
data analysis on every one
MIN, MAX, AVG, COUNT, SUM, etc.
They usually ignore NULL values
*/
-- COUNT Syntax
SELECT
	department_id,
	COUNT("id") AS employee_count -- agregation function COUNT
FROM employees
GROUP BY department_id
ORDER BY department_id;

SELECT
	department_id,
	COUNT(department_id) AS employee_count -- agregation function COUNT
FROM employees
GROUP BY department_id -- grouping by group out of agregation function
ORDER BY department_id;

SELECT * FROM employees

SELECT
	category_id,
	COUNT(category_id) AS product_count
FROM products
GROUP BY category_id
ORDER BY category_id;

SELECT * FROM products;

SELECT salary
FROM employees

SELECT
	department_id,
	COUNT(salary) AS employee_count	
FROM employees
GROUP BY department_id
ORDER BY department_id;

SELECT
	first_name,
	department_id,
	SUM(salary) AS sum_salary
FROM employees
WHERE salary IS NOT NULL
GROUP BY department_id, first_name
ORDER BY sum_salary DESC;

SELECT
	department_id,
	SUM(salary) AS total_salaries
FROM employees
GROUP BY department_id
ORDER BY department_id;

SELECT
	department_id,
	MAX(salary) AS max_salary
FROM employees
GROUP BY department_id
ORDER BY department_id;

SELECT
	department_id,
	MIN(salary) AS min_salary
FROM employees
GROUP BY department_id
ORDER BY department_id;

SELECT
	department_id,
	AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
ORDER BY department_id;

/*
Having Clause
The HAVING clause is used to filter data based on
aggregate values
We cannot use it without grouping before that
Any Aggregate functions in the "HAVING" clause and
in the "SELECT" statement are executed one
time only
Unlike HAVING, the WHERE clause filters rows before
the aggregation
*/
SELECT
	department_id,
	SUM(salary) AS "Total Salary"
FROM employees
GROUP BY department_id
HAVING SUM(salary) < 4200
ORDER BY department_id;

SELECT
	department_id,
	SUM(salary) AS "Total Salary"
FROM employees
WHERE salary > 1000
GROUP BY department_id
HAVING SUM(salary) < 4200
ORDER BY department_id;

/*
SELECT --> FROM --> WHERE --> GROUP BY --> HAVING --> ORDER BY --> LIMIT
*/
-- CASE Expression
/*
The PostgreSQL CASE expression is the same as
IF/ELSE statement in other programming languages
It allows you to add if-else logic to form a
powerful query
The CASE expression has two forms: general and
simple form
Can be used in SELECT, WHERE, GROUP BY clauses
*/
--CASE Expression Simple Syntax
/*
CASE
	WHEN condition_1 THEN result_1
	WHEN condition_2 THEN result_2
	...
ELSE else_result
END AS column_name
*/
	
SELECT id, first_name, last_name, 
TRUNC(salary, 2) AS salary, department_id,
	CASE
 		WHEN department_id = 1 THEN 'Management'
		WHEN department_id = 2 THEN 'Kitchen Staff'
		WHEN department_id = 3 THEN 'Service Staff'
		ELSE 'Other'
	END AS department_name
FROM employees
ORDER BY id;

SELECT id, first_name, last_name, 
TRUNC(salary, 2) AS salary, department_id,
	CASE department_id
 		WHEN 1 THEN 'Management'
		WHEN 2 THEN 'Kitchen Staff'
		WHEN 3 THEN 'Service Staff'
		ELSE 'Other'
	END AS department_name
FROM employees
ORDER BY id;
-- CASE Expression in Aggregate Functions

SELECT SUM(salary) AS total_salaries,
SUM(CASE department_id
	WHEN 1 THEN salary*1.15
	WHEN 2 THEN salary*1.10
	ELSE salary*1.05
	END) AS total_increased_salaries
FROM employees;

-- CASE Expression and GROUP BY

SELECT
CASE
	WHEN category_id IN (1, 2, 3) THEN 'Starters'
	WHEN category_id = 4 THEN 'Mains'
	ELSE 'Desserts'
	END AS "new product category",
COUNT(id)
FROM products
GROUP BY "new product category";

-- CASE Expression in HAVING

SELECT
CASE
	WHEN salary < 1000 THEN 'Low (< 1000)'
	WHEN salary <= 3000 THEN 'Middle (1000-3000)'
	ELSE 'High (> 3000)'
	END AS "salary_range",
COUNT(salary) AS "salary_count"
FROM employees
GROUP BY "salary_range"
HAVING CASE COUNT(salary)
	WHEN 0 THEN 'false'::boolean
	ELSE 'true'::boolean
	END;
