#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module tests the largest element function which returns the largest
element in a list of numbers.

Created on Dec 21, 2024

@author: Meklit Gebregiorgis
"""

import sys
import os
import unittest

# Allow modifying sys.path before imports
# pylint: disable=wrong-import-position
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from solutions.largest_element import largest_element
# pylint: enable=wrong-import-position


class TestLargeNumbers(unittest.TestCase):
    """Test for the largest_element function"""

    def test_positive_numbers(self):
        """It should correctly display the largest positive number"""
        actual = largest_element([1, 2, 3])
        expected = 3
        self.assertEqual(actual, expected)

    def test_negative_numbers(self):
        """It should correctly display the largest negative number"""
        actual = largest_element([-1, -2, -3])
        expected = -1
        self.assertEqual(actual, expected)

    def test_mixed_numbers(self):
        """It should correctly display the largest value"""
        actual = largest_element([-1, 0, 2.5])
        expected = 2.5
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        """It should correctly return None"""
        self.assertEqual(largest_element([]), None)
