SELECT 
country,
SUM(score)
FROM customers
GROUP BY country