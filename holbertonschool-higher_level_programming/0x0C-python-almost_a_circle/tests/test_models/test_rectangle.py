#!/usr/bin/python3
"""
Unittest for "rectangle.py"

Execute all tests: python3 -m unittest discover tests
Execute this test: python3 -m unittest tests/test_models/test_rectangle.py
"""

import unittest
import pycodestyle
from models.base import Base
from models.rectangle import Rectangle
from os.path import exists


class TestRectangle(unittest.TestCase):
    """
    class that test the max integer function

    ValueError:
        negative width
        negative height
        negative x
        negative y
        zero width
        zero height
    
    TypeError:
        too many arguments
        too few arguments

        string width
        string height
        string x
        string y

        float width
        float height
        float x
        float y

        list width
        list height
        list x
        list y

        tuple width
        tuple height
        tuple x
        tuple y

        dict width
        dict height
        dict x
        dict y

        None width
        None height
        None x
        None y

    __str__
        test the __str__ function of Rectangle

    area
        test the area function of Rectangle

    display
        Don't know how to test !

    update
        test the update function of Rectangle

    to_dictionary
        test the to_dictionary function of Rectangle
    """
    def test_documentation(self):
        """test all documentation of module"""
        # module documentation
        module = len(__import__("models.rectangle").__doc__)
        self.assertGreater(module, 0)

        # class documentation
        module_class = len(Rectangle.__doc__)
        self.assertGreater(module_class, 0)

        # function documentation
        # not implemented

    def test_subclass(self):
        """fuction that test if Rectangle is a subclass of Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_conformance(self):
        """Test that we conform to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (pycodestyle).")

    def test_valid(self):
        """fuction that test for good assignment of differents value"""
        r1 = Rectangle(10, 2, 34, 121, 45027310974)
        self.assertEqual(r1.id, 45027310974)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 34)
        self.assertEqual(r1.y, 121)

        r2 = Rectangle(10, 2, 5, 65, None)
        self.assertGreater(r2.id, 0)
        self.assertEqual(r2.width, 10)
        self.assertEqual(r2.height, 2)
        self.assertEqual(r2.x, 5)
        self.assertEqual(r2.y, 65)

        r3 = Rectangle(10, 2)
        self.assertGreater(r3.id, 0)
        self.assertEqual(r3.width, 10)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 0)
        self.assertEqual(r3.y, 0)

##########################################################
# ValueError
##########################################################
    def test_negative_width(self):
        """fuction that test for ValueError"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)

    def test_negative_height(self):
        """fuction that test for ValueError"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2)
            r1.width = -10

    def test_negative_x(self):
        """fuction that test for ValueError"""
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -1, 2)

    def test_negative_y(self):
        """fuction that test for ValueError"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 3, 4)
            r1.y = -10

    def test_zero_width(self):
        """fuction that test for ValueError"""
        with self.assertRaises(ValueError):
            Rectangle(0, 2)

    def test_zero_height(self):
        """fuction that test for ValueError"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(10, 2)
            r1.width = 0

##########################################################
# TypeError
##########################################################

    def test_too_many_arguments(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_too_few_arguments(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1)

# string
    def test_string_width(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle("hello", 2)

    def test_string_height(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, "world")

    def test_string_x(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "hello", 4)

    def test_string_y(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "World")

# float
    def test_float_width(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1.1, 2)

    def test_float_height(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2.2)

    def test_float_x(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3.3, 4)

    def test_float_y(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4.4)

# list
    def test_list_width(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle([1, 1], 2, 3, 4)

    def test_list_height(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, [2, 2], 3, 4)

    def test_list_x(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, [3, 3], 4)

    def test_list_y(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, [4, 4])

# tuple
    def test_tuple_width(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle((1, 1), 2, 3, 4)

    def test_tuple_height(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, (2, 2), 3, 4)

    def test_tuple_x(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, (3, 3), 4)

    def test_tuple_y(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, (4, 4))

# dict
    def test_dict_width(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle({"hello": 12}, 2, 3, 4)

    def test_dict_height(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, {"hello": 12}, 3, 4)

    def test_dict_y(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, {"hello": 12}, 4)

    def test_dict_x(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, {"hello": 12})

# None
    def test_None_width(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(None, 2, 3, 4)

    def test_None_height(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, None, 3, 4)

    def test_None_y(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, None, 4)

    def test_None_x(self):
        """fuction that test for TypeError"""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, None)

##########################################################
# __str__
##########################################################

    def test___str__(self):
        """fuction that test for __str__()"""
        r1 = Rectangle(1, 2, 0, 0, 1212121212)
        self.assertEqual(r1.__str__(), "[Rectangle] (1212121212) 0/0 - 1/2")

##########################################################
# area
##########################################################

    def test_area(self):
        """fuction that test for area()"""
        r1 = Rectangle(12, 43)
        self.assertEqual(r1.area(), 516)

##########################################################
# display
##########################################################

    # Don't know

##########################################################
# update
##########################################################

    def test_update(self):
        """fuction that test for update()"""
        r1 = Rectangle(7, 3, 2, 4)
        r1.update(1234567890, 1, 2, 3, 4)

        self.assertEqual(r1.id, 1234567890)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 4)

        r1.update(width=131)
        self.assertEqual(r1.width, 131)
        self.assertEqual(r1.height, 2)

        r1.update(height=454, width=331, y=1)
        self.assertEqual(r1.width, 331)
        self.assertEqual(r1.height, 454)
        self.assertEqual(r1.y, 1)

        r1.update()
        self.assertEqual(r1.height, 454)

##########################################################
# to_dictionary
##########################################################

    def test_to_dictionary(self):
        """fuction that test for to_dictionary()"""
        r1 = Rectangle(1, 2, 3, 4, 1234567890)
        self.assertEqual(r1.to_dictionary(), {'id': 1234567890, 'width': 1, 'height': 2, 'x': 3, 'y': 4})


if __name__ == '__main__':
    unittest.main()
