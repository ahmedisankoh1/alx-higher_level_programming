#!/usr/bin/python3
"""Creating a retcanngle"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self._width)

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._width = value


    @property
    def height(self):
        return (self._height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._height = value

        def area(self):
            return (self._width * self._height)

        def perimeter(self):
            if self._width == 0 or self._height == 0:
                return (0)
            return ((2 * self._width) * (2 * self._height))

        def __str__(self):
            if self._width == 0 or self._height == 0:
                return ("")

            rct = []
            for i in range(self._height):
                [rct.appent('#') for j in range(self._width)]
                if i != self._height - 1:
                    rct.append("\n")
            return ("".join(rct))


