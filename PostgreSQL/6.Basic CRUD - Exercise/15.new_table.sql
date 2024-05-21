CREATE TABLE company_chart
AS SELECT 
	CONCAT_WS(' ',first_name,last_name) AS full_name,
	job_title,
	department_id,
	manager_id
FROM employees;
-- check new table
SELECT * FROM company_chart;
-- diferent style 
CREATE TABLE IF NOT EXISTS company_chart 
AS 
SELECT
	CONCAT(
		first_name,
		' ',
		last_name
	) AS full_name,
	job_title,
	department_id,
	manager_id
FROM
	employees;