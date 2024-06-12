SELECT
	mc.country_code,
	m.mountain_range,
	p.peak_name,
	p.elevation
FROM peaks AS p
	JOIN mountains AS m
		ON m.id = p.mountain_id
			JOIN mountains_countries AS mc
				ON mc.mountain_id = m.id
					--JOIN countries AS c
						--USING (country_code)
WHERE elevation > 2835 AND mc.country_code = 'BG'
ORDER BY elevation DESC;
-----------------------------------------------
SELECT 
	mc.country_code,
	m.mountain_range,
	p.peak_name,
	p.elevation
FROM
	mountains_countries AS mc
JOIN
	mountains AS m
ON 
	m.id = mc.mountain_id
JOIN 
	peaks AS p
ON
	m.id = p.mountain_id
WHERE 
	p.elevation > 2835 
		AND
	mc.country_code = 'BG'
ORDER BY
	p.elevation DESC;