#!/usr/bin/python3
"""Defines a module that inhertis from int"""


class MyInt(int):
    """Defines a class int"""
    def __eq__(self, other):
        """override == op"""
        return super().__ne__(other)

    def __ne__(self, other):
        """override != op"""
        return super().__eq__(other)
