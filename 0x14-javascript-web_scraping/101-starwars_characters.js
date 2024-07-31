#!/usr/bin/node

const request = require('request');

// Movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the API URL for the specified Movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// request to the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body
  const movie = JSON.parse(body);

  // Check if the movie exists
  if (!movie.title) {
    console.log('Movie not found');
    return;
  }

  // Retrieve character URLs from the movie data
  const characterUrls = movie.characters;

  // Function to fetch character names
  const fetchCharacterNames = (urls) => {
    let count = 0;

    urls.forEach((characterUrl) => {
      request(characterUrl, (err, res, charBody) => {
        if (err) {
          console.error(err);
          return;
        }

        // Parse the character response
        const character = JSON.parse(charBody);
        // Print the character's name
        console.log(character.name);
        count++;

        // If this was the last character, exit the process
        if (count === urls.length) {
          process.exit(0);
        }
      });
    });
  };

  // Fetch the character names
  fetchCharacterNames(characterUrls);
});

