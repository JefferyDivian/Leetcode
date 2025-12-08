import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Solution.Two_sum import twoSum
import pytest

@pytest.mark.parametrize("nums, target,expected",[([2,7,11,15],9,(0,1)),([3,2,4],6,(1,2))],ids=["Test Case 1","Test Case 2"])

def test_two_sum(nums,target, expected):
    assert twoSum(nums,target) == expected