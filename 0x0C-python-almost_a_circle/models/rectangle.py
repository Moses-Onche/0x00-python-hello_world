#!/usr/bin/python3
"""Defines a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Create a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new rectangle
        Args:
            width (int): The rectangle's width.
            height (int): The rectangle's height.
            x (int): The x coordinate of the rectangle.
            y (int): The y coordinate of the rectangle.
            id (int): The identity of the rectangle.
        Raises:
            TypeError: If either the width or height is not an int.
            ValueError: If either of the width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)
