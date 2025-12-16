import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Solution.Two_sum_II import twoSumII
import pytest

import pytest

@pytest.mark.parametrize(
    "numbers, target, expected",
    [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
    ],
    ids=[
        "Example 1",
        "Example 2",
        "Example 3"
    ]
)
def test_two_sum(numbers, target, expected):
    assert twoSumII(numbers, target) == expected
