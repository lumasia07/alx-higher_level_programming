#!/usr/bin/python3
"""Module that writes a string into a txt file"""


def write_file(filename="", text=""):
    """Writes a string into a txt file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    return len(text)
