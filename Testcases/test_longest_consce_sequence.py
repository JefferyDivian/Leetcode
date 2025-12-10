
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Solution.longest_consce_sequence import longestConsecutive
import pytest

@pytest.mark.parametrize(
    "nums, expected",
    [
        ([100, 4, 200, 1, 3, 2], 4),          # longest sequence = [1,2,3,4]
        ([1, 2, 2, 3], 3),                    # duplicates included
        ([], 0),                              # empty list
        ([7], 1),                             # single element
        ([9,1,4,7,3,-1,0,5,8,-1,6], 7),       # longest = [-1,0,1,3...?] Actually 0–9 missing 2; longest = [3..9]=7
    ],
    ids=[
        "Basic Case",
        "With Duplicates",
        "Empty List",
        "Single Element",
        "Mixed & Unordered"
    ]
)
def test_longest_consecutive(nums, expected):
    assert longestConsecutive(nums) == expected