#!/usr/bin/python3
"""Loads adds Saves"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        x = load_from_json_file("add_item.json")
    except FileNotError:
        x = []
    x.extend(sys.argv[1:])
    save_to_json_file(x, "add_item.json")
