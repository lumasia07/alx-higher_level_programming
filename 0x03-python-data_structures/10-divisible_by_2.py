#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    their_list = []

    for x in my_list:
        their_list.append(x % 2 == 0)
    return their_list
