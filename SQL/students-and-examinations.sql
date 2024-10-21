-- https://leetcode.com/problems/students-and-examinations/?envType=study-plan-v2&envId=top-sql-50

SELECT st.student_id, st.student_name, su.subject_name, COUNT(e.student_id) AS attended_exams
FROM Students st CROSS JOIN Subjects su LEFT JOIN Examinations e
ON st.student_id = e.student_id AND su.subject_name = e.subject_name
GROUP BY st.student_id, st.student_name, su.subject_name
ORDER BY st.student_id, st.student_name, su.subject_name ASC;