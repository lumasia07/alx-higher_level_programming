#!/usr/bin/python3
"""Module to base class"""


import json
import csv
import os
import turtle


class Base:
    """Defines a class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor for Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_directories):
        """Returns JSON to list dirs"""
        if list_directories is None or len(list_directories) == 0:
            return "[]"
        else:
            return json.dumps(list_directories)

    @staticmethod
    def from_json_string(json_string):
        """Returns a list of dicts"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        "Returns an instance with all attrs"""
        if cls.__name__ == "Rectangle":
            d = cls(1, 1)
        elif cls.__name__ == "Square":
            d = cls(1)
        d.update(**dictionary)
        return d
    
    @classmethod
    def load_from_file(cls):
        f_name = cls.__name__ + ".json"
        s = []
        try:
            with open(f_name, 'r') as f:
                s = cls.from_json_string(f.read())
            for i, j in enumerate(s):
                s[i] = cls.create(**s[i])
        except:
            pass
        return s

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON to a file"""
        if list_objs is None:
            list_objs = []
        f_name = cls.__name__ + ".json"
        with open(f_name, 'w') as f:
            s = cls.to_json_string([o.to_dictionary() for o in list_objs])
            f.write(s)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize objects to CSV"""
        f = cls.__name__ + ".csv"
        with open(f, 'w', newline='') as cs:
            wt = csv.writer(cs)
            for i in list_objs:
                if cls.__name__ == "Rectangle":
                    wt.writerow([i.id, i.width, i.height, i.x, i.y])
                elif cls.__name__ == "Square":
                    wt.writerow([i.id, i.size, i.x, i.y])


    @classmethod
    def load_from_file_csv(cls):
        """Decentralize object from the CSV"""
        f = cls.__name__ + ".csv"
        objs = []
        with open(f, 'r') as cs:
            rd = csv.reader(cs)
            for row in rd:
                if cls.__name__ == "Rectangle":
                    j = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                elif cls.__name__ == "Square":
                    j = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                objs.append(j)
        return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all Rectangles and Squares"""
        s = turtle.Screen()
        s.setup(width=800, height=600)
        s.title("Draw")
        s.bgcolor("blue")
        s.tracer(0)

        p = turtle.Turtle()
        p.speed(0)


        for rectangle in list_rectangles:
            p.penup()
            p.goto(rectangle.x, rectangle.y)
            p.pendown()
            p.color("yellow")
            p.begin_fill()
            for _ in range(2):
                p.forward(rectangle.width)
                p.left(90)
                p.forward(rectangle.height)
                p.left(90)
            p.end_fill()

        for square in list_squares:
            p.penup()
            p.goto(square.x, square.y)
            p.pendown()
            p.color("grey")
            p.begin_fill()
            for _ in range(4):
                p.forward(square.size)
                p.left(90)
            p.end_fill()

        s.update()
        s.mainloop()

