SELECT 
	last_name,
	COUNT(notes) AS notes_with_dumbledore 
FROM wizard_deposits
WHERE notes LIKE '%Dumbledore%'
GROUP BY last_name;

SELECT 
	last_name,
	COUNT(notes) AS "Notes with Dumbledore"
FROM 
	wizard_deposits
WHERE 
	notes LIKE '%Dumbledore%'
GROUP BY 
	last_name;

SELECT 
	last_name,
	COUNT(*) AS "Notes with Dumbledore"
FROM 
	wizard_deposits
WHERE 
	notes LIKE '%Dumbledore%'
GROUP BY 
	last_name;