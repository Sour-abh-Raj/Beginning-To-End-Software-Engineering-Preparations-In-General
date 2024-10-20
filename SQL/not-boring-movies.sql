-- https://leetcode.com/problems/not-boring-movies/?envType=study-plan-v2&envId=top-sql-50

SELECT id, movie, description, rating
FROM Cinema
WHERE id % 2 !=  0 AND description != 'boring'
ORDER BY rating DESC;

-- SELECT id, movie, description, rating
-- FROM Cinema
-- WHERE MOD(id, 2) = 1 AND description <> 'boring'
-- ORDER BY rating DESC;