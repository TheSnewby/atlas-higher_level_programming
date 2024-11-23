#!/usr/bin/node

const { argv } = require('process');
const request = require('request');
const results = {};

request(argv[2], (err, response, body) => {
  if (err) throw err;
  else { // else statement not needed because throw skips scope
    body = JSON.parse(body);
    for (const element of body) {
      if (element.completed) {
        if (element.userId in results) {
          results[element.userId] += 1;
        } else {
          results[element.userId] = 1;
        }
      }
    }
    console.log(results);
  }
});
