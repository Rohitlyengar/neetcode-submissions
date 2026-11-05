-- Write your query below
SELECT u.name, SUM(t.amount) AS balance
FROM users u
INNER JOIN transactions t
ON u.account = t.account
GROUP BY t.account, u.name
HAVING SUM(amount) > 10000;
