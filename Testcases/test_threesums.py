import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Solution.ThreeSums import threeSum
import pytest

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        ([], []),
        ([3, -2, 1, 0], []),
    ],
    ids=[
        "Standard Case",
        "No Triplet Sum Zero",
        "All Zeros",
        "Empty Input",
        "No Valid Triplets"
    ]
)
def test_three_sum(nums, expected):
    result = threeSum(nums)
    
    result_sorted = sorted([sorted(x) for x in result])
    expected_sorted = sorted([sorted(x) for x in expected])
    assert result_sorted == expected_sorted