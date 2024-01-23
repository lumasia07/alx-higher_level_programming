#!/usr/bin/python3
# 6-square.py
"""Defines a square"""


class Square:
    """Defines a class square"""
    def __init__(self, size=0, position=(0, 0)):
        """inits a class Square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size of Square

        Return:
            int: Size of Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size of square
        Args:
            value (int): size set for square
        Raises:
            TypeError: if value is not int
            ValueError: value < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter for position of square
        Returns:
            int: position of Square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter method for position of square
        Args:
            value (int): position to be set
        Raises:
            TypeError: if position is not a tuple of two positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or not
        all(isinstance(x, int) and x >= 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Defines areas of square
        Returns:
            int: area of square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints position and square"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
