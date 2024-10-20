-- https://leetcode.com/problems/confirmation-rate/?envType=study-plan-v2&envId=top-sql-50

SELECT s.user_id,
CASE WHEN c.action IS NULL THEN 0
ELSE ROUND(AVG(IF(c.action = 'confirmed', 1, 0)), 2) END AS confirmation_rate
FROM Signups s LEFT JOIN Confirmations c USING(user_id)
GROUP BY s.user_id
ORDER BY s.user_id ASC;

-- SELECT s.user_id,
-- CASE WHEN c.action IS NULL THEN 0
-- ELSE ROUND(SUM(c.action = 'confirmed') / COUNT(c.action), 2) END AS confirmation_rate
-- FROM Signups s LEFT JOIN Confirmations c USING(user_id)
-- GROUP BY s.user_id
-- ORDER BY s.user_id ASC;