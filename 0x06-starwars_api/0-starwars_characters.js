#!/usr/bin/node

const request = require('request');

const filmNum = process.argv[2] + '/';
const filmURL = 'https://swapi-api.hbtn.io/api/films/';

// Make request to film URL
request(filmURL + filmNum, async function (err, res, body) {
  if (err) return console.error(err);

  // Parse body to get list of character URLs
  const charURLList = JSON.parse(body).characters;

  // Make request to each character URL
  for (const actor of charURLList) {
    await new Promise(function (resolve, reject) {
      request(actor, function (err, res, body) {
        if (err) return console.error(err);

        // Parse body to get character name
        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});