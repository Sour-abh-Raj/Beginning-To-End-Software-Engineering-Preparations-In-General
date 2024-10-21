-- https://leetcode.com/problems/monthly-transactions-i/description/?envType=study-plan-v2&envId=top-sql-50

SELECT
DATE_FORMAT(trans_date, '%Y-%m') AS month,
country,
COUNT(id) AS trans_count,
SUM(state = 'approved') AS approved_count, 
SUM(amount) AS trans_total_amount,
SUM(IF(state = 'approved' ,amount, 0)) AS approved_total_amount
FROM Transactions
GROUP BY 1, 2
ORDER BY 1, 2 ASC;

SELECT
LEFT(trans_date, 7) AS month,
country,
COUNT(id) AS trans_count,
SUM(state = 'approved') AS approved_count, 
SUM(amount) AS trans_total_amount,
SUM((state = 'approved') * amount) AS approved_total_amount
FROM Transactions
GROUP BY month, country
ORDER BY month, country ASC;