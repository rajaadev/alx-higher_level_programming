#!/usr/bin/python3

""" MOdule : Square."""


class Square:
    """class square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.

        Raises: 
            TypeError: if not integer
            ValueError: size less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
