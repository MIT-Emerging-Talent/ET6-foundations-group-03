#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the find_largest_number function.

Created on 2025-01-07
@author: Saliha Kalender
"""

import unittest
from find_largest_number import find_largest_number


class TestFindLargestNumber(unittest.TestCase):
    # Unit tests for the `find_largest_number` function.

    def test_positive_numbers(self):
        # Test the function with a list of positive numbers.
        self.assertEqual(find_largest_number([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        # Test the function with a list of negative numbers.
        self.assertEqual(find_largest_number([-10, -20, -30, -5]), -5)

    def test_mixed_numbers(self):
        # Test the function with a list of mixed positive and negative numbers.
        self.assertEqual(find_largest_number([-1, 0, 1]), 1)

    def test_single_element(self):
        # Test the function with a list containing a single element.
        self.assertEqual(find_largest_number([42]), 42)

    def test_empty_list(self):
        # Test that a ValueError is raised for an empty list.
        with self.assertRaises(ValueError) as context:
            find_largest_number([])
        self.assertEqual(str(context.exception), "The list is empty.")

    def test_non_integer_list(self):
        # Test that a ValueError is raised when the list contains non-integer elements.
        with self.assertRaises(ValueError) as context:
            find_largest_number([1, 2, "a"])
        self.assertEqual(
            str(context.exception), "All elements in the list must be integers."
        )

    def test_non_list_input(self):
        # Test that a TypeError is raised when the input is not a list.
        with self.assertRaises(TypeError) as context:
            find_largest_number(123)
        self.assertEqual(
            str(context.exception), "Invalid input: Expected a list of integers."
        )


# Run the unit tests when this script is executed

if __name__ == "__main__":
    unittest.main()
