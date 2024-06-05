SELECT
	CASE
 		WHEN age > 0 and age < 11 THEN '[0-10]'
		WHEN age > 10 and age < 21 THEN '[11-20]'
		WHEN age > 20 and age < 31 THEN '[21-30]'
		WHEN age > 30 and age < 41 THEN '[31-40]'
		WHEN age > 40 and age < 51 THEN '[41-50]'
		WHEN age > 50 and age < 61 THEN '[51-60]'
		ELSE '[61+]'
	END AS age_group,	
	COUNT(age) AS count 
FROM wizard_deposits
GROUP BY age_group
ORDER BY age_group

SELECT
	CASE
        WHEN age BETWEEN 0 AND 10 THEN '[0-10]'
		WHEN age BETWEEN 11 AND 20 THEN '[11-20]'
		WHEN age BETWEEN 21 AND 30 THEN '[21-30]'
		WHEN age BETWEEN 31 AND 40 THEN '[31-40]'
		WHEN age BETWEEN 41 AND 50 THEN '[41-50]'
		WHEN age BETWEEN 51 AND 60 THEN '[51-60]'
		WHEN age >= 61 THEN '[61+]'
	END AS "Age Group",
	COUNT(*)
FROM 
	wizard_deposits
GROUP BY 
	"Age Group"
ORDER BY
	"Age Group" ASC;