#!/usr/bin/node

const { argv } = require('process');

if (argv.length <= 3) {
  console.log('0');
} else {
  let firstMax;
  let secondMax;
  if (Number(argv[2]) > Number(argv[3])) {
    firstMax = Number(argv[2]);
    secondMax = Number(argv[3]);
  } else {
    firstMax = Number(argv[3]);
    secondMax = Number(argv[2]);
  }
  for (let i = 4; i < argv.length; i++) {
    if (Number(argv[i]) > firstMax) {
      secondMax = firstMax;
      firstMax = Number(argv[i]);
    } else if (Number(argv[i]) > secondMax) {
      secondMax = Number(argv[i]);
    }
  }
  console.log(secondMax);
}
