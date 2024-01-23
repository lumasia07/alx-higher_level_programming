#!/usr/bin/python3
# 4-main.py
"""Defines a sqaure"""


class Square:
    """Defines a class Square"""
    def __init__(self, size=0):
        """Inits new instance of class Square"""
        self.size = size

    @property
    def size(self):
        """Getter method for getting size of square

        Returns:
            int: size of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method that sets square size.

        Args:
            value (int): size of square.

        Raises:
            TypeError: if value is non-int
            ValueError: value is < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns area of sqaure

        Returns:
            int: area of square
        """
        return self.__size ** 2
