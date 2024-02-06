#!/usr/bin/python3
"""Module to append a string to a txt file"""


def append_write(filename="", text=""):
    """Appends a string to a text file"""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(text)
    return len(text)
