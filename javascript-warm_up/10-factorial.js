#!/usr/bin/node

const { argv } = require('process');

function factorial (num) {
  if (num === 0) {
    return 1;
  }
  return factorial(num - 1) * num;
}

console.log(factorial(argv[2]));
