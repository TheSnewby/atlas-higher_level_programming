#!/usr/bin/node

const Square = require('./5-square.js');
module.exports = class Square extends Square {
  constructor (size) {
    super(size);
  }

  charPrint () {
    for (let i = 0; i < size; i++) {
      for (let j = 0; j < size; j++) {
        process.stdout.write('c');
      }
      console.log();
    }
  }
};
