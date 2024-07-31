#!/usr/bin/node

const request = require('request');

// Get the Movie ID from the command line arguments
const movieId = process.argv[2];

// Construct the API URL for the specified Movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
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

  // Use a Promise to handle asynchronous requests
  const fetchCharacterNames = (urls) => {
    const characterPromises = urls.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, (err, res, charBody) => {
          if (err) {
            reject(err);
          } else {
            const character = JSON.parse(charBody);
            resolve(character.name);
          }
        });
      });
    });

    // Wait for all promises to resolve and print character names
    Promise.all(characterPromises)
      .then((names) => {
        names.forEach((name) => {
          console.log(name);
        });
      })
      .catch((err) => {
        console.error(err);
      });
  };

  // Fetch the character names
  fetchCharacterNames(characterUrls);
});
