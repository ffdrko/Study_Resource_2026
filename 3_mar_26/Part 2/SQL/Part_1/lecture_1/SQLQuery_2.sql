/* Find the average score for each country considering only customwes with 
a score not equal to 0 and return only those countries with an average 
score greater tham 430 */
SELECT 
country,
AVG(score) AS average_Score
FROM customers
WHERE score !=0
GROUP BY country
HAVING AVG(SCORE) > 430