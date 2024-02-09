#!/usr/bin/python3
"""Module to class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Defines a class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new instance of class Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        self.__width

    @width.setter
    def width(self, val):
        if not isinstance(val, int):
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = val

    @property
    def height(self):
        self.__height
        
    @height.setter
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = val

    @property
    def x(self):
        self.__x

    @x.setter
    def x(self, val):
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = val

    @property
    def y(self):
        self.__y

    @y.setter
    def y(self, val):
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be > 0")
        else:
            self.__y = val

    def area(self):
        """returns area"""
        return self.__width * self.__height

    def display(self):
        """Display with #"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def __str__(self):
        """Returns the string rep of the rectangle instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        if args and len(args) != 0:
            counter = 0
            for _ in args:
                if counter == 0:
                    if _ is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = _
                elif counter == 1:
                    self.width = _
                elif counter == 2:
                    self.height = _
                elif counter == 3:
                    self.x = _
                elif counter == 4:
                    self.y = _
                counter += 1
        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    if j is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = j
                elif i == "width":
                    self.width = j
                elif i == "height":
                    self.height = j
                elif i == "x":
                    self.x = j
                elif i == "y":
                    self.y = j
