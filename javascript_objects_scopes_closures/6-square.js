#!/usr/bin/node

const fiveSquare = require('./5-square.js');
module.exports = class Square extends fiveSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let str;
    for (let i = 0; i < this.height; i++) {
      if (c === undefined) {
        str = 'X';
      } else {
        str = c;
      }
      console.log(str.repeat(this.width));
    }
  }
};
