#!/usr/bin/node

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/';
let count = 0;

request(url, (err, response, body) => {
  if (err) throw err;
  else if (response.statusCode === 200) {
    const dict = JSON.parse(body);
    for (const movie of dict.results) {
      for (const char of movie.characters) {
        if (char.includes('people/18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
