-- Lists all the cities of California in database
-- Sorted by ascending order
SELECT cities.name
FROM cities, states
WHERE cities.state_id = states.id
AND states.name = 'California'
ORDER BY cities.id ASC;
