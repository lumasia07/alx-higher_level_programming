#!/usr/bin/python3
"""Module to unittest Base Model"""


import unittest
from models.base import Base
import os
import csv
import json


class TestBase(unittest.TestCase):
    """Defines a unittest Base"""
    def setUp(self):
        self.b1 = Base(1)
        self.b2 = Base()
        self.j_data =[{"id": 1, "width": 2, "height": 3, "x": 4, "y": 5}, {"id": 2, "size": 3, "x": 4, "y": 5}]
        self.csv_data = [[1, 2, 3, 4, 5], [2, 3, 4, 5]]

    def test_construcutor(self):
        """Tests init to Base class"""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 1)

    def test_json_encoder(self):
        """Tests for encoder"""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        j = Base.to_json_string(self.j_data)
        self.assertEqual(json.loads(j), self.j_data)

    def test_json_decoder(self):
        """Tests for decoder"""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        j = json.dumps(self.j_data)
        self.assertEqual(Base.from_json_string(j), self.j_data)

    def test_save(self):
        """Test file saved"""
        Base.save_to_file([])
        self.assertTrue(os.path.exists("Base.json"))
        os.remove("Base.json")

    def test_csv(self):
        """Test csv file"""
        Base.save_to_file_csv([])
        self.assertTrue(os.path.exists("Base.csv"))
        os.remove("Base.csv")

if __name__ == '__main__':
    unittest.main()


