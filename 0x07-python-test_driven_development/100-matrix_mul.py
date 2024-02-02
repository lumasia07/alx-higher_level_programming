#!/usr/bin/python3

"""

Module to multiply matrices

"""


def matrix_mul(m_a, m_b):
    """Defines a module to multiply matrices"""
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not all(isinstance(i, list) for i in m_a):
        raise TypeError("m_a must ba a list of lists")

    if not m_a or any(not i for i in m_a):
        raise ValueError("m_a can't be empty")

    if any(not isinstance(x, (int, float)) for i in m_a for x in i):
        raise TypeError("m_a should contain only integers or floats")

    if any(len(i) != len(m_a[0]) for i in m_a):
        raise TypeError("Each row of m_a must be of the same size")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    
    if not all(isinstance(i, list) for i in m_b):
        raise TypeError("m_b must ba a list of lists")
        
    if not m_b or any(not i for i in m_b):
        raise ValueError("m_b can't be empty")
        
    if any(not isinstance(x, (int, float)) for i in m_b for x in i):
        raise TypeError("m_b should contain only integers or floats")
        
    if any(len(i) != len(m_b[0]) for i in m_b):
        raise TypeError("Each row of m_b must be of the same size")


    res = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    for a in range(len(m_a)):
        for b in range(len(m_b[0])):
            for c in range(len(m_b)):
                res[a][b] += m_a[a][c] * m_b[c][b]

    return res
