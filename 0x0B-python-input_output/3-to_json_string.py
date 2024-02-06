#!/usr/bin/python3
"""Module to return JSON"""
import json


def to_json_string(my_obj):
    """Returns the JSON rep of string"""
    return json.dumps(my_obj)
