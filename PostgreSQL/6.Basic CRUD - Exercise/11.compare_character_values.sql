SELECT 
	name,
	start_date
FROM projects
WHERE name IN('Mountain','Road') 
OR name IN('Touring')
LIMIT 20;

SELECT
	name,
	start_date
FROM
	projects
WHERE
	name IN ('Mountain', 'Road', 'Touring')
LIMIT 20;