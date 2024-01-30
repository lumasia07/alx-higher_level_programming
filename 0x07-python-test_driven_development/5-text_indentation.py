#!/usr/bin/python3
"""

Module that prints a text with 2 new lines

"""


def text_indentation(text):
    """
    Defines a function to print text with two new lines
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    counter = 0
    while counter < len(text) and text[counter] == " ":
        counter += 1

    while counter < len(text):
        print(text[counter], end="")
        if text[counter] == "\n" or text[counter] in ".?:":
            if text[counter] in ".?:":
                print("\n")
            counter += 1
            while counter < len(text) and text[counter] == " ":
                counter += 1
            continue
        counter += 1
