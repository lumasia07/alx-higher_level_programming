-- Lists all shows without the genre comedy
SELECT title
FROM tv_shows
WHERE id NOT IN (
	SELECT show_id
	FROM shows_genres
	INNER JOIN tv_genres ON tv_genres.id = shows_genres.genre_id
	WHERE name = 'Comedy'
)
ORDER BY title ASC;
