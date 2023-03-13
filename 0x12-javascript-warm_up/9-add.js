#!/usr/bin/node
const process = require('process');
const a = parseInt(process.argv[2]);
const b = parseInt(process.argv[3]);
function add (a, b) {
  if (a && b) {
    return console.log(a + b);
  } else {
    return console.log(NaN);
  }
}

add(a, b);
