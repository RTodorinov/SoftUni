SELECT
	id,
	CONCAT_WS(' ',number,street) AS address,
	city_id
FROM addresses
WHERE id >= 20;

SELECT
	id,
	CONCAT_WS(
		' ',
		number,
		street
	) AS address,
	city_id
FROM 
	addresses
WHERE
	id >= 20;
