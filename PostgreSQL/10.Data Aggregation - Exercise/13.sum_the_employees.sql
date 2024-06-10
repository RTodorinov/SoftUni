SELECT 
	COUNT(CASE WHEN department_id = 1 THEN 1 END) AS "Engineering",
	COUNT(CASE WHEN department_id = 2 THEN 1 END) AS "Tool Design",
	COUNT(CASE WHEN department_id = 3 THEN 1 END) AS "Sales",
	COUNT(CASE WHEN department_id = 4 THEN 1 END) AS "Marketing",
	COUNT(CASE WHEN department_id = 5 THEN 1 END) AS "Purchasing",
	COUNT(CASE WHEN department_id = 6 THEN 1 END) AS "Research and Development",
	COUNT(CASE WHEN department_id = 7 THEN 1 END) AS "Production"
FROM employees;

SELECT 
	COUNT(CASE department_id WHEN 1 THEN 1 ELSE 0 END) "Engineering",
	COUNT(CASE department_id WHEN 2 THEN 1 ELSE 0 END) "Tool Design",
	COUNT(CASE department_id WHEN 3 THEN 1 ELSE 0 END) "Sales",
	COUNT(CASE department_id WHEN 4 THEN 1 ELSE 0 END) "Marketing",
	COUNT(CASE department_id WHEN 5 THEN 1 ELSE 0 END) "Purchasing",
	COUNT(CASE department_id WHEN 6 THEN 1 ELSE 0 END) "Research and Development",
	COUNT(CASE department_id WHEN 7 THEN 1 ELSE 0 END) "Production"
FROM employees;