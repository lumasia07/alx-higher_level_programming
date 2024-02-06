#!/usr/bin/python3
"""Creates object from JSON file"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file"""
    with open(filename, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return None
