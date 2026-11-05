-- Write your query below
SELECT c.customer_id, c.name
FROM customers c
WHERE c.customer_id IN (
    SELECT o.customer_id
    FROM orders o
    INNER JOIN product p
    ON o.product_id = p.product_id
    WHERE order_date >= '2020-06-01 00:00:00' AND order_date <= '2020-6-30 23:59:59'
    GROUP BY o.customer_id
    HAVING SUM(o.quantity * p.price) >= 100
) AND c.customer_id IN (
    SELECT o.customer_id
    FROM orders o
    INNER JOIN product p
    ON o.product_id = p.product_id
    WHERE order_date >= '2020-07-01 00:00:00' AND order_date <= '2020-7-31 23:59:59'
    GROUP BY o.customer_id
    HAVING SUM(o.quantity * p.price) >= 100
);




