"""
largest_element.py

This module contains the implementation of the largest_element function,
which checks values of numbers in the list and returns the largest value.

Functions:
- largest_element(numbers: list) -> int | float | None: Returns the largest element in a list.

Example:
>>> largest_element([-1, 0, 1])
1
>>> largest_element([1, 2, 3])
3
>>> largest_element([-1, 0, 2.5])
2.5
"""


def largest_element(numbers: list) -> int | float | None:
    """
    Returns the largest element in a list of numbers.

    Parameters:
    numbers (list): list of numbers

    Returns:
    int/float: The largest number from the list, or None if the list is empty.
    """
    assert all(
        isinstance(num, (int, float)) for num in numbers
    ), "num must be integer or float"
    if not numbers:  # checks if the list is empty
        return None  # if the list is empty returns none

    largest = numbers[0]  # This takes the first element from the list
    for num in numbers:  # This loops through the list
        largest = max(
            largest, num
        )  # This checks if each number is greater than the largest
    return largest  # return the largest number


if __name__ == "__main__":
    print(largest_element([1, 2, 3]))  # Simple print for debugging
