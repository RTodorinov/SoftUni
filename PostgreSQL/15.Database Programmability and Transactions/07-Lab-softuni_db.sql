/*
User-Defined Functions
▪ Extend the functionality of a PostgreSQL
▪ Write it once, call it any number of times
▪ Can be customized to fit specific requirements
▪ Break out complex logic into shorter code blocks
▪ Functions can be:
▪ Scalar - returning a single value or NULL
▪ Table-valued - returning a table

User-Defined Functions Syntax

CREATE [OR REPLACE] FUNCTION function_name (arguments)
RETURNS return_datatype
AS $variable_name$
	DECLARE
		declaration;
		[...]
	BEGIN
		< function_body >
		[.. logic]
		RETURN { variable_name | value }
	END;
$variable_name$
LANGUAGE language_name;

*/

CREATE OR REPLACE FUNCTION fn_full_name(VARCHAR, VARCHAR)
RETURNS VARCHAR AS -- казваме какъв тип данни ще върне функцията
$$
	BEGIN
		RETURN CONCAT('Hello ', $1, ' ', $2); -- тук връща резултата
	END;
$$
LANGUAGE plpgsql
;

SELECT * FROM fn_full_name('Rosen', 'Bokov')
--------------------------------------------------------
CREATE OR REPLACE FUNCTION fn_full_name1(VARCHAR, VARCHAR)
RETURNS VARCHAR AS -- казваме какъв тип данни ще върне функцията
$$
	DECLARE -- декларираме променливите
		first_name ALIAS FOR $1;
		last_name ALIAS FOR $2;
		greeting VARCHAR;
	BEGIN
		greeting := 'Hello';
		RETURN CONCAT(greeting, ' ', first_name, ' ', last_name); -- тук връща резултата
	END;
$$
LANGUAGE plpgsql
;

SELECT * FROM fn_full_name1('Rosen', 'Chokov')
--------------------------------------------------
CREATE OR REPLACE FUNCTION fn_get_name_len(name VARCHAR)
RETURNS INT AS -- казваме какъв тип данни ще върне функцията
$$
	BEGIN
		RETURN LENGTH(name); -- тук връща резултата
	END;
$$
LANGUAGE plpgsql
;

SELECT * FROM fn_get_name_len('Rosen')
--------------------------------------------------
CREATE OR REPLACE FUNCTION fn_full_name2(first_name VARCHAR, last_name VARCHAR)
RETURNS VARCHAR AS 
$$
	DECLARE
		full_name VARCHAR(30);
	BEGIN
		IF first_name IS NULL AND last_name IS NULL THEN
			full_name := NULL;
		ELSEIF first_name IS NULL THEN
			full_name := last_name;
		ELSEIF last_name IS NULL THEN
			full_name := first_name;
		ELSE
			full_name := CONCAT(first_name, ' ', last_name);
		END IF;
		RETURN full_name;
	END
$$
LANGUAGE plpgsql
;

SELECT * FROM fn_full_name2('Rosen','')
SELECT * FROM fn_full_name2('','Bokov')
SELECT * FROM fn_full_name2('null','null')
SELECT * FROM fn_full_name2('Rosen','Bokov')
SELECT * FROM fn_full_name2('','')
-----------------------------------------------------
-- da se dopishe
CREATE OR REPLACE FUNCTION fn_full_name3(first_name VARCHAR, last_name VARCHAR)
RETURNS VARCHAR AS 
$$
	DECLARE
		full_name VARCHAR(30);
	BEGIN
		IF first_name IS NULL AND last_name IS NULL THEN
			full_name := NULL;
		ELSEIF first_name IS NULL THEN
			full_name := last_name;
		ELSEIF last_name IS NULL THEN
			full_name := first_name;
		ELSE
			full_name := fn_full_name('Rosen', 'Bokov');
		END IF;
		RETURN full_name;
	END
$$
LANGUAGE plpgsql
;

SELECT * FROM fn_full_name3('Rosen','')
SELECT * FROM fn_full_name3('','Bokov')
SELECT * FROM fn_full_name3('','')
SELECT * FROM fn_full_name3('Rosen','Bokov')
---------------------------------------------------------
	/*this is with other database: subqueries_joins_geography_db*/
