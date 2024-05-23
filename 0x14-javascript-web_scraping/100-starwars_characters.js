#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2]

if (!movieId) {
  process.exit(1);
}

const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request (url, (err, response, body) => {
  if (err) {
    process.exit(1);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(response.statusCode);
    return;
  }

  const film = JSON.parse(body);
  const chtUrl = film.characters;

  chtUrl.forEach(urls => {
    request(urls, (charErr, charRes, charBody) => {
      if (charErr) {
        console.error(charErr);
        return;
      }

      if (charRes.statusCode !== 200) {
        console.error(charRes.statusCode);
      }

      const chts = JSON.parse(charBody);
      console.log(chts.name);
    });
  });
});
