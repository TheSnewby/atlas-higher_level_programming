#!/usr/bin/node

const request = require('request');
const { argv } = require('process');

const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + argv[2], (err, response, body) => {
  if (err) throw err;
  if (!err && response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  }
});