CREATE OR REPLACE FUNCTION fn_get_city_id(city VARCHAR)
RETURNS INT AS
$$
	DECLARE
		city_id INT;
	BEGIN
		SELECT id FROM countries WHERE country_name = city INTO city_id;
		RETURN city_id;
	END;
$$
LANGUAGE plpgsql;


SELECT * FROM fn_get_city_id('Germany');

SELECT
	id,
	country_name
FROM countries
ORDER BY countries;
------------------------------------------------
CREATE OR REPLACE FUNCTION fn_get_city_id1(IN city_name VARCHAR, OUT city_id INT)
AS
$$
	BEGIN
		SELECT id FROM countries WHERE lower(country_name) = lower(city_name) INTO city_id;
	END;
$$
LANGUAGE plpgsql;

SELECT fn_get_city_id1('Bulgaria');
SELECT fn_get_city_id1('BULGARIA');
---------------------------------------------
-- обратно към база soft_uni
-- Задача 1
CREATE OR REPLACE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20)) 
RETURNS INT AS
$$
	DECLARE
		town_count INT;
	BEGIN
		SELECT
			COUNT(*) INTO town_count
		FROM 
			employees AS e
				JOIN addresses AS a
					USING(address_id)
				JOIN towns AS t
					USING(town_id)
		WHERE t.name = town_name;
		RETURN town_count;
	END;
$$
LANGUAGE plpgsql;
-------------------------------------------
CREATE FUNCTION fn_count_employees_by_town(town_name VARCHAR(20))
RETURNS INT
AS $$
	DECLARE e_count INT;
	BEGIN
		SELECT COUNT(employee_id) INTO e_count
		FROM employees AS e
			JOIN addresses AS a ON a.address_id = e.address_id
				JOIN towns AS t ON t.town_id = a.town_id
					WHERE t.name = town_name;
		RETURN e_count;
	END;
$$ 
LANGUAGE plpgsql;

SELECT fn_count_employees_by_town('Sofia') AS count;
SELECT fn_count_employees_by_town('Berlin') AS count;
SELECT fn_count_employees_by_town(NULL) AS count;
-------------------------------------------
--използване на функция за инсъртване на данни

CREATE OR REPLACE FUNCTION fn_insert_data(town_id INT, name VARCHAR)
RETURNS BOOLEAN AS
$$
	DECLARE
	BEGIN
		INSERT INTO towns(town_id, name)
		VALUES (town_id, name);
		EXCEPTION 
			WHEN UNIQUE_VIOLATION THEN RETURN FALSE;
		RETURN TRUE;
	END;
$$
LANGUAGE plpgsql
;

SELECT fn_insert_data(33, 'Plovdiv')

SELECT * FROM towns;
---------------------------------------------------------------
-- използване на функция за връщане на таблица

CREATE OR REPLACE FUNCTION fn_get_towns()
RETURNS TABLE (town_id INT, name VARCHAR) AS
$$
	BEGIN
		RETURN QUERY (SELECT * FROM towns);
	END;
$$
LANGUAGE plpgsql
;

SELECT * FROM fn_get_towns()
--------------------------------------------
CREATE OR REPLACE PROCEDURE sp_increase_salaries(department_name VARCHAR) 
AS
$$
	BEGIN
		UPDATE employees
		SET salary = salary + salary * 0.05
		WHERE department_id = (SELECT department_id FROM departments WHERE name = department_name);
	END;
$$
LANGUAGE plpgsql;

CALL sp_increase_salaries('Marketing') -- извикване на функцията
--------------------------------------
-- проверка на кода

CREATE OR REPLACE FUNCTION fn_show_notice(msg VARCHAR(40))
RETURNS BOOL AS
$$
	BEGIN
		RAISE NOTICE 'The notice is %', msg; -- заменяме с някаква променлива за да видим какво става с нея
		RETURN TRUE;
	END;
$$
LANGUAGE plpgsql;

