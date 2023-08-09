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

class BaseGeometry:
    """An empty class"""
    
    def __dir__(cls):
        return [
            attribute
            for attribute in super().__dir__()
            if attribute != "__init_subclass__"
        ]