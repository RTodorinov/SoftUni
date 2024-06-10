SELECT 
	*
FROM 
	departments
JOIN 
	employees 
ON 
	departments.id = employees.department_id;
-------------------------------------------------
SELECT 
	*
FROM departments as d
JOIN employees as e
ON d.id = e.department_id;
