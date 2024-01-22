#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    sum = 0

    try:
        for i in range(x):
            val = my_list[i]
            if type(val) == int:
                print("{:d}".format(val), end="")
                sum += 1
    except IndexError:
        pass

    print()

    return sum
