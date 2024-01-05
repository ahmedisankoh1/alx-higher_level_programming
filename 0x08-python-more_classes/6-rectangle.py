#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self._width * self._height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self._width == 0 or self._height == 0:
            return (0)
        return ((self._width * 2) + (self._height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self._width == 0 or self._height == 0:
            return ("")

        rct = []
        for i in range(self._height):
            [rct.append('#') for j in range(self._width)]
            if i != self._height - 1:
                rct.append("\n")
        return ("".join(rct))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rct = "Rectangle(" + str(self._width)
        rct += ", " + str(self._height) + ")"
        return (rct)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
