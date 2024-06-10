/*
JOINS
Used to collect data from two or more tables
▪ Types:
INNER JOIN - Produces a set of records that match in both tables
LEFT JOIN - Matches every entry in left table regardless of match in the right
RIGHT JOIN - Matches every entry in right table regardless of match in the left
FULL JOIN - Returns all records in both tables regardless of any match
CROSS JOIN - Produces a set of associated rows of two tables
▪ Multiplication of each row in the first table with each in the
second one
▪ The result is a Cartesian product when there's no condition
in the WHERE clause

*/
SELECT
	t.town_id,
	t.name AS town_name,
	a.address_text
FROM 
	towns AS t
		JOIN addresses AS a
			ON a.town_id = t.town_id
WHERE t.name IN ('San Francisco', 'Sofia', 'Carnation') 
ORDER BY
	t.town_id,
	a.address_id;
------------------------------------
SELECT
	t.town_id,
	t.name AS town_name,
	a.address_text
FROM 
	towns AS t
		JOIN addresses AS a
			USING(town_id)
WHERE t.name IN ('San Francisco', 'Sofia', 'Carnation') 
ORDER BY
	t.town_id,
	a.address_id;
--------------------------------------------------------
SELECT
	e.employee_id,
	CONCAT(e.first_name, ' ', e.last_name) AS full_name,
	d.department_id,
	d.name AS department_name
FROM 
	employees AS e
		JOIN departments AS d
			ON e.employee_id = d.manager_id
ORDER BY
	e.employee_id
LIMIT 5;
-------------------------------------------------
SELECT
	e.employee_id,
	CONCAT(e.first_name, ' ', e.last_name) AS full_name,
	d.department_id,
	d.name AS department_name
FROM 
	employees AS e
		RIGHT JOIN departments AS d
			ON e.employee_id = d.manager_id
ORDER BY
	e.employee_id
LIMIT 5;
-------------------------------------------------
/*
Subqueries
Subqueries – SQL query inside a larger one
▪ Can be nested in SELECT, INSERT, UPDATE, DELETE
▪ Usually added within a WHERE clause

SELECT employee_id AS
	id, first_name,
	department_id
FROM employees
WHERE department_id = 1;
*/
SELECT
	ep.employee_id,
	CONCAT(e.first_name, ' ', e.last_name) AS full_name,
	ep.project_id,
	projects.name AS project_names
FROM
	employees AS e
		JOIN employees_projects AS ep
			ON e.employee_id = ep.employee_id,
	projects
WHERE ep.project_id = 1 AND projects.project_id = 1;
------------------------------------------------------
SELECT
	e.employee_id,
	CONCAT(e.first_name, ' ', e.last_name) AS full_name,
	p.project_id,
	p.name AS project_names
FROM
	employees AS e
		JOIN employees_projects AS ep
			USING (employee_id)
				JOIN projects AS p
					ON ep.project_id = p.project_id
	
WHERE p.project_id = 1;
---------------------------------------------------
SELECT
	e.employee_id,
	CONCAT(e.first_name, ' ', e.last_name) AS full_name,
	p.project_id,
	p.name AS project_names
FROM
	employees AS e
		JOIN employees_projects AS ep
			USING (employee_id)
				JOIN projects AS p
					USING (project_id)
	
WHERE p.project_id = 1;
----------------------------------------------------------
ALTER TABLE employees 
ADD COLUMN bonus_salary INT DEFAULT 0 -- създаване на колона с дефолтна стойност 0
----------------------------------------------------------
SELECT FLOOR(RANDOM() * 10000) -- създаване на рандъм число с таван 10000
------------------------------------------------------------
UPDATE employees
SET bonus_salary = FLOOR(RANDOM() * 10000 + 1); -- запълване на колоната с тестови данни 
------------------------------------------------------------------
SELECT
	COUNT(salary) -- COUNT(*)
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
--------------------------------------------------------
SELECT COUNT(e.employee_id) AS "count"
FROM employees AS e
WHERE e.salary >
(
SELECT AVG(salary) AS
"average_salary" FROM employees
);
-------------------------------------------
/*
Indices
Special lookup tables that speed retrieval of rows
▪ Usually implemented as B-trees
▪ Speed up SELECT queries and WHERE clauses
▪ Slows down data input
▪ Should be used for big tables only (e.g., 50 000 rows)
▪ Should NOT be used on columns that contain a high
number of NULL values

Indices Syntax:

CREATE INDEX index_name_idx
ON table_name(first_column, second_column);

*/
-------------------------------------------------
/*
Summary

▪ Joins

SELECT * FROM employees AS e
	JOIN departments AS d ON
		d.department_id = e.department_id

▪ Subqueries are used to nest queries

▪ Indices improve SQL search performance if used properly

*/