-- https://leetcode.com/problems/average-time-of-process-per-machine/?envType=study-plan-v2&envId=top-sql-50

SELECT s.machine_id, ROUND(AVG(e.timestamp) - AVG(s.timestamp), 3) AS processing_time
FROM Activity s INNER JOIN Activity e USING(machine_id, process_id)
WHERE s.activity_type = 'start' AND e.activity_type = 'end'
GROUP BY 1
ORDER BY 1 ASC;

-- -- Using sub-query
-- SELECT a.machine_id, ROUND(
--     -- (SELECT AVG(e.timestamp) FROM Activity e WHERE e.activity_type = 'end' AND process_id = process_id AND e.machine_id = a.machine_id) -
--     -- (SELECT AVG(s.timestamp) FROM Activity s WHERE s.activity_type = 'start'  AND process_id = process_id AND s.machine_id = a.machine_id)

--     -- We can normalize process_id for the s and e Activity tables with a.machine_id as activity_type and machine_id can uniquely define process_id
--     (SELECT AVG(e.timestamp) FROM Activity e WHERE e.activity_type = 'end' AND process_id = process_id AND e.machine_id = a.machine_id) -
--     (SELECT AVG(s.timestamp) FROM Activity s WHERE s.activity_type = 'start'  AND process_id = process_id AND s.machine_id = a.machine_id)
-- , 3) AS processing_time
-- FROM Activity a
-- GROUP BY 1
-- ORDER BY 1 ASC;