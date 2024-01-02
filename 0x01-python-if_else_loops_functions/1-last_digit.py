#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_last = number % 10
if (last_last == 6) and (last_last != 0):
    print(f"Last digit of {number} is {last_last} and is less than 6 and not\
    0")
elif (last_last == 0):
    print(f"Last digit of {number} is {last_last} and is 0")
elif (last_last > 5):
    print(f"Last digit of {number} is {last_last} and is greater than 5")
