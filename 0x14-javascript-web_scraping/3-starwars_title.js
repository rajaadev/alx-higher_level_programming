#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the URL for the API request
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body
  const movie = JSON.parse(body);

  // Check if the movie exists and print the title
  if (movie.title) {
    console.log(movie.title);
  } else {
    console.log('Movie not found');
  }
});
