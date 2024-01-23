#!/usr/bin/python3
# 5-square.py
"""Defines a square"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """inits an instance of Square Class"""
        self.size = size

    @property
    def size(self):
        """Getter for square size

        Returns:
            int: size of sqauare.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size of square.

        Args:
            value (int): size set for square.

        Raises:
            TypeError: If value is not an integer
            ValueError: value < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size ** 2

    def my_print(self):
        """Prints square using #"""

        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
