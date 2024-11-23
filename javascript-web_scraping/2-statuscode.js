#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request(argv[2], (error, response, body) => {
  if (!error && response.statusCode === 200) {
    console.log(body);
  }
});
