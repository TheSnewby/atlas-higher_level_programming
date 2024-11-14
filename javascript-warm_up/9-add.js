#!/usr/bin/node

const { argv } = require('process');

function add (a, b) {
  if (isNaN(Number(a)) || isNaN(Number(b))) {
    console.log('NaN');
  } else {
    console.log(`${Number(a) + Number(b)}`);
  }
}

add(argv[2], argv[3]);
