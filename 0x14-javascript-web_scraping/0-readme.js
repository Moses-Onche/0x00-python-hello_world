#!/usr/bin/node
/* A script that reads out the contents of a file. */
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
