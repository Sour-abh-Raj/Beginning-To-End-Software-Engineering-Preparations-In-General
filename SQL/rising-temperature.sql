-- https://leetcode.com/problems/rising-temperature/?envType=study-plan-v2&envId=top-sql-50

SELECT today.id
FROM Weather today
INNER JOIN Weather yesterday
ON DATE_SUB(today.recordDate, INTERVAL 1 DAY) = yesterday.recordDate
WHERE yesterday.temperature < today.temperature
ORDER BY today.id ASC;

-- SELECT today.id
-- FROM Weather yesterday 
-- CROSS JOIN Weather today

-- WHERE DATEDIFF(today.recordDate,yesterday.recordDate) = 1
--     AND today.temperature > yesterday.temperature
-- ;