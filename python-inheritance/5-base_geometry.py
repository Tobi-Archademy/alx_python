#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""
class BaseMetaClass(type):
    """
    overrides.
    """

    def __dir__(cls):
        return [
            attribute
            for attribute in super().__dir__()
            if attribute != "__init_subclass__"
        ]

class BaseGeometry(metaclass=BaseMetaClass):
    """A class with public instance methods area and integer_validator"""
    
    def __dir__(cls):
        return [
            attribute
            for attribute in super().__dir__()
            if attribute != "__init_subclass__"
        ]
        
        
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value is an integer greater than 0"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))