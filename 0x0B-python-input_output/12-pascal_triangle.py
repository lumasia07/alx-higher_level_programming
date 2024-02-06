#!/usr/bin/python3
"""Module to pascal triangle"""


def pascal_triangle(n):
    """Defines a pascal triangle"""
    if n <= 0:
        return []

    t = [[1]]

    for i in range(1, n):
        prev = t[-1]
        new = [1]

        for j in range(1, len(prev)):
            new.append(prev[j - 1] + prev[j])

        new.append(1)
        t.append(new)

    return t
