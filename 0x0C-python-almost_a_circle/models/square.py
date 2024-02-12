#!/usr/bin/python3
"""Model that inherits from rectangle"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Inits an instance of class Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """String rep for overload"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Updates Square attributes"""
        if args and len != 0:
            count = 0
            for i in args:
                if count == 0:
                    if i is not None:
                        self.id = i
                elif count == 1:
                    self.size = i
                elif count == 2:
                    self.x = i
                elif count == 3:
                    self.y = i
                count += 1
        elif kwargs:
            for i, j in kwargs.items():
                if i == "id":
                    if j is not None:
                        self.id = j
                elif i == "size":
                    self.size = j
                elif i == "x":
                    self.x = j
                elif i == "y":
                    self.y = j
