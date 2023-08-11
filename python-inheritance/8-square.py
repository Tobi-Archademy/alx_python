"""
Contains the class BaseGeometry and subclass Rectangle
"""

Rectangle = __import__('7-rectangle').Rectangle


"""Square class"""


class Square(Rectangle):
    """Initializing size"""

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
