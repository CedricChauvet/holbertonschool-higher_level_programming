-- task 15
-- Write a script that lists the number of records with the same score in the table.


SELECT score, COUNT(score) FROM second_table GROUP BY score
ORDER BY COUNT(score) DESC;