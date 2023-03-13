#!/usr/bin/node
const process = require('process');
let a = 0;
let b = 0;
if (parseInt(process.argv[2])) {
  while (a < process.argv[2]) {
    while (b < process.argv[2]) {
      console.log('X'.repeat(process.argv[2]));
      b++;
    }
    a++;
  }
} else {
  console.log('Missing size');
}
