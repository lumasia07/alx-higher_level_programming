#!/usr/bin/python3
"""Module to convert JSON to an object"""
import json


def from_json_string(my_str):
    """Returns object from JSON"""
    return json.loads(my_str)
