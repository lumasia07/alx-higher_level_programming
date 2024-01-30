#!/usr/bin/python3
"""Module that defines a rectangle"""


class Rectangle:
    """Defines class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Inits class rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate area"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self) -> str:
        """prints informal str"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rec_str = ""

        for _ in range(self.__height):
            rec_str += str(self.print_symbol) * self.__width + '\n'

        return rec_str.rstrip()

    def __repr__(self):
        """Return str rep for recreating object"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print message on instance deletion"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare rectangles"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        x = rect_1.area()
        y = rect_2.area()

        if x >= y:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Creates square"""
        return cls(size, size)