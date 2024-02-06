#!/usr/bin/python3
"""Loads adds Saves"""


import sys
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

if __name__ == "__main__":
    try:
        x = load_from_json_file("add_item.json")
    except FileNotFoundError:
        x = []
    x.extend(sys.argv[1:])
    save_to_json_file(x, "add_item.json")
