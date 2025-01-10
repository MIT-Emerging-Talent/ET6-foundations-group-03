"""
Test Module: sort_and_append

    Unit tests for sort_and_append, covering empty lists, numbers, strings, and single-element cases.

Created: 2025/01/09
Author: Mohammad
"""

import unittest
from ..sort_and_append import sort_and_append


class TestSortAndAppend(unittest.TestCase):
    """Test module for sort_and_append function"""

    def test_empty_lists(self):
        """Cases in which both the source and target are empty."""
        self.assertEqual(sort_and_append([], []), [])

    def test_numbers_only(self):
        """Lists of numbers are sorted and appended."""
        self.assertEqual(sort_and_append([3, 1, 2], []), [1, 2, 3])
        self.assertEqual(sort_and_append([5, 4], [1, 2, 3]), [1, 2, 3, 4, 5])

    def test_strings_only(self):
        """Lists of strings can be sorted and appended."""
        self.assertEqual(
            sort_and_append(["Mohammad", "Meklit", "Mushtary"], []),
            ["Meklit", "Mohammad", "Mushtary"],
        )
        self.assertEqual(
            sort_and_append(["Canada", "Us"], ["Afghanistan", "Pakistan"]),
            ["Afghanistan", "Pakistan", "Canada", "Us"],
        )

    def test_mixed_empty_source(self):
        """Appends to the target when source is empty."""
        self.assertEqual(
            sort_and_append([], ["Hello", "Mohammad"]), ["Hello", "Mohammad"]
        )

    def test_single_item_source(self):
        """Handles cases where source has only one item."""
        self.assertEqual(sort_and_append([3], []), [3])
        self.assertEqual(sort_and_append(["single"], []), ["single"])

    def test_invalid_source_type(self):
        """The function is tested to check if it raises an AssertionError for an invalid source type."""
        with self.assertRaises(AssertionError):
            sort_and_append("not_a_list", [])


if __name__ == "__main__":
    unittest.main()  # Run all the unit tests
