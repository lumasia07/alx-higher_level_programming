#!/usr/bin/python3
"""Module to check if object belongs to a specified instance"""


def is_same_class(obj, a_class):
    """Checks if an object belongs to a specified class"""
    return type(obj) is a_class
