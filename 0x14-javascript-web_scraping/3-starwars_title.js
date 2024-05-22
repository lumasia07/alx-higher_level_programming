#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const endPoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

request({ url: endPoint, method: 'GET' }, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(body && JSON.parse(body).title);
  }
});
