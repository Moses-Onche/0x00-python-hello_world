#!/usr/bin/node
/* This script prints all the characters of a Star Wars movie. */

const request = require('request');
const uid = process.argv[2];
const requestUrl = 'https://swapi-api.hbtn.io/api/films/';
request.get(requestUrl + uid, function (error, res, body) {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const dd = data.characters;
  for (const count of dd) {
    req.get(count, function (error, res, body1) {
      if (error) {
        console.log(error);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
