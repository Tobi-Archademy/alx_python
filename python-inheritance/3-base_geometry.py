#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


class BaseGeometry:
    """An empty class"""
    
    def __dir__(cls):
        return [
            attribute
            for attribute in super().__dir__()
            if attribute != "__init_subclass__"
        ]