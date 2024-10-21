# Write your MySQL query statement below
-- https://leetcode.com/problems/queries-quality-and-percentage/?envType=study-plan-v2&envId=top-sql-50

SELECT query_name, ROUND(
    AVG(rating / position), 2
) AS quality, ROUND(
    AVG(rating < 3) * 100, 2) AS poor_query_percentage
FROM Queries
WHERE query_name IS NOT NULL
GROUP BY query_name
ORDER BY query_name ASC;

-- SELECT query_name, ROUND(
--     -- AVG(CAST(rating AS DECIMAL) / position), 2
--     -- Casting to decimal is not necessary since the division will return a decimal.
--     -- But it's done to avoid any potential issues with integer division.
--     AVG(rating / position), 2
-- ) AS quality, ROUND(
--     SUM(CASE
--     WHEN rating < 3 THEN
--     1 ELSE 0
--     END) * 100 / COUNT(rating), 2) AS poor_query_percentage
-- FROM Queries
-- WHERE query_name IS NOT NULL
-- GROUP BY query_name
-- ORDER BY query_name ASC;
