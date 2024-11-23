#!/usr/bin/node

const { argv } = require('node:process');
const fs = require('fs');

fs.readFile(argv[1], (err, data) => {
  if (err) throw err;
  console.log(data.toString());
});