SELECT fn_show_notice('Hello Notice')
---------------------------------------------------
BEGIN; 
INSERT INTO towns(town_id, name)
VALUES (34, 'Varna');
ROLLBACK -- Връща направените промени
COMMIT -- Запазва промените
----------------------------------------
-------- не е сигурно че работи примера отдолу
CREATE OR REPLACE PROCEDURE st_transfer_money(  -- процедура за прехвърляне на пари 
	IN sender_id INT,
	IN receiver_id INT,
	IN transfer_amount INT,
	OUT status VARCHAR(30)
)
AS
$$
	DECLARE
		sender_amount INT;
		receiver_amount INT;
		temp_val INT;
	BEGIN
		SELECT amount FROM bank WHERE id = sender_id INTO sender_amount;
		IF sender_amount < transfer_amount THEN
			status := 'Not enough money';
			RETURN;
		END IF;
		SELECT amount FROM bank WHERE id = receiver_id INTO receiver_amount;
		UPDATE bank SET amount = amount - transfer_amount WHERE id = sender_id;
		UPDATE bank SET amount = amount + transfer_amount WHERE id = receiver_id;

		SELECT amount FROM bank WHERE id = sender_id INTO temp_val;
		IF sender_amount - transfer_amount <> temp_val THEN
			status := 'Error in sender';
			ROLLBACK;
			RETURN;
		END IF;

		SELECT amount FROM bank WHERE id = receiver_id INTO temp_val;
		IF receiver_amount + transfer_amount <> temp_val THEN
			status := 'Error in receiver';
			ROLLBACK;
			RETURN;
		END IF;
		status := 'Money transferred';
		COMMIT;
	END;
$$
LANGUAGE plpgsql;

CALL st_transfer_money(1, 2, 400, NULL)
----------------------------------------------------------
/*
Stored Procedures
Stored procedures allow some part of the logic to be removed
from the application and stored in the RDBMS
▪ Can significantly cut down traffic on the network
▪ Improve the security of the database
▪ Encapsulate complex operations and logic, making it easier to
manage and maintain the code
▪ Stored procedures can be accessed by programs using different
platforms and APIs

Creating Stored Procedures:

CREATE PROCEDURE sp_employees_count_by_work_experience()
AS 
$$
	DECLARE employees_count INT;
	BEGIN
		SELECT COUNT(employee_id) INTO employees_count
		FROM employees
		WHERE DATE_PART('year', AGE(NOW(), hire_date)) < 18;
		RAISE NOTICE 'Employees count: %', employees_count;
	END; 
$$
LANGUAGE plpgsql;

CALL sp_employees_count_by_work_experience();
DROP PROCEDURE sp_employees_count_by_work_experience;

Parameterized Stored Procedures – Example

CREATE PROCEDURE sp_select_employees_by_experience(min_years_at_work INT)
AS 
$$
	DECLARE
		employee_count INT;
	BEGIN
		SELECT COUNT(employee_id) INTO employee_count FROM employees
		WHERE date_part('year', age(now(), hire_date)) > min_years_at_work;
		RAISE NOTICE '%', employee_count;
	END;
$$
LANGUAGE plpgsql;

CALL sp_select_employees_by_experience(23);
*/
--------------------------------------------------------------
CREATE PROCEDURE sp_increase_salaries(department_name varchar(50))
LANGUAGE plpgsql
AS 
$$
	BEGIN
		UPDATE employees AS e
		SET salary = salary * 1.05
		WHERE e.department_id = (
		SELECT department_id FROM departments WHERE name = department_name);
	END; 
$$;

CALL sp_increase_salaries('Sales');
--------------------------------------------------------------
/*
Transactions
Transaction is a sequence of actions (database operations)
executed as a whole
▪ Either all of them succeed or fail as a whole
▪ Example of transaction
▪ A bank transfer from one account to another
(withdrawal & deposit operations)
▪ If either the withdrawal or the deposit operation fails
the whole set of operations is canceled
Transactions guarantee consistency and the integrity
of the database
▪ All changes within a transaction are temporary
▪ Changes persist when COMMIT is executed
▪ At any time, all changes can be canceled by ROLLBACK
▪ All operations are executed as a whole
Transactions Syntax:

-- start a transaction
BEGIN;
-- make a sequence of actions
-- roll back the transaction
ROLLBACK;
-- commit the change
COMMIT;

-- start a transaction
BEGIN;
-- make a sequence of actions
-- create a save point
SAVEPOINT my_savepoint;
-- roll back the transaction
ROLLBACK TO my_savepoint;
-- commit the change
COMMIT;

*/

CREATE OR REPLACE PROCEDURE sp_increase_salary_by_id(id INT) 
AS
$$
	BEGIN
		IF (SELECT salary FROM employees WHERE employee_id = id) IS NULL THEN
			RETURN;
		END IF;
		UPDATE employees SET salary = salary * 1.05 WHERE employee_id = id;
		COMMIT;
	END;
