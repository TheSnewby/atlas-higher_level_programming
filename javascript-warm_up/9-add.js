#!/usr/bin/node

const { argv } = require('process');

function add (a, b) {
  if (isNaN(Number(a)) || isNaN(Number(b))) {
    console.log('NaN');
  } else {
    console.log(`${a + b}`);
  }
}

add(argv[2], argv[3]);
