-- Find the total score for each country
SELECT 
country,
SUM(score) AS score
FROM customers
GROUP BY country