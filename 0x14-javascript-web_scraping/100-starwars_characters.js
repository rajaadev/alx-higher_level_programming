#!/usr/bin/node

const request = require('request');

// Movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the API URL for the specified Movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// GET request to the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body
  const movie = JSON.parse(body);

  // movie exists
  if (!movie.title) {
    console.log('Movie not found');
    return;
  }

  // Print the movie title
  console.log(`Characters in "${movie.title}":`);

  // Retrieve character URLs and fetch their names
  const characterUrls = movie.characters;

  // Function fetch character names
  const fetchCharacterNames = (urls) => {
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
      });
    });
  };

  // Fetch the character names
  fetchCharacterNames(characterUrls);
});
