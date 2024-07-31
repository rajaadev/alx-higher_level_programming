#!/usr/bin/node

const request = require('request');

// API URL from the command line arguments
const apiUrl = process.argv[2];

// GET request to the Star Wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body
  const films = JSON.parse(body).results;

  // Filter + count the movies where Wedge Antilles is present
  const wedgeAntillesId = 18;
  const count = films.reduce((accumulator, film) => {
    // Wedge Antilles is in the characters array
    if (film.characters.some(character => character.endsWith(`/${wedgeAntillesId}/`))) {
      return accumulator + 1;
    }
    return accumulator;
  }, 0);

  // Print count of movies
  console.log(count);
});
