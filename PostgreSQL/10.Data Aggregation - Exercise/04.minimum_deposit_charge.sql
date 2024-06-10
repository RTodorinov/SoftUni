SELECT 
	MIN(deposit_charge) AS minimum_deposit_charge
FROM 
	wizard_deposits;

SELECT 
	MIN(deposit_charge) AS "Minimum Deposit Charge"
FROM 
	wizard_deposits;

SELECT
	deposit_charge as minimum_deposit_charge
FROM wizard_deposits
ORDER BY eposit_charge DESC
LIMIT 1;