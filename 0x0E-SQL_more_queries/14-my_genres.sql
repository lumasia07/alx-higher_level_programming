-- Lists all genres of the show Dexter
SELECT gr.name AS tv_genres.name
FROM hbtn_0d_tvshows tv
INNER JOIN hbtn_0d_genre_tv_shows gtvs ON tv.id = gtvs.tv_show_id
INNER JOIN hbtn_0d_genres gr ON gtvs.genre_id = gr.id
WHERE tv.title = "Dexter"
ORDER BY gr.name ASC;
