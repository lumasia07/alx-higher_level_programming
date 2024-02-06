#!/usr/bin/python3
"""Module to define a class Student"""


class Student:
    """Reps a student"""

    def __init__(self, first_name, last_name, age):
        """Inits a new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns Dict in JSON form"""
        if (type(attrs) == list and all(type(i) == str for i in attrs)):
            return{j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__
