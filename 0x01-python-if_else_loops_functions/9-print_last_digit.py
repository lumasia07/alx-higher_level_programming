#!/usr/bin/python3
def print_last_digit(number):
    last_last = abs(number) % 10
    print("{:d}".format(last_last), end='')
    return last_last
