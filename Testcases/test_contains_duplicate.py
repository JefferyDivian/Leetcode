import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Solution.contains_duplicate import containsDuplicate
import pytest
@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 3], True),      # Test Case 1
        ([1, 2, 3, 4], False),     # Test Case 2
        ([], False),               # Test Case 3 - empty list
        ([0], False),              # Test Case 4 - single element
        ([1, 1, 1, 1], True),      # Test Case 5 - all duplicates
        ([3, 1, 4, 2, 5], False),  # Test Case 6 - no duplicates
        ([-1, -2, -3, -1], True),  # Test Case 7 - negative duplicates
    ],
    ids=[
        "Duplicate exists",
        "No duplicates",
        "Empty list",
        "Single element",
        "All duplicates",
        "Unique list",
        "Negative numbers duplicate"
    ]
)
def test_contains_duplicate(nums, expected):
    assert containsDuplicate(nums) == expected
