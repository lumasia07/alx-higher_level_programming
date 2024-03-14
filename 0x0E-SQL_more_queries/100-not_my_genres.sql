-- Lists all genres not linked to Dexter
SELECT name
FROM tv_genres
WHERE id NOT IN (
	SELECT genre_id
	FROM shows_genres
	INNER JOIN tv_shows ON tv_shows.id = shows_genres.show_id
	WHERE title = 'Dexter'
)
ORDER BY name ASC;
