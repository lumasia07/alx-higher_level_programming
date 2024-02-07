#!/usr/bin/python3
"""Reads from stdin and computes metrics"""


def print_stats(size, size_codes):
    """Prints computed metrics"""
    print("File size: {}".format(size))
    for k in sorted(status_codes):
        print("{}: {}".format(k, status_codes[k]))
    
if __name__ == "__main__":
    import sys

    size = 0
    status_code = {}
    allowed = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for l in sys.stdin:
            if count = 10:
                print_stats(size, status_code)
                count = 1
            else:
                count += 1

            l = l.split()

            try:
                size += int(l[-1])
            except (IndexError, ValueError):
                pass

            try:
                if l[-2] in allowed:
                   if status_codes.get(l[-2], -1) == -1:
                       status_codes[l[-2]] = 1
                   else:
                       status_codes[l[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

        except KeyboardInterrupt:
            print(size, status_codes)
            raise
