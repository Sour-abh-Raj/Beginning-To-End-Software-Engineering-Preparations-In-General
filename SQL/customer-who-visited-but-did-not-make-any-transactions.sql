-- https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/submissions/1425763517/?envType=study-plan-v2&envId=top-sql-50

# Write your MySQL query statement below

SELECT v.customer_id, COUNT(v.customer_id) AS count_no_trans
FROM Visits v LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id
ORDER BY v.customer_id ASC;

-- SELECT
--   Visits.customer_id,
--   COUNT(Visits.visit_id) AS count_no_trans
-- FROM Visits
-- LEFT JOIN Transactions
--   USING (visit_id)
-- WHERE Transactions.transaction_id IS NULL
-- GROUP BY 1;

-- SELECT Customer_id, COUNT(visit_id) AS count_no_tran
-- FROM Visits
-- WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)
-- GROUP BY customer_id
-- ORDER BY customer_id ASC;