/*
Как се създават Базите
1.Без повторения на данните 
2.Уникални идентификатори Defining PRIMARY keys 
3.NULL само ако е наложително
4.Интеграция на референции RELATIONS : Modeling
relationships, Defining constraints
5.Атомик дата - в една колона трябва да има само един тип данни
6.Правилен подбор на данни Identification of
the entities, Defining table columns
7.Индексация - начина на търсене по PRIMARY KEY но има възможност и по 
друго ентити.
8.Аксес контрол - кой какви права да има
9.Filling test data
*/
-- examples: remove long names and change it to strings
UPDATE persons
SET country =
CASE country
	WHEN 'Greece' THEN '1'
	WHEN 'Italy' THEN '2'
	WHEN 'England' THEN '3'
	WHEN 'Bulgaria' THEN '4'
END;
-- change strings to integers in column country
ALTER TABLE persons
ALTER COLUMN country TYPE INTEGER USING country::integer
-- change name of column country
ALTER TABLE persons
RENAME COLUMN country TO country_id
--we create foreign key from persons to country table
ALTER TABLE persons
ADD CONSTRAINT fk_persons_country
	FOREIGN KEY (country_id)
	REFERENCES country(id)
-- gat all the data from two tables
SELECT * FROM persons AS p
	JOIN country AS c ON p.country_id = c.id
-- now we can change only one piece of DATA
UPDATE country
SET country_name = 'Elada'
WHERE country_name = 'Greece'

/*
How to Choose a Primary Key?
▪ Always define an additional column for the
primary key
▪ Don't use an existing column (for example "name")
▪ Can be an integer number
▪ Must be declared as a PRIMARY KEY
▪ Put the primary key in a first column
▪ Exceptions
▪ Entities that have well-known ID, e.g., countries (BG,
DE, US) and currencies (USD, EUR, BGN)
*/
-- Relationships between tables are based on interconnections: PRIMARY KEY / FOREIGN KEY
-- Таблицата с PRYMARY KEY e parrent а таблицата с FOREIGN KEY e винаги chield.
/* 
Primary Key Implementation
Primary Key: id INT PRIMARY KEY - трябва ръчно да му подаваме следващия PK при нов запис
Auto-increment: id SERIAL PRIMARY KEY - автоматично дава следващ номер но има проблем ако му подадем ръчно
Auto-increment always (cannot provide an explicit value):id INT GENERATED ALWAYS AS IDENTITY - автоматично генерира PK и не можем да пипаме ръчно
Auto-increment (cannot guarantee uniqueness):id INT GENERATED BY DEFAULT AS IDENTITY -
*/
/*
The foreign key is an identifier of a record located in
another table (usually its primary key)
▪ By using relationships, we avoid repeating data in
the database
▪ Relationships have multiplicity:
▪ One-to-many – e.g., mountain / peaks
▪ Many-to-many – e.g., students / courses
▪ One-to-one – e.g., country / capital
*/
-- ONE to MANY methods:
-- method one
CREATE TABLE mountains(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50)
);

CREATE TABLE peaks(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	mountain_id INT
);

ALTER TABLE peaks	
ADD CONSTRAINT fk_peaks_mountains
	FOREIGN KEY (mountain_id)
	REFERENCES mountains(id);

SELECT * FROM peaks

DROP TABLE mountains, peaks

--method two
CREATE TABLE mountains(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50)
);

CREATE TABLE peaks(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	mountain_id INT, 
CONSTRAINT fk_peaks_mountains
	FOREIGN KEY (mountain_id)
	REFERENCES mountains(id)
);

DROP TABLE mountains, peaks
--method three without CONSTRAINT
CREATE TABLE mountains(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50)
);

CREATE TABLE peaks(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50),
	mountain_id INT REFERENCES mountains(id)
);
-- method with incremented unique PK that can't be changed
CREATE TABLE mountains(
	id INT GENERATED ALWAYS AS IDENTITY UNIQUE,
	name VARCHAR(50) NOT NULL
);
CREATE TABLE peaks(
	id INT GENERATED ALWAYS AS IDENTITY UNIQUE,
	name VARCHAR(50) NOT NULL,
	mountain_id INT,
CONSTRAINT fk_peaks_mountains
	FOREIGN KEY (mountain_id)
	REFERENCES mountains(id)
);
-- MANY to MANY methods
-- method one
CREATE TABLE men(
	id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name VARCHAR(20)
);

CREATE TABLE women(
	id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
	name VARCHAR(20)
);

CREATE TABLE men_women(
	men_id INT REFERENCES men(id),  -- създаваме FOREIGN KEY насочен към таблицата men
	women_id INT REFERENCES women(id), -- създаваме FOREIGN KEY насочен към таблицата women
	CONSTRAINT pk_men_women -- Правим задължителен констрайнт който казва 
		PRIMARY KEY (men_id, women_id) -- че е композитен PK с комбинация men_id и women_id
);
-- добавяме тестови данни в таблиците
INSERT INTO men(name)
VALUES
	('Kiko')
	('Miko')
	('Tiko')
	('Diko')

INSERT INTO women(name)
VALUES
	('Mitka')
	('Ditka')
	('Pitka')
	('Vitka')

