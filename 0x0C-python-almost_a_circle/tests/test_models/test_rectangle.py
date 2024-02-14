#!/usr/bin/python3
"""unittest for Rectangle model"""

import sys
import io
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Defines test case for Rectangle model"""
    def test_constructor(self):
        """Test for initalizer"""
        r = Rectangle(3, 4, 1, 2, 6)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 6)

    def test_width(self):
        """Test validity of width"""
        with self.assertRaises(TypeError):
            r = Rectangle("3", 4, 1, 2, 6)
        with self.assertRaises(ValueError):
            r = Rectangle(-3, 4, 1, 2, 6)

    def test_height(self):
        """Test validity of height"""
        with self.assertRaises(TypeError):
            r = Rectangle(3, "4", 1, 2, 6)
        with self.assertRaises(ValueError):
            r = Rectangle(3, -4, 1, 2, 6)

    def test_x(self):
        """Test validity of x"""
        with self.assertRaises(TypeError):
            r = Rectangle(3, 4, "1", 2, 6)
        with self.assertRaises(ValueError):
            r = Rectangle(3, 4, -1, 2, 6)

    def test_y(self):
        """Test validity of y"""
        with self.assertRaises(TypeError):
            r = Rectangle(3, 4, 1, "2", 6)
        with self.assertRaises(ValueError):
            r = Rectangle(-3, 4, 1, -2, 6)

    def test_area(self):
        """Tests area"""
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_display(self):
        """Tests Display"""
        r = Rectangle(2, 3)
        expect = "##\n##\n##\n"
        with unittest.mock.patch('sys.stdout', new=io.StringIO()) as f:
            r.display()
            self.assertEqual(f.getvalue(), expect)
    
    def test_str(self):
        """Test string rep"""
        r = Rectangle(3, 4, 1, 2, 6)
        self.assertEqual(str(r), "[Rectangle] (6) 1/2 - 3/4")

    def test_update(self):
        """Test for updates"""
        r = Rectangle(3, 4, 1, 2, 6)
        r.update(7, 8, 9, 10, 12)
        self.assertEqual(r.width, 8)
        self.assertEqual(r.height, 9)
        self.assertEqual(r.x, 10)
        self.assertEqual(r.y, 12)
        self.assertEqual(r.id, 7)

    def test_to_dictionary(self):
        r = Rectangle(3, 4, 1, 2, 6)
        expected = {'id': 6, 'width': 3, 'height': 4, 'x': 1, 'y': 2}
        self.assertEqual(r.to_dictionary(), expected)

if __name__ == '__main__':
    unittest.main()