$$
LANGUAGE plpgsql;
--------------------------------------------
CREATE PROCEDURE sp_increase_salary_by_id(id INT)
LANGUAGE plpgsql
AS 
$$
	BEGIN
		IF (SELECT COUNT(employee_id) FROM employees WHERE employee_id = id) != 1 THEN
		ROLLBACK;
		ELSE
		UPDATE employees SET salary = salary * 1.05 WHERE employee_id = id;
		END IF;
		COMMIT;
	END; 
$$;
-----------------------------------------------
/*
What Are Triggers in PostgreSQL?
Triggers - special user-defined functions invoked automatically
whenever an event associated with a table occurs
▪ UPDATE, DELETE, INSERT, or TRUNCATE
▪ We do not call triggers explicitly
▪ Triggers are attached to a table
▪ PostgreSQL supports row-level and statement-level triggers

Types of Triggers:
BEFORE -> TRIGER -> EVENT
AFTER -> TRIGER -> EVENT
*/

CREATE TABLE items(   -- създаване на тестова таблица
	id SERIAL PRIMARY KEY,
	status INT,
	created DATE
);
CREATE TABLE items_log( -- създаване на копие на тестовата която да пази последните промени
	id SERIAL PRIMARY KEY,
	status INT,
	created DATE
);

CREATE FUNCTION log_items() -- Създаване на функция която да записва новите промени в лог таблицата
RETURNS TRIGGER             -- за да следим оригиналната таблица какво е променяно
AS
$$
	BEGIN
		INSERT INTO items_log (status, created)
		VALUES (new.status, new.created);
		RETURN new;
	END;
$$
LANGUAGE plpgsql;

CREATE TRIGGER log_items_trigger -- създаване на тригер който да вика горната функция при всяка промяна 
AFTER INSERT on items            -- на запис за а може да се отрази в лог таблицата
FOR EACH ROW
EXECUTE PROCEDURE log_items();

INSERT INTO items (status, created) -- вкарване на тестови данни
VALUES
	(1, now()),
	(2, now()),
	(3, now()),
	(4, now()),
	(5, now()),
	(6, now());

SELECT * FROM items
SELECT * FROM items_log

-----------------------------
------------------ изтриване на най старите записи чрез тригер

CREATE OR REPLACE FUNCTION delete_last_items_log() -- създаваме функция за триене на последните записи от лога
RETURNS TRIGGER
AS
$$
	BEGIN
		WHILE (SELECT count(*) FROM items_log) > 10 LOOP
			DELETE FROM items_log WHERE id= (SELECT min(id) FROM items_log);
		END LOOP;
		RETURN new;
	END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER clear_items_log_triger -- създаване на тригер на функцията 
AFTER INSERT ON items_log
FOR EACH STATEMENT
EXECUTE PROCEDURE delete_last_items_log();

INSERT INTO items (status, created) -- слагаме още тестови данни
VALUES
	(7, now()),
	(8, now()),
	(9, now()),
	(10, now()),
	(11, now()),
	(12, now());

SELECT * FROM items
SELECT * FROM items_log  -- проверяваме дали тригера чисти последните записи така че да остават само последните 10
--------------------------------------------------------------------------------

CREATE TABLE deleted_employees(
	employee_id SERIAL PRIMARY KEY,
	first_name VARCHAR(20),
	last_name VARCHAR(20),
	middle_name VARCHAR(20),
	job_title VARCHAR(50),
	department_id INT,
	salary NUMERIC (19, 4)
);

CREATE OR REPLACE FUNCTION backup_fired_employees()
RETURNS TRIGGER
AS
$$
	BEGIN
		INSERT INTO deleted_employees(
			first_name, last_name, middle_name, job_title, department_id, salary
		)
		VALUES (
			old.first_name,
			old.last_name,
			old.middle_name,
			old.job_title,
			old.department_id,
			old.salary
		);
		RETURN new;
	END;
$$
LANGUAGE plpgsql;

CREATE OR REPLACE TRIGGER backup_employees
AFTER DELETE ON employees
FOR EACH ROW
EXECUTE PROCEDURE backup_fired_employees();

/*
Summary:
▪ We can optimize our code with
user-defined Functions
▪ Stored Procedures encapsulate sets of query
statements and logic
▪ Transactions improve security and consistency
▪ Triggers execute before or after certain events
on tables
*/