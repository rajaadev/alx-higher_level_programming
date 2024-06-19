#!/usr/bin/node

function factorial(n) {
  if (isNaN(parseInt(n)) || parseInt(n) < 0) {
    return 1;
  } else if (parseInt(n) === 0) {
    return 1;
  } else {
    return parseInt(n) * factorial(parseInt(n) - 1);
  }
}

const arg = process.argv[2];
console.log(factorial(arg));
