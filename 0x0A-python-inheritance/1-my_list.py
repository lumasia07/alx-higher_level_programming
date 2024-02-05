#!/usr/bin/python3
"""Module that inherits MyList from List"""


class MyList(list):
    """A class MyList"""
    def print_sorted(self):
        """Prints a sorted list"""
        print(sorted(self))
