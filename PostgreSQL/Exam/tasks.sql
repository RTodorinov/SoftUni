CREATE TABLE IF NOT EXISTS accounts (
    id SERIAL PRIMARY KEY,
    username VARCHAR(30) NOT NULL UNIQUE,
    password VARCHAR(30) NOT NULL,
    email VARCHAR(50) NOT NULL,
    gender CHAR(1) NOT NULL,
    age INT NOT NULL, 
    job_title VARCHAR(40) NOT NULL,
    ip VARCHAR(30) NOT NULL,

	CONSTRAINT ck_age_is_postive
		CHECK (age >= 0),
	CONSTRAINT ck_gender_is_m_or_f
		CHECK (gender IN ('M', 'F'))
);

CREATE TABLE IF NOT EXISTS addresses (
    id SERIAL PRIMARY KEY,
    street VARCHAR(30) NOT NULL,
    town VARCHAR(30) NOT NULL,
    country VARCHAR(30) NOT NULL,
    account_id INT NOT NULL,

	CONSTRAINT fk_addresses_accounts
		FOREIGN KEY (account_id)
		REFERENCES accounts(id) 
		ON DELETE CASCADE 
		ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS photos (
    id SERIAL PRIMARY KEY,
    description TEXT,
    capture_date TIMESTAMP NOT NULL,
    views INT NOT NULL DEFAULT 0,

	CONSTRAINT ck_views_is_postive
		CHECK (views >= 0)
);

CREATE TABLE IF NOT EXISTS comments (
    id SERIAL PRIMARY KEY,
    content VARCHAR(255) NOT NULL,
    published_on TIMESTAMP NOT NULL,
    photo_id INT NOT NULL,

	CONSTRAINT fk_comments_photos
    	FOREIGN KEY (photo_id)
		REFERENCES photos(id) 
		ON DELETE CASCADE 
		ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS accounts_photos (
    account_id INT NOT NULL,
    photo_id INT NOT NULL,

	CONSTRAINT pk_accounts_photos
    	PRIMARY KEY (account_id, photo_id),
	CONSTRAINT fk_account_photos_accounts
    	FOREIGN KEY (account_id)
		REFERENCES accounts(id)
		ON DELETE CASCADE 
		ON UPDATE CASCADE,
	CONSTRAINT fk_account_photos_photos
    	FOREIGN KEY (photo_id) 
		REFERENCES photos(id) 
		ON DELETE CASCADE 
		ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS likes (
    id SERIAL PRIMARY KEY,
    photo_id INT NOT NULL,
    account_id INT NOT NULL,

	CONSTRAINT fk_likes_photos
    	FOREIGN KEY (photo_id) 
		REFERENCES photos(id) 
		ON DELETE CASCADE 
		ON UPDATE CASCADE,
	CONSTRAINT fk_likes_accounts
    	FOREIGN KEY (account_id) 
		REFERENCES accounts(id) 
		ON DELETE CASCADE 
		ON UPDATE CASCADE
);
-------------------------------------------------------
INSERT INTO addresses (street, town, country, account_id)
SELECT 
    username AS street,
    password AS town,
    ip AS country,
    age AS account_id
FROM 
    accounts
WHERE 
    gender = 'F';
---------------------------------------
UPDATE addresses
SET country = CASE
    WHEN country LIKE 'B%' THEN 'Blocked'
    WHEN country LIKE 'T%' THEN 'Test'
    WHEN country LIKE 'P%' THEN 'In Progress'
    ELSE country
END;
-----------------------------------------
DELETE FROM addresses
WHERE id % 2 = 0
AND LOWER(street) LIKE '%r%';
---------------------------------------------
SELECT 
    username, 
    gender, 
    age
FROM 
    accounts
WHERE 
    age >= 18 
    AND LENGTH(username) > 9
ORDER BY 
    age DESC, 
    username ASC;
-----------------------------------------------
SELECT
    p.id AS photo_id,
    p.capture_date,
    p.description,
    COUNT(c.id) AS comments_count
FROM
    photos AS p
JOIN
    comments AS c ON p.id = c.photo_id
WHERE
    p.description IS NOT NULL
GROUP BY
    p.id, p.capture_date, p.description
HAVING
    COUNT(c.id) > 0
ORDER BY
    comments_count DESC,
    p.id ASC
LIMIT 3;
----------------------------------
SELECT 
    CONCAT(a.id, ' ', a.username) AS id_username,
    a.email
FROM 
    accounts AS a
JOIN 
    accounts_photos AS ap
	ON a.id = ap.account_id
JOIN 
    photos AS p 
	ON ap.photo_id = p.id
WHERE 
    a.id = p.id
ORDER BY 
    a.id ASC;
--------------------------------------
SELECT 
    p.id AS photo_id,
    COALESCE(l.likes_count, 0) AS likes_count,
    COALESCE(c.comments_count, 0) AS comments_count
FROM 
    photos AS p
LEFT JOIN (
    SELECT 
        photo_id, 
        COUNT(*) AS likes_count
    FROM 
        likes
    GROUP BY 
        photo_id
) AS l ON p.id = l.photo_id
LEFT JOIN (
    SELECT 
        photo_id, 
        COUNT(*) AS comments_count
    FROM 
        comments
    GROUP BY 
        photo_id
) AS c ON p.id = c.photo_id
ORDER BY 
    likes_count DESC,
    comments_count DESC,
    photo_id ASC;
-----------------------------------------
SELECT 
    CASE 
        WHEN LENGTH(description) > 10 
        THEN SUBSTRING(description FROM 1 FOR 10) || '...'
        ELSE description 
    END AS summary,
    TO_CHAR(capture_date, 'DD.MM HH24:MI') AS date
FROM 
    photos
WHERE 
    EXTRACT(DAY FROM capture_date) = 10
ORDER BY 
    capture_date DESC;
------------------------------------------------------------------
SELECT 
    CASE 
        WHEN description IS NULL THEN '...'
        WHEN LENGTH(description) > 10 THEN SUBSTRING(description FROM 1 FOR 10) || '...'
        ELSE description 
    END AS summary,
    TO_CHAR(capture_date, 'DD.MM HH24:MI') AS date
FROM 
    photos
WHERE 
    EXTRACT(DAY FROM capture_date) = 10
ORDER BY 
    capture_date DESC;
------------------------------------------
SELECT 
    CASE 
        WHEN description IS NULL THEN '...'
        WHEN LENGTH(description) > 10 THEN SUBSTRING(description, 1, 10) || '...'
    END AS summary,
    TO_CHAR(capture_date, 'DD.MM HH24:MI') AS date
FROM 
    photos
WHERE 
    EXTRACT(DAY FROM capture_date) = 10
ORDER BY 
    capture_date DESC;
-------------------------------
SELECT 
    CASE 
        WHEN description IS NULL THEN '...'
        WHEN LENGTH(description) > 10 THEN LEFT(description, 10) || '...'
        ELSE description 
    END AS summary,
    TO_CHAR(capture_date, 'DD.MM HH24:MI') AS date
FROM 
    photos
WHERE 
    EXTRACT(DAY FROM capture_date) = 10
ORDER BY 
    capture_date DESC;
------------------------------------------
CREATE OR REPLACE FUNCTION udf_accounts_photos_count(account_username VARCHAR(30))
RETURNS INT AS 
$$
DECLARE
    photo_count INT;
BEGIN
    SELECT COUNT(*) INTO photo_count
    FROM accounts AS a
    	JOIN accounts_photos AS ap 
        	ON a.id = ap.account_id
    WHERE a.username = account_username;

    RETURN photo_count;
END;
$$ LANGUAGE plpgsql;
---------------------------------------------
CREATE OR REPLACE PROCEDURE udp_modify_account(address_street VARCHAR(30), address_town VARCHAR(30))
AS 
$$
BEGIN
    UPDATE accounts a
    SET job_title = '(Remote) ' || job_title
    FROM addresses ad
    WHERE a.id = ad.account_id
      AND ad.street = address_street
      AND ad.town = address_town
      AND a.job_title NOT LIKE '(Remote)%';
END;
$$
LANGUAGE plpgsql;

-------------------------------------------------------------
SELECT 
    COALESCE(LEFT(description, 10) || '...','...') AS summary,
    TO_CHAR(capture_date, 'DD.MM HH24:MI') AS date
FROM 
    photos
WHERE 
    EXTRACT(DAY FROM capture_date) = 10
ORDER BY 
    capture_date DESC;
--------------------------------


