SELECT 
	continent_name,
	LTRIM(continent_name, ' ') AS "trim"
FROM
	continents;

SELECT
	continent_name,
	TRIM(LEADING FROM continent_name) AS "trim"
	-- LTRIM(continent_name) AS "trim" -- same thing as the upper solution
FROM
	continents;
--LEADING, BOTH, TRAILING : от началото, от двете страни, от края