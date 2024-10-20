-- https://leetcode.com/problems/employee-bonus/?envType=study-plan-v2&envId=top-sql-50

SELECT Employee.name, Bonus.bonus
FROM Employee LEFT JOIN BONUS USING(empId)
WHERE Bonus.bonus < 1000 OR Bonus.bonus IS NULL
ORDER BY Employee.name ASC;