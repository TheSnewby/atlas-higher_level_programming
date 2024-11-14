#!/usr/bin/node

function add (a, b) {
  if (isNaN(Number(a)) || isNaN(Number(b))) {
    return NaN;
  } else {
    return Number(a) + Number(b);
  }
}
