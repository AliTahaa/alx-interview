#!/usr/bin/node

const req = require('request');

const req = (array, n) => {
  if (n === array.length) return;
  req(array[n], (error, resp, b) => {
    if (error) {
      throw error;
    } else {
      console.log(JSON.parse(b).name);
      req(array, n + 1);
    }
  });
};

req(
  `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`,
  (error, resp, b) => {
    if (error) {
      throw error;
    } else {
      const chars = JSON.parse(b).characters;
      req(chars, 0);
    }
  }
);
