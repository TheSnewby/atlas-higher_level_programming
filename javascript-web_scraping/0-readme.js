#!/usr/bin/node

const { argv } = require('process');
const fs = require('fs');

fs.readFile(argv[2], (err, data) => {
  if (err) throw err;

  console.log(data.toString());
});