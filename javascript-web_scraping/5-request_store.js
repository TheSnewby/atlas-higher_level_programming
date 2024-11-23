#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');
const request = require('request');

request(argv[2], (err, status, data) => {
  if (err) throw err;
  else {
    fs.writeFile(argv[3], data, (writeErr, writeData) => {
      if (writeErr) throw writeErr;
    });
  }
});
