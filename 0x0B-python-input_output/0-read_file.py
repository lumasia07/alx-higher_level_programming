#!/usr/bin/python3
"""Module to read a txt file"""


def read_file(filename=""):
    """Reads a text file"""
    with open(filename, 'r', encoding='utf-8') as f:
        for i in f:
            print(i, end='')
