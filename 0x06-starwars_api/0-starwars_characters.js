#!/usr/bin/node

const req = require('request');

const req = (arr, i) => {
  if (i === arr.length) return;
  req(arr[i], (err, response, body) => {
    if (err) {
      throw err;
    } else {
      console.log(JSON.parse(body).name);
      req(arr, i + 1);
    }
  });
};

req(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (err, response, body) => {
    if (err) {
      throw err;
    } else {
      const chars = JSON.parse(body).characters;
      req(chars, 0);
    }
  }
);
