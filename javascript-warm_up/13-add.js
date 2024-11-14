#!/usr/bin/node

function add (a, b) {  // export function might work as well
  if (isNaN(Number(a)) || isNaN(Number(b))) {
    return NaN;
  } else {
    return Number(a) + Number(b);
  }
}

module.exports.add = add;
