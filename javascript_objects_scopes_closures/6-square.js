#!/usr/bin/node

const fiveSquare = require('./5-square.js');
module.exports = class Square extends fiveSquare {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.weight; j++) {
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
