#!/usr/bin/python3
"""Save an object file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an obj to txt file using JSON rep"""
    with open(filename, 'w') as f:
        json.dump(my_obj, file)
