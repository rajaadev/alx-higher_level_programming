#!/usr/bin/python3

"""Module Square."""


class Square:
    """Class square."""

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
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
