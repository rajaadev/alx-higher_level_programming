#!/usr/bin/python3

"""Module Square."""


class Square:
    """ class square."""

    def __init__(self, size):
        """Initialize a new instance square.

        Args:
            size (int): length of new square.
        """
        self.size = size

    @property
    def size(self):
        """current size of the square.
        Raises:
            TypeError: not an integer
            ValueError: less than 0"
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return  current  square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print()
        if self.__size == 0:
            print()
