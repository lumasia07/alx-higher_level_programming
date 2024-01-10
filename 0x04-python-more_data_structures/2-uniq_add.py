#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set()

    for i in my_list:
        a.add(i)

    return sum(a)
