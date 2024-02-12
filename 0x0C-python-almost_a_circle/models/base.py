#!/usr/bin/python3
import json
"""Module to base cilass"""


class Base:
    """Defines a class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor for Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_directories):
        """Returns JSON to list dirs"""
        if list_directories is None or len(list_directories) == 0:
            return "[]"
        else:
            return json.dumps(list_directories)
