-- Lists all the cities of California in database
-- Sorted by ascending order
SELECT id, name
FROM cities
WHERE state_id = 1
ORDER BY cities.id ASC;
