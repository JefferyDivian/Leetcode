import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Solution.product_of_array_except_self import productExceptSelf
import pytest

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),            # Example 1
        ([2, 3, 4, 5], [60, 40, 30, 24]),          # Basic case
        ([1, 1, 1, 1], [1, 1, 1, 1]),              # All ones
        ([5, 0, 2], [0, 10, 0]),                   # Contains zero
        ([0, 0, 3], [0, 0, 0]),                    # Two zeros
        ([10], [1]),                               # Single element
    ],
    ids=[
        "Case 1 - [1,2,3,4]",
        "Case 2 - [2,3,4,5]",
        "Case 3 - all ones",
        "Case 4 - one zero",
        "Case 5 - two zeros",
        "Case 6 - single element"
    ]
)
def test_productExceptSelf(nums, expected):
    assert productExceptSelf(nums) == expected