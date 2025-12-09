import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Solution.k_frequent_elements import topKFrequent
import pytest

@pytest.mark.parametrize("nums,k, expected",[([1,1,1,2,2,3],2,[1,2]),([1,2,1,2,1,2,3,1,3,2],2,[1,2])],ids=["Test Case 1","Test Case 2"])

def test_k_frequent_elements(nums,k, expected):
    assert topKFrequent(nums,k) == expected