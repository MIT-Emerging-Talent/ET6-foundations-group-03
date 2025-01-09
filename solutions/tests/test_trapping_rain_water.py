"""
Test cases for the `trap` function, which calculates the amount of rainwater
that can be trapped given an elevation map.

The `trap` function is tested with various scenarios, including edge cases,
to ensure accuracy and robustness.
"""

import os
import sys

# Add the parent directory to the system path for importing the `trap` function.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Import the `trap` function from the solution file
from solutions.trapping_rain_water import trap


def test_trap():
    """
    Tests the `trap` function with various input cases.
    Validates the correctness of the implementation for:
        - Empty elevation map
        - Single bar or two bars (no trapping possible)
        - Basic cases with small maps
        - Complex cases with valleys and multiple trapping regions
    """
    # Test case 1: Empty list
    # Expected output: 0, as no elevation bars are present.
    assert trap([]) == 0, "Failed on empty list"

    # Test case 2: Single bar
    # Expected output: 0, as one bar cannot trap any water.
    assert trap([1]) == 0, "Failed on single element"

    # Test case 3: Two bars
    # Expected output: 0, as two bars cannot trap any water.
    assert trap([1, 2]) == 0, "Failed on two bars"

    # Test case 4: Small trapping
    # Expected output: 1, as 1 unit of water is trapped between the bars.
    assert trap([0, 1, 0, 2]) == 1, "Failed on basic trapping case"

    # Test case 5: Complex trapping
    # Expected output: 9, as water is trapped in multiple valleys.
    assert trap([4, 2, 0, 3, 2, 5]) == 9, "Failed on complex trapping case"

    # Test case 6: Flat elevation
    # Expected output: 0, as no valleys exist to trap water.
    assert trap([3, 3, 3]) == 0, "Failed on flat elevation"

    # Test case 7: Increasing elevation
    # Expected output: 0, as the elevation consistently rises.
    assert trap([1, 2, 3, 4]) == 0, "Failed on increasing elevation"

    # Test case 8: Decreasing elevation
    # Expected output: 0, as the elevation consistently falls.
    assert trap([4, 3, 2, 1]) == 0, "Failed on decreasing elevation"

    # Test case 9: Mixed elevation
    # Expected output: 6, as water is trapped in two valleys.
    assert trap([0, 3, 0, 2, 0, 4]) == 7, "Failed on mixed elevation"

    # Test case 10: Single valley
    # Expected output: 3, as water is trapped in the single valley.
    assert trap([3, 0, 3]) == 3, "Failed on single valley case"


if __name__ == "__main__":
    # Run all tests
    test_trap()
    print("All tests passed successfully!")

# This is a formatting test
