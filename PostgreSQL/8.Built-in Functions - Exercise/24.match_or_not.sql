SELECT
	companion_full_name,
	email
FROM users
WHERE companion_full_name ILIKE '%aNd%' AND email NOT LIKE '%@gmail';

SELECT
	companion_full_name,
	email
FROM
	users
WHERE
	companion_full_name ILIKE '%aNd%' -- and And aNd anD....сравнява case insensitive
		AND
	email NOT LIKE '%@gmail'; -- sasho@gmail - not valid; sasho@gmail.com - valid cause its not ending gmail