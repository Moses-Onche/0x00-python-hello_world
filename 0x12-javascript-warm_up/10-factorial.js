#!/usr/bin/node
function factorial (i) {
  if (i) {
    return (i * (factorial(i - 1)));
  } else {
    return (1);
  }
}

console.log(factorial(process.argv[2]));
