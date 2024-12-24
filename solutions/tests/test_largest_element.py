#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module tests the largest element function which returns the largest 
element in a list of numbers

Created on Dec 21, 2024

@author: Meklit Gebregiorgis

"""

import unittest

# --- imports & test class before documenting and testing ---

# from ..largest_element import largest_element

# class Testlargenumbers(unittest.TestCase):

# --- imports & test class after documenting and testing ---

from ..largest_element import largest_element


class TestLargeNumbers(unittest.TestCase):
    """test for the largest_element function"""

    def test_positive_numbers(self):
        """It should correctly display the largest positive number"""
        actual = largest_element([1,2,3])
        expected = 3
        self.assertEqual(actual, expected)

    def test_negative_numbers(self):
        """It should correctly display the largest negative number"""
        actual = largest_element([-1,-2,-3])
        expected = -1
        self.assertEqual(actual, expected)

    def test_mixed_numbers(self):
        """It should correctly display the largest value"""
        actual = largest_element([-1,0,2.5])
        self.assertEqual(actual, 2.5)

    def test_empty_list(self):
        """It should correctly return None"""
        self.assertEqual(largest_element([]),None)
