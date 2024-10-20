-- https://leetcode.com/problems/project-employees-i/?envType=study-plan-v2&envId=top-sql-50

SELECT DISTINCT p.project_id, 
       ROUND(AVG(e.experience_years) OVER w, 2) AS average_years
FROM Project p
LEFT JOIN Employee e ON p.employee_id = e.employee_id
WINDOW w AS (PARTITION BY p.project_id)
ORDER BY 1;

-- SELECT p.project_id, ROUND(AVG(e.experience_years), 2) AS average_years
-- FROM Project p LEFT JOIN Employee e ON p.employee_id = e.employee_id
-- GROUP BY p.project_id
-- ORDER BY p.project_id ASC;