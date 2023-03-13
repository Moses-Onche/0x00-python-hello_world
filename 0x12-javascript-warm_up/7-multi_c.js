#!/usr/bin/node
const process = require('process');
let a = 0;
if (parseInt(process.argv[2])) {
  while (a < process.argv[2]) {
    console.log('C is fun');
    a++;
  }
} else {
  console.log('Missing number of occurences');
}
