#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, mul, div, sub

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    o = {"+": add, "-": sub, "/": div, "*": mul}

    if sys.argv[2] not in list(o.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

        a = int(sys.argv[1])
        b = int(sys.argv[3])

        print("{} {} {} = {}".format(a, sys.argv[2], b, o[sys.argv[2]](a, b)))
