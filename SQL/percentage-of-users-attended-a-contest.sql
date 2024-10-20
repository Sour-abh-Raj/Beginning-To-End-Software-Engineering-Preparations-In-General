-- https://leetcode.com/problems/percentage-of-users-attended-a-contest/solutions/3789653/sql-subquery-group-by-order-by-easy-to-understand/?envType=study-plan-v2&envId=top-sql-50

SELECT 
    contest_id, 
    ROUND(COUNT(DISTINCT user_id) * 100 / (SELECT COUNT(user_id) FROM Users), 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;

-- SELECT 
--     r.contest_id, 
--     ROUND(
--         COUNT(r.user_id) * 100.0 / (
--             SELECT COUNT(DISTINCT u.user_id) 
--             FROM users u
--         ), 
--         2
--     ) AS percentage
-- FROM 
--     register r
-- LEFT JOIN 
--     users u ON u.user_id = r.user_id
-- GROUP BY 
--     r.contest_id
-- ORDER BY 
--     percentage DESC, 
--     r.contest_id ASC;