SELECT
population,
LENGTH(CAST(population AS VARCHAR)) AS length
FROM countries;

SELECT 
	population,
	LENGTH(CAST(population AS VARCHAR)) AS length
FROM
	countries
-- За да ползваме LENGHT първо обръщаме population с CAST във VARCHAR
-- The PostgreSQL LENGTH() function returns the number of characters in a string.
