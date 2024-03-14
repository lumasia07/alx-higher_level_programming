-- Lists all comedy in database
SELECT title
FROM hbtn_0d_tvshows
WHERE id IN (
	SELECT tv_show_id
	FROM hbtn_0d_genre_tv_shows
	WHERE genre_id = (
		SELECT ID
		FROM hbtn_0d_genres
		WHERE name = "Comedy"
	)
);
ORDER BY title ASC;

