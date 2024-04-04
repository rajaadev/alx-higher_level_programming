#!/usr/bin/python3

"""Magic Class matching with a bytecode provided."""

import math


class MagicClass:
    """circle."""

    def __init__(self, radius=0):
        """Initialize an instance Magic Class.

        Arg:
            radius (float or int): radius of the new Magic Class.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return area of the Magic Class."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return circumference of the Magic Class."""
        return (2 * math.pi * self.__radius)
