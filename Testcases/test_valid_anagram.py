import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Solution.Valid_Anagram import isAnagram
import pytest

@pytest.mark.parametrize("s,t, expected",[("anagram","nagaram",True),("rat","car",False)],ids=["Test Case 1","Test Case 2"])

def test_valid_anagram(s,t, expected):
    assert isAnagram(s,t) == expected