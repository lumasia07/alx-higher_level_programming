-- Lists all scores by their rating
SELECT tv_shows.title, SUM(show_ratings.rating) AS rating_sum
FROM tv_shows
JOIN show_ratings ON tv_shows.id = show_ratings.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
