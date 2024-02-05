#!/usr/bin/python3
"""Module to get a list of attributes"""


def lookup(obj):
    """Defines a function lookup with parameter obj"""
    return [x for x in dir(obj) if not callable(getattr(obj, x))]
