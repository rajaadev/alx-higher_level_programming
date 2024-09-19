#!/usr/bin/node

// Class Rectangle
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {}; // Returning an empty object if w or h is not a positive integer
    }
    this.width = w;
    this.height = h;
  }

  // Method to print the rectangle
  print() {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // Method to exchange the width and height of the rectangle
  rotate() {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // Method to double the width and height of the rectangle
  double() {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
