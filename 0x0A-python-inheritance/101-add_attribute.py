#!/usr/bin/python3
"""Module to add a new attribute"""


def add_attribute(obj, attr_name, attr_value):
    """Adds a new attr to obj"""
    if hasattr(obj, '__dict__'):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
