#!/usr/bin/node

const { argv } = require('node:process');

const newNum = Number(argv[2]);
if (isNaN(newNum)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${argv[2]}`);
}
