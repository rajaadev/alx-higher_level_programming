#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Get the URL and file path from command line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Make a GET request to the URL
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Write the response body to the specified file in UTF-8 encoding
  fs.writeFile(filePath, body, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
});
