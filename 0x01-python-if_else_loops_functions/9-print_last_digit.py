#!/usr/bin/python3
def print_last_digit(number):
    last_last = number % 10
    if last_last:
        print("{:d}".format(last_last))
