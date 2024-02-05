#!/usr/bin/python3
"""Module to check if an instance of class is inherited"""


def inherits_from(obj, a_class):
    """Returns true, false otherwise"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
