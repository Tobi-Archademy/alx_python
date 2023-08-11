#!/usr/bin/python3
"""
contains the class BaseGeometry and subclass Rectangle
"""

BaseGeometry = __import__('5-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):

    """Initializing with and height"""

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)