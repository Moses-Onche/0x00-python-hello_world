#!/usr/bin/node
/* This script stores the contents of a webpage in a file. */
const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
