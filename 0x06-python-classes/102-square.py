#!/usr/bin/python3
"""Square module"""


class Square:
    """defines a square"""

    def __init__(self, size=0):
        """Creates a square
        Args: size: len of side Square
        """
        self.__size = size

    @property
    def size(self):
        """Getter for size of square
        Raises:
            TypeError: if size != int
            ValueError: if size < 0
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size of must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Get the area of a Square
        Returns: Size of the square
        """
        return self.__size * self.__size

    def __le__(self, other):
        return self.area() <= other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __lt__(self, other):
        return self.area() < other.area()
