#!/usr/bin/python3
"""
This is the "test_base" module
The test_base module suppies a class to test class Base
"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Test class Base
    """

    def test_base_id(self):
        """
        This functions tests assigned id for class creation
        """
        test_1 = Base()
        test_2 = Base()
        test_3 = Base(77)
        test_4 = Base(None)
        self.assertIsInstance(test_1, Base)
        self.assertEqual(test_1.id, 1)
        self.assertEqual(test_2.id, 2)
        self.assertEqual(test_3.id, 77)
        self.assertEqual(test_4.id, 3)

# ---------------------------------------------------------------

    def test_base_to_json_string(self):
        """
        This function test if the method to_json_string returns
        the JSON string representation ofdictionaries list
        """
        dict_test = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]
        self.assertTrue(type(Base.to_json_string(dict_test)), str)
        self.assertEqual(Base.to_json_string(
            dict_test), '[{"a": 1, "b": 2}, {"c": 3, "d": 4}]')
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(None), "[]")

# --------------------------------------------------------------
    def test_base_from_json_string(self):
        """
        This function test if the method from_json_string returns
        the list of the JSON string representation
        """
        json_str = '[{"a": 1, "b": 2}, {"c": 3, "d": 4}]'
        self.assertTrue(type(Base.from_json_string(json_str)), list)
        self.assertTrue(
            all(type(elt) is dict for elt in Base.from_json_string(
                json_str)), dict)
        self.assertEqual(Base.from_json_string(json_str), [
                         {"a": 1, "b": 2}, {"c": 3, "d": 4}])
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])

#
