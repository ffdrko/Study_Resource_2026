/* Customers from a Specific Country  
Retrieve the first name and last name 
of customers who live in United States from DimCustomer */
SELECT FirstName, LastName
FROM DimCustomer
WHERE Gender = 'M'