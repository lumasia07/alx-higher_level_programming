#!/usr/bin/python3
# 2-square.py
"""Defines a square"""


class Square:
    """A class that reps a square"""

    def __init__(self, size=0):
        """Inits square class
        Args:
            size; reps size of square defined
        Raises:
            TypeError: if size is not an int
            ValueError: if size < 0
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
