UPDATE countries
SET country_code = REVERSE(LOWER(country_code));

UPDATE 
	countries
SET 
	country_code = LOWER(REVERSE(country_code));
