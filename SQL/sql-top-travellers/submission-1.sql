-- Write your query below
SELECT u.name, COALESCE(SUM(distance), 0) AS travelled_distance
FROM rides r
RIGHT JOIN users u
ON u.id = r.user_id
GROUP BY r.user_id, u.name
ORDER BY travelled_distance DESC, u.name ASC;
