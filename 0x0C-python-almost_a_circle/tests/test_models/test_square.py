#!/usr/bin/python3
"""unittest for Square model"""

import sys
import io
import unittest
from models.square import Square


class TestRectangle(unittest.TestCase):
    """Defines test case for Square model"""
    def test_constructor(self):
        """Test for initalizer"""
        r = Square(3, 4, 1, 2)
        self.assertEqual(r.size, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 2)

    def test_size(self):
        """Test validity of size"""
        with self.assertRaises(TypeError):
            r = Square("3", 4, 1, 2)
        with self.assertRaises(ValueError):
            r = Square(-3, 4, 1, 2,)

    def test_x(self):
        """Test validity of x"""
        with self.assertRaises(TypeError):
            r = Square(3, "4", 1, 2)
        with self.assertRaises(ValueError):
            r = Square(3, -4, 1, 2)

    def test_y(self):
        """Test validity of y"""
        with self.assertRaises(TypeError):
            r = Square(3, 4, "1", 2)
        with self.assertRaises(ValueError):
            r = Square(3, 4, -1, 2)

    def test_area(self):
        """Tests area"""
        r = Square(3)
        self.assertEqual(r.area(), 9)

    def test_str(self):
        """Test string rep"""
        r = Square(3, 4, 1, 2)
        self.assertEqual(str(r), "[Square] (2) 4/1 - 3")

    def test_update(self):
        """Test for updates"""
        r = Square(3, 4, 1, 2)
        r.update(7, 8, 9, 10)
        self.assertEqual(r.size, 8)
        self.assertEqual(r.x, 9)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.id, 7)

    def test_to_dictionary(self):
        r = Square(3, 4, 1, 2)
        expected = {'id': 2, 'size': 3, 'x': 4, 'y': 1}
        self.assertEqual(r.to_dictionary(), expected)

if __name__ == '__main__':
    unittest.main()

