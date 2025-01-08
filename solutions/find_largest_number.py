#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding the largest number in a list.
Module contents:
    - find_largest_number: A function to find the largest number in a list.
Created on 2025-01-07
@author: Saliha Kalender
"""


def find_largest_number(numbers: list) -> int:
    """
    Find the largest number in a list.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        int: The largest number in the list.

    Raises:
        TypeError: If the input is not a list.
        ValueError: If the list is empty or contains non-integer elements.

    Examples:
        >>> find_largest_number([1, 2, 3, 4])
        4
        >>> find_largest_number([-10, -20, -30, -5])
        -5
        >>> find_largest_number([42])
        42
    """
    if not isinstance(numbers, list):
        raise TypeError("Invalid input: Expected a list of integers.")
    if not numbers:
        raise ValueError("The list is empty.")
    if not all(isinstance(num, int) for num in numbers):
        raise ValueError("All elements in the list must be integers.")

    return max(numbers)
