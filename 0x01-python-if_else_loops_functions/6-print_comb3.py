#!/usr/bin/python3
for digit in range(10):
    for y in range(digit + 1, 10):
        if (digit, y) != (8, 9):
            print("{:d}{:d}".format(digit, y), end=', ')
        else:
            print('89')
