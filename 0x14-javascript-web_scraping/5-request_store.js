#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const urlPath = process.argv[2];
const filePath = process.argv[3];

request(urlPath, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, body, 'utf-8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
