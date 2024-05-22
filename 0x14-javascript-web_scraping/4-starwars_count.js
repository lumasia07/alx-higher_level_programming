#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    let c = 0;
    const films = JSON.parse(body).results;
    for (let res = 0; res < films.length; res++) {
      const chts = films[res].characters;
      for (let i = 0; i < chts.length; i++) {
        if (chts[i] === 'https://swapi-api.alx-tools.com/api/people/18/') {
          c += 1;
        }
      }
    }
    console.log(c);
  }
});
