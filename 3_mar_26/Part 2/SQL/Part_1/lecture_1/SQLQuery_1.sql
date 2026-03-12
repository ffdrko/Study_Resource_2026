-- Find the total score and total number of customers for each count
SELECT 
country,
SUM(score) AS total_score,
COUNT(id) AS total_num_of_cus
FROM customers
GROUP BY country
ORDER BY total_score ASC