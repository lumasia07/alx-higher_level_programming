#!/usr/bin/python3
def magic_string():
    magic_string.y = getattr(magic_string, 'y', 0) + 1
    return ", ".join(['BestSchool' for x in range(magic_string.y)])
