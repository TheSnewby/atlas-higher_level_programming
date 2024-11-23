#!/usr/bin/node

const { argv } = require('process');
const request = require('request');

request(argv[2], (err, response, body) => {
  if (err) throw err;

  console.log(`code: ${response.statusCode}`);
});
