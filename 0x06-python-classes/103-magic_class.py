#!/usr/bin/python3
"""Python bytecodes to calculate areas & circumfrence"""
import math


class MagicClass:
    """Defines MagicClass"""
    def __init__(self, radius=0):
        """Initializes python bytecode
        Args: radius
        Raises: TypeError: if radius is non-number
        """
        self.__radius = 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be number')
        self.__radius = radius

    def area(self):
        """Calculates area
        Returns: Area
        """
        return (self.__radius ** 2 * math.pi)

    def circumfrence(self):
        """Calculates circumfrence
        Returns: circumfrence
        """
        return (2 * math.pi * self.__radius)
