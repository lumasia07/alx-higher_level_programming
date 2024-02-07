#!/usr/bin/python3
"""Module that inserts a text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Open file in read mode"""

    with open(filename, 'r') as file:
        line = file.readlines()

    """Open filr in write mode"""
    with open(filename, 'w') as file:
        for i in lines:
            file.write(line)
            if search_string in i:
                file.write(new_string + '\n')
