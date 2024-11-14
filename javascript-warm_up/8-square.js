#!/usr/bin/node

const { argv } = require('process');
const { isNumber } = require('util');

if (argv[2] === undefined || isNaN(Number(argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv[2]; i++) {
    for (let j = 0; j < argv[2]; j++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
