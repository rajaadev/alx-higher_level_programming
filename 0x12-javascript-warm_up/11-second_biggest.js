#!/usr/bin/node

function secondBiggest(numbers) {
  if (numbers.length <= 1) {
    return 0;
  } else {
    numbers.sort((a, b) => b - a);
    return numbers[1];
  }
}

const args = process.argv.slice(2).map(Number);
console.log(secondBiggest(args));
