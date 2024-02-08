#!/usr/bin/python3
"""Module to class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Defines a class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new instance of class Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        self.__width

    @width.setter
    def width(self, val):
        self.__width = val

    @property
    def height(self):
        self.__height
        
    @height.setter
    def height(self, val):
        self.__height = val

    @property
    def x(self):
        self.__x

    @x.setter
    def x(self, val):
        self.__x = val

    @property
    def y(self):
        self.__y

    @y.setter
    def y(self, val):
        self.__y = val

