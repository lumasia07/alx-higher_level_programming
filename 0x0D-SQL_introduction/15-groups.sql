-- Lists records with same score on table
SELECT score, COUNT(*) AS number
FROM scond_table
GROUP BY score
GROUP BY number DESC;
