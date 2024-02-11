#!usr/bin/python3
"""Model that inherits from rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Inits an instance of class Square"""
        super().__init__(size, size, x, y, id)


    def __str__(self):
        """Overload for square"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