SELECT * FROM men
SELECT * FROM women
-- създаваме връзките коя жена с кой мъж е  
INSERT INTO men_women(men_id, women_id)
VALUES 
	(1, 1)
	(1, 2)
	(2, 1)
	(2, 3)
	(2, 4)
	(3, 2)
	(3, 3)
	(4, 1)
	(4, 4)

SELECT * FROM men_women
-- изваждане на данните кой с кого
SELECT * FROM men AS m
	JOIN men_women AS mw 
		ON m.id = mw.men_id
    JOIN women AS w 
		ON	mw.women_id = w.id
-- когато ползваме JOIN не създаваме нова таблица
-- нещо като VIEW
SELECT
	m.name,
	w.name
FROM men AS m
	JOIN men_women AS mw 
		ON m.id = mw.men_id
    JOIN women AS w 
		ON	mw.women_id = w.id
-- method two
CREATE TABLE employees(
	id SERIAL PRIMARY KEY,
	employee_name VARCHAR(50)
);

CREATE TABLE projects(
	id SERIAL PRIMARY KEY,
	project_name VARCHAR(50)
);

CREATE TABLE employees_projects(
	employee_id INT,
	project_id INT,
	CONSTRAINT pk_employees_projects -- PK
		PRIMARY KEY(employee_id, project_id),
	CONSTRAINT fk_employees_projects_employees -- FK
		FOREIGN KEY(employee_id)
		REFERENCES employees(id),
	CONSTRAINT fk_employees_projects_projects -- FK
		FOREIGN KEY(project_id)
		REFERENCES projects(id)
);
-- ONE to ONE methods
-- method one
CREATE TABLE capitals(
	capital_id SERIAL PRIMARY KEY, -- PK
	capital_name VARCHAR(50)
);
CREATE TABLE countries(
	country_id SERIAL PRIMARY KEY,
	capital_id INT UNIQUE, -- Задължително условие FK да е UNIQUE
	CONSTRAINT fk_countries_capitals FOREIGN KEY
	(capital_id) REFERENCES capitals(capital_id)
);
/*
Joins
Table relations are useful when combined with JOINS
▪ With JOINS we can get data from two tables simultaneously
▪ By pointing a "join condition"
▪ Example:
SELECT * FROM table_a
	JOIN table_b ON
		table_b.common_column = table_a.common_column
*/

SELECT 
	driver_id, 
	vehicle_type,
	CONCAT(first_name, ' ', last_name) AS driver_name
FROM vehicles AS v
JOIN campers AS c
	ON v.driver_id = c.id;

SELECT 
	v.driver_id, 
	v.vehicle_type,
	CONCAT(c.first_name, ' ', c.last_name) AS driver_name
FROM vehicles AS v
JOIN campers AS c -- създаваме временна таблица по долните условия
	ON v.driver_id = c.id;

SELECT 
	start_point, 
	end_point,
	leader_id,
	CONCAT(c.first_name, ' ', c.last_name) AS leader_name
FROM routes AS r
JOIN campers AS c
	ON r.leader_id = c.id;
-- Cascade Operations
/*
CASCADE allows changes made to a specific entity to be applied
to all related entities
CASCADE DELETE
CASCADE can be either DELETE or UPDATE
▪ Use CASCADE DELETE when:
▪ The related entities are meaningless without the
"main" one
▪ Do not use CASCADE DELETE when:
▪ You make "logical delete"
▪ You preserve history
▪ Keep in mind that in more complicated relations it
won't work with circular references
*/
-- Example: 
CREATE TABLE drivers(
	driver_id INT PRIMARY KEY,
	driver_name VARCHAR(50)
);
CREATE TABLE cars(
	car_id INT PRIMARY KEY,
	driver_id INT,
	CONSTRAINT fk_car_driver FOREIGN KEY(driver_id)
	REFERENCES drivers(driver_id) ON DELETE CASCADE -- Foreign Key with Cascade Delete
);

CREATE TABLE mountains(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL
);

CREATE TABLE peaks(
	id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	mountain_id INT, 
CONSTRAINT fk_mountain_id
	FOREIGN KEY (mountain_id)
	REFERENCES mountains(id) ON DELETE CASCADE
);
/*
CASCADE UPDATE
Use when:
▪ The primary key is NOT auto-incremented and
therefore it can be changed
▪ Best used with the UNIQUE constraint
▪ Do not use when:
▪ The primary key is auto-incremented
▪ Avoid cascading updates by using triggers
or procedures
*/
-- Foreign Key Update Cascade
CREATE TABLE drivers(
driver_id INT PRIMARY KEY,
driver_name VARCHAR(50)
);
CREATE TABLE cars(
car_id INT PRIMARY KEY,
driver_id INT,
CONSTRAINT fk_car_driver FOREIGN KEY(driver_id)
REFERENCES drivers(driver_id) ON UPDATE CASCADE -- Foreign Key Update Cascade
);
/*
E/R Diagrams
Entity / Relationship Diagrams

▪ Relational schema of a DB is a collection of:
▪ The schemas of all tables
▪ Relationships between tables
▪ Any other database objects (e.g., constraints)
▪ The relational schema describes the structure of
the database
▪ Does not contain data, but metadata
▪ Relational schemas are graphically displayed in Entity
/ Relationship diagrams (E/R Diagrams)
*/