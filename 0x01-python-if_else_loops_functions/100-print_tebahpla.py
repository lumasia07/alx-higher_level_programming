#!/usr/bin/python3
for x in range(90, 64, -1):
    if x % 2 == 0:
        i = 0
    else:
        i = 32
    print('{}'.format(chr(x - i)), end='')
