#!/usr/bin/python3
import json
"""Module to base class"""


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

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of dicts"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON to a file"""
        if list_objs is None:
            list_objs = []
        f_name = cls.__name__ + ".json"
        with open(f_name, 'w') as f:
            s = cls.to_json_string([o.to_dictionary() for o in list_objs])
            f.write(s)
