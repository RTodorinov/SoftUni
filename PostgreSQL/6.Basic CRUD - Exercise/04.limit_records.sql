SELECT 
	id,
	CONCAT(first_name, ' ', last_name) AS full_name,
	job_title
FROM employees
ORDER BY first_name
Limit 50;
-- just different arrangement style
SELECT 
	id,
	CONCAT(
		first_name,
		' ',
		last_name
	) AS full_name,
	job_title
FROM 
	employees
ORDER BY
	first_name
LIMIT 50;