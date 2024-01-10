#!/usr/bin/python3
def uniq_add(my_list=[]):
    a = set()

    b = lambda a, i: a.add(a) or a
    c = reduce(b, my_list, a)
    return sum(c)
