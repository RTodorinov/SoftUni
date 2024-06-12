SELECT 
    MIN(avg_area) AS min_average_area 
FROM (
SELECT
	continent_code,
	AVG(area_in_sq_km) AS avg_area
FROM
	countries
GROUP BY
	continent_code
	) AS continent_averages;
--------------------------------------
SELECT 
	MIN(average_area) AS min_average_area
FROM (
	SELECT
		AVG(area_in_sq_km) AS average_area
	FROM 
		countries 
	GROUP BY
		continent_code
) AS min_average_area