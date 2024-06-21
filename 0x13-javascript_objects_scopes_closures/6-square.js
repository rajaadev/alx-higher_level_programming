#!/usr/bin/node

const Square = require('./5-square');

class SquareWithCharPrint extends Square {
    constructor(size) {
        super(size);
    }

    charPrint(c) {
        if (!c) {
            c = 'X';
        }
        const row = c.repeat(this.size);
        for (let i = 0; i < this.size; i++) {
            console.log(row);
        }
    }
}

module.exports = SquareWithCharPrint;
