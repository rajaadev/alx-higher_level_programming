#!/usr/bin/python3
'''Module for Rectangle class.'''

from models.base import Base


class Rectangle(Base):
    """Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        """Setter for width."""
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        """Setter for height."""
        self.__height = value

    @property
    def x(self):
        """Getter for x attribute."""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        """Setter for x attribute."""
        self.__x = value

    @property
    def y(self):
        """Getter for y attribute."""
        return self.__y

    @y.setter
    def y(self, value):
         self.validate_integer("y", value)
        """Setter for y attribute."""
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        '''Method for value validating.'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """Calculate the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle  with '#' characters."""
        for _ in range(self.height):
            print("#" * self.width)

    def __str__(self):
        """Return string representation of Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def __update(self, id=None, width=None, height=None, x=None, y=None):
     """Update the attributes of the Rectangle."""
     if id is not None:
        self.id = id
     if width is not None:
        self.width = width
     if height is not None:
        self.height = height
     if x is not None:
        self.x = x
     if y is not None:
        self.y = y

   def update(self, *args, **kwargs):
    '''Updates attributes via no-keyword & keyword args.'''
    if args:
        self.__update(*args)
    elif kwargs:
        self.__update(**kwargs)

   def to_dictionary(self):
       """Return dictionary representation of Rectangle."""
       return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
       }
