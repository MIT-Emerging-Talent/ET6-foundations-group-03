"""
Module: sort_and_append

    A utility that sorts a list and appends it to another list. It works with lists containing any type of elements.

Created: 2025/01/09
Author: Mohammad
"""

from typing import List, Any  # Import List and Any for type annotations


def sort_and_append(source: List[Any], target: List[Any]) -> List[Any]:
    """
    Sort the items in the source list and append them to the target list.

    Parameters:
    source (List[Any]): A list of elements to be sorted.
    target (List[Any]): A list where sorted elements will be appended.

    Returns:
    List[Any]: The target list after the sorted elements from the source are appended.

    Example:
    >>> sort_and_append([3, 1, 2], [])
    [1, 2, 3]

    >>> sort_and_append(["Canada", "Us"], ["Afghanistan", "Pakistan"])
    ['Afghanistan', 'Pakistan', 'Canada', 'Us']

    >>> sort_and_append([], ["Hello", "Mohammad"])
    ['Hello', 'Mohammad']

    >>> sort_and_append("not_a_list", [])
    Raises: AssertionError: source must be a list
    """

    # Assertion to check that source is a list
    assert isinstance(source, list), "source must be a list"
    target.extend(sorted(source))
    return target
