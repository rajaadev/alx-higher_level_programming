#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line arguments
const apiUrl = process.argv[2];

// Make a GET request to the API URL
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  // Parse the response body
  const todos = JSON.parse(body);

  // Create an object to store the count of completed tasks for each user
  const completedTasksCount = {};

  // Iterate through the todos and count completed tasks per user
  todos.forEach(todo => {
    if (todo.completed) {
      const userId = todo.userId;
      if (completedTasksCount[userId]) {
        completedTasksCount[userId] += 1;
      } else {
        completedTasksCount[userId] = 1;
      }
    }
  });

  // Print the results
  console.log(completedTasksCount);
});
