SELECT * FROM authors

SELECT * FROM books

SELECT * FROM triangles
-- Write a query to find all books whose titles start with "The".
-- Order the result by id. 
SELECT title FROM books
WHERE SUBSTRING(title, 1, 3) = 'The'
ORDER BY id; -- This is not needed

SELECT title FROM books
WHERE LEFT(title, 3) = 'The';
-- Write a query to find all books, whose titles start with "The" and replace the substring with 3 asterisks.
-- Retrieve data about the updated titles.
-- Order the result by id.

SELECT REPLACE(title, 'The', '***') AS "Title"
FROM books
WHERE LEFT(title, 3) = 'The'
ORDER BY id;

SELECT REPLACE(title, 'The', '***') AS "Title"
FROM books
WHERE SUBSTRING(title, 1, 3) = 'The';

SELECT * FROM authors
CREATE TABLE full_name AS
SELECT concat(first_name, ' ' , last_name)
FROM authors;

SELECT * FROM full_name
ALTER TABLE full_name
RENAME COLUMN concat to "Full Name";

SELECT 
	"Full Name",
	LEFT("Full Name", position(' ' in "Full Name")) AS first_name,
	RIGHT("Full Name", length("Full Name") - position(' ' in "Full Name")) AS last_name,
	SUBSTRING("Full Name", 1, position(' ' in "Full Name")) AS first_name,
	SUBSTRING("Full Name", position(' ' in "Full Name"), length("Full Name")) AS last_name
FROM full_name;

SELECT * FROM books
SELECT 
	id,
	id / 2,
	id::FLOAT / 2, -- кастване към друг формат
	CAST(id AS FLOAT) / 2
FROM books

SELECT * FROM triangles
/*Write a query to calculate the area of triangles with a given side and height from table triangles.
-	Display the resulting table with columns id and area. Order by id.
*/
SELECT 
	id,
	side * height / 2 AS area
FROM triangles
/*Write a query to get each book’s title and cost (cost as modified_price)
and format the output to 3 digits after the decimal point. Order by id. */
SELECT 
	title,
	trunc(cost, 3) AS modified_price
FROM books

SELECT EXTRACT('year' FROM NOW())
SELECT EXTRACT('month' FROM NOW())
SELECT EXTRACT('day' FROM NOW())

SELECT DATE_PART('year', now())
SELECT DATE_PART('month', now())
SELECT DATE_PART('day', now())
SELECT DATE_PART('hour', now())
SELECT DATE_PART('minute', now())

SELECT AGE(NOW(), '2020-01-01')

DO $$
	DECLARE
	time_1 TIMESTAMP := '2021-01-02:12:20';
	time_2 TIMESTAMP := NOW();
	time_3 INTERVAL;
	BEGIN
		time_3 := time_2 - time_1;
		RAISE NOTICE 'The difference is %', time_3;
	END;
$$
/*
Write a query to get the year of birth for each author. Your query should return:
-	first_name – the first name of each author
-	last_name – the last name of each author
-	year – the year of birth of each author
*/
SELECT
	first_name,
	last_name,
	EXTRACT('year' FROM born)
FROM authors

SELECT
	first_name,
	last_name,
	age(died, born)
FROM authors
WHERE died IS NOT NULL

SELECT CURRENT_DATE;
SELECT CURRENT_TIME;

SELECT NOW()
SELECT TO_CHAR(NOW(), 'DD Month YYYY') AS "Date";

/*
Write a query to display the author’s last name and date of birth in the format 15 (Mon) Sep 1890. 
-	use date format: DD (Dy) Mon YYYY
-	born field(formatted) as Date of Birth
-	last_name as Last Name
*/
SELECT
	last_name,
	TO_CHAR(born, 'DD (Dy) Mon YYYY') AS "Date of Birth"
FROM authors

--Write a query to retrieve the titles of all Harry Potter books.
--Order the information by id.
SELECT
	title
FROM books
WHERE title like '%Harry Potter%'

-- Summary
-- String Functions – manipulating text
/*
SUBSTRING(string, position, length: optional) - String from Position for Length, също може да бъде използван за това дали един стринг е събстринг на друг.
REPLACE(string, string to replace, to replace with) - case sensitive
LTRIM, RTRIM - маха празни разстояния от ляво и от дясно
нямаме полза да пазим празни места;
можем да изтриваме и определен символ;
ще изтриваме всеки символ докато не намерим различен от този, който търсим.
CHAR_LENGTH - STRING LENGTH;
LENGTH - Връща дължината на един стринг.
BIT_LENGTH - Всеки символ от ascii таблицата е 8 байтa, за останалите зависи от encoding-a => "café" => c - 1byte, a - 8bits, f - 1byte, é - 16 bits;
LEFT, RIGHT, (string count)- вземат n на брой елементи, ляво и дясно; можем да подаваме отрицателни стойности и по този начин да взимаме всико без последните n елементи.
LOWER, UPPER, (string)
REVERSE, (string)
REPEAT, (string, count)
INSERT(String, Position, chars count to delete, sub string)
POSITION - ex. POSITION('b' IN some_field) - връща индекса, на който е намерило въпросната стойност.
*/

-- Math Functions – calculations and working with aggregate data
/*
/, -, *, +
АBS
PI
SELECT PI() AS pi_value;
SQRT (NUMBER)
POW (NUMBER, POWER) - степенуване
ROUND - UP >= 5 DOWN 4 <= - (NUMBER, PERCISION)
FLOOR, CEIL
SIGN(NUMBER) - връща знака като 1, -1 или 0
RANDOM() - връща число между 0 и 1
SELECT CEIL(RANDOM() * 100) % 7 AS random_mod_7; връща число между 0 и 6;
*/

-- Date/Time Functions - e.g., compute the length of a time span
/*EXTRACT (PART FROM DATE) - PART - YEAR, MONTH, DAY, MINUTES...
AGE() - връща разликата между две дати
TO_CHAR()
TO_CHAR(NOW() AT TIME ZONE 'UTC', 'YYYY-MM-DD HH24:MI:SS TZD');
Резултат '2023-09-20 12:34:56 UTC'
*/

-- WILD_CARDS
/*
LIKE() - подобно на регекс търси дали нещо започва/завършва или двете едновременно на някакъв string/pattern
% означава 0 или повече символи преди/след string-a
_ е за попълване на точна позиция
REGEXP
*/

-- A great variety of Other Functions have a look at the official documentation https://www.postgresql.org/docs/15/functions.html