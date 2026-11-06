-- Write your query below
SELECT DISTINCT c.title 
FROM content c
INNER JOIN tv_program t
ON c.content_id = t.content_id
WHERE t.program_date >= '2020-06-01' AND t.program_date < '2020-07-01'
AND c.kids_content = 'Y' AND c.content_type = 'Movies';