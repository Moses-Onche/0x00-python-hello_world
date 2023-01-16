#!/usr/bin/python3
"""Defines a class Base"""
import json
import csv
import turtle


class Base:
    """Base for all other classes in this project.
    private class attribute:
        __nb_objects (int): number of instantiated classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new base
        Args:
            id (int): new base identifier
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
