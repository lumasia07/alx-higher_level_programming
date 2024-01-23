#!/usr/bin/python3
# 3-square.py
"""Defines a square"""


class Square:
    """class that reps a square"""
    def __init__(self, size=0):
        """Inits sqaure class
        Args:
            size: reps size of square defined
        Raises:
            TypeError: if size is not int
            ValueError: if size < 0
        """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """
        calculate area of square
        Returns: square of size
        """

        return (self.__size ** 2)
