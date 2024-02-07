#!/usr/bin/python3
"""Module that inserts a text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Open file in read mode"""
    txt = ""
    with open(filename) as f:
        for line in f:
            txt += line
            if search_string in line:
                txt += new_string
    with open(filename, 'w') as g:
        g.write(txt)
