-- Lists genres by their rating sum
SELECT tv_genres.name, SUM(show_ratings.rating) AS rating_sum
FROM tv_genres
JOIN shows_genres ON tv_genres.id = shows_genres.genre_id
JOIN tv_shows ON shows_genres.show_id = tv_shows.id
JOIN show_ratings ON tv_shows.id = show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
