import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Solution.Container_with_most_water import maxArea
import pytest

@pytest.mark.parametrize(
    "height, expected",
    [
        ([1,8,6,2,5,4,8,3,7], 49),   # Standard example
        ([1,1], 1),                 # Only two walls
        ([4,3,2,1,4], 16),          # Max area between outer walls
        ([1,2,1], 2),               # Best between index 0 and 2
        ([2,3,10,5,7,8,9], 36),     # Known test case
    ],
    ids=[
        "Example 1",
        "Two Elements",
        "Symmetric Walls",
        "Small Valley",
        "Complex Case"
    ]
)
def test_max_area(height, expected):
    assert maxArea(height) == expected