#!/usr/bin/node

const { argv } = require('node:process');

const newNum = parseInt(argv[2]);
if (newNum === NaN) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argv[2]}`);
}
