-- Lists cities with the highest averages btn July and August
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
WHERE `month` = 7 OR `month` = 8
GROUP BY `city`
ORDER BY `avg_tmp` DESC
LIMIT 3;
