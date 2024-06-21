#!/usr/bin/node

// class Rectangle
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {}; // Returning an empty object if w or h is not a positive integer
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
