#!/usr/bin/node

const req = require('request');

const req = (array, n) => {
  if (n === array.length) return;
  req(array[n], (err, response, body) => {
    if (err) {
      throw err;
    } else {
      console.log(JSON.parse(body).name);
      req(array, n + 1);
    }
  });
};

req(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (error, resp, body) => {
    if (error) {
      throw error;
    } else {
      const chars = JSON.parse(body).characters;
      req(chars, 0);
    }
  }
);
