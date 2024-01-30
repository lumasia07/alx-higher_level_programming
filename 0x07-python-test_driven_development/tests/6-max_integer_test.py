#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer"""

    def test_ordered(self):
        """Test odererd list"""
        i = [1, 2, 3, 4]
        self.assertEqual(max_integer(i), 4)

    def test_unordered(self):
        """Test unodererd list"""
        i = [1, 4, 3, 2]
        self.assertEqual(max_integer(i), 4)

    def test_max_at_begginning(self):
        """Test max at beggining of list"""
        i = [4, 3, 2, 1]
        self.assertEqual(max_integer(i), 4)

    def test_empty(self):
        """Test empty list"""
        i = []
        self.assertEqual(max_integer(i), None)

    def test_one_element(self):
        """Test one element list"""
        i = [4]
        self.assertEqual(max_integer(i), 4)

    def test_float(self):
        """Test floats list"""
        i = [1.5, 2.5, 3.5, 4.5]
        self.assertEqual(max_integer(i), 4.5)

    def test_float_int(self):
        """Test float and int in list"""
        i = [1.5, 2, 3, 4]
        self.assertEqual(max_integer(i), 4)

    def test_str(self):
        """Test str in list"""
        i = "Lumasia"
        self.assertEqual(max_integer(i), 'u')

    def test_str_list(self):
        """Test strings in list"""
        i = ["One", "Two", "Three", "name"]
        self.assertEqual(max_integer(i), "name")
    
    def test_empty_str(self):
        """Test empty strings in  list"""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()






