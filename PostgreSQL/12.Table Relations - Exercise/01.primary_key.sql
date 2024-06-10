CREATE TABLE products (
	product_name VARCHAR(100)	
);
	
INSERT INTO products
VALUES
	('Broccoli'),
	('Shampoo'),
	('Toothpaste'),
	('Candy');

ALTER TABLE products
ADD COLUMN "id" SERIAL PRIMARY KEY;
-------------------------------------- създаване на PK с CONSTRAINT и собствено име 
CREATE TABLE products (
	id SERIAL
	product_name VARCHAR(100)
	CONSTRAINT products_custom_name_pkey PRIMARY KEY (id)
);

INSERT INTO 
	products
VALUES 
	('Broccoli'),
	('Shampoo'),
	('Toothpaste'),
	('Candy');
