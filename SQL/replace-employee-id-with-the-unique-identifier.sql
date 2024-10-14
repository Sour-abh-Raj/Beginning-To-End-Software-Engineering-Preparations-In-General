-- https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/solutions/5795041/easy-solution-with-explanation/?envType=study-plan-v2&envId=top-sql-50

SELECT Employees.name, EmployeeUNI.unique_id
FROM Employees LEFT JOIN EmployeeUNI
ON Employees.id = EmployeeUNI.id
ORDER BY name ASC;
