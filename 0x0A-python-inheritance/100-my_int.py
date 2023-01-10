#!/usr/bin/python3
"""Defines a class my_int that inherits from int"""


class MyInt(int):
    """Invert the operators == and !="""

    def __eq__(self, value):
        """Return != for =="""
        return self.real != value

    def __ne__(self, value):
        """Return == for !="""
        return self.real == value
