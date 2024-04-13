#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""

    def test_empty_list(self):
        """Test max_integer with an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_single_element(self):
        """Test max_integer with a single element list"""
        self.assertEqual(max_integer([98]), 98)

    def test_identical_elements(self):
        """Test max_integer with a list of identical elements"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_ordered_elements(self):
        """Test max_integer with a list of ordered elements"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_elements(self):
        """Test max_integer with a list of unordered elements"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_mixed_integer_types(self):
        """Test max_integer with a list containing mixed integer types"""
        self.assertEqual(max_integer([-23, 58, 91, 24, -1024, 89, 98,
                                     108, -256, -512]), 108)

    def test_mixed_numeric_types(self):
        """Test max_integer with a list containing mixed numeric types"""
        self.assertEqual(max_integer([10, 99.8, -100, -0.1, 1000, 9999,
                                      -100000, 9998.9]), 9999)

    def test_numeric_string(self):
        """Test max_integer with a numeric string"""
        self.assertEqual(max_integer("192834754"), "9")

    def test_list_of_lists(self):
        """Test max_integer with a list of lists"""
        self.assertEqual(max_integer([[], [2], [4], [2, 9]]), [4])

    def test_floats(self):
        """Test max_integer with a list of floating point numbers"""
        self.assertEqual(max_integer([.00123, .457568, .02345, .23423434,
                                       .45675674, .678678, .867090, .74653,
                                       .5745375]), 0.86709)

    def test_mixed_list(self):
        """Test max_integer with a mixed list"""
        with self.assertRaises(TypeError):
            max_integer([[], [2], [4], [2, 9], 99, "foo"])

    def test_none(self):
        """Test max_integer with None"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_invalid_input(self):
        """Test max_integer with invalid input"""
        with self.assertRaises(TypeError):
            max_integer([{20: 23, 14: 45}, {"a": "b"}])

if __name__ == '__main__':
    unittest.main()
