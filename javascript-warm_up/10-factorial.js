#!/usr/bin/node

const { argv } = require('process');

function factorial (num) {
  if (num === 0) {
    return 1;
  }
  return factorial(num - 1) * num;
}

if (argv[2] === undefined) {
  console.log(factorial(1));
} else {
  console.log(factorial(argv[2]));
}
