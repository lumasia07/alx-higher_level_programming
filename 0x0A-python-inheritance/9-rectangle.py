#!/usr/bin/python3
"""Module to raise Exception"""


class BaseGeometry:
    """Raises Exception Error"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Defines a rectangle"""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Defines area"""
        return self.__width * self.__height

    def __str__(self):
        """Dunder method for string"""
        return "[Retangle] {}/{}".format(self.__width, self.__height)

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
