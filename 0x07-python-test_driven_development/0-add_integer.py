#!/usr/bin/python3
"""

Module to add 2 integers

"""


def add_integer(a, b=98):
    """Function to add two integers
    Args: a , b, Return: Sum fo a and b, Raise:TypeError
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
