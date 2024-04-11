#!/usr/bin/python3
"""Defines a Rectangle class."""

class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance. """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for instance  width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for instance width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for instance height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for instance height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
	Returns a string representation
	of the rectangle using '#' characters
	"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str[:-1]

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
