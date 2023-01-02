#!/usr/bin/python3
"""Define a real class Rectangle"""


class Rectangle:
    """Class rectangle definition"""
    def __init__(self, width=0, height=0):
        """Initialize a rectangle object
        Arguments:
            width (type int): width of the rectangle
            height (type int): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Collect the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("Must be an integer")
        if value < 0:
            raise ValueError("Must be greater than zero")
        self.__width = value

    @property
    def height(self):
        """Collect the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
