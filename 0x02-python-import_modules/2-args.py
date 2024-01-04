#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args_counter = len(sys.argv) - 1

    if args_counter == 0:
        print("0 arguments.")
    elif args_counter == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(args_counter))
    for x in range(args_counter):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
