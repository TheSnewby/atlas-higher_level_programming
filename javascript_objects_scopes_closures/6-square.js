#!/usr/bin/node

const fiveSquare = require('./5-square.js');
module.exports = class Square extends fiveSquare {
  constructor (size) {
    super(size);
  }

  charPrint (c) {
    for (let i = 0; i < this.size; i++) {
      for (let j = 0; j < this.size; j++) {
        if (c === undefined) {
          process.stdout.write('X');
        } else {
          process.stdout.write(c);
        }
      }
      console.log();
    }
  }
};
