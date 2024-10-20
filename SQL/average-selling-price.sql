-- https://leetcode.com/problems/average-selling-price/?envType=study-plan-v2&envId=top-sql-50

SELECT DISTINCT(p.product_id), IFNULL(ROUND(SUM(p.price * u.units) OVER w / SUM(u.units) OVER w, 2), 0) AS average_price
FROM Prices p LEFT JOIN UnitsSold u ON p.product_id = u.product_id AND u.purchase_date BETWEEN p.start_date AND p.end_date
WINDOW w AS (PARTITION BY p.product_id)
ORDER BY p.product_id ASC;

-- SELECT p.product_id, IFNULL(ROUND(SUM(p.price * u.units) / SUM(u.units), 2), 0) AS average_price
-- FROM Prices p LEFT JOIN UnitsSold u ON p.product_id = u.product_id
-- WHERE u.purchase_date BETWEEN p.start_date AND p.end_date
-- GROUP BY p.product_id
-- ORDER BY p.product_id ASC;

-- SELECT p.product_id, 
--        CASE WHEN p.product_id = u.product_id THEN ROUND(SUM(u.units * p.price) / SUM(u.units), 2)
--             ELSE 0 END AS average_price
-- FROM Prices p LEFT JOIN UnitsSold u ON p.product_id = u.product_id
-- WHERE u.purchase_date >= p.start_date AND u.purchase_date <= p.end_date
-- GROUP BY p.product_id
-- ORDER BY p.product_id ASC;