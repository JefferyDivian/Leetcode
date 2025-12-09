import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Solution.Group_Anagram import groupAnagrams
import pytest
from pytest_unordered import unordered

@pytest.mark.parametrize("strs, expected",[(["eat","tea","tan","ate","nat","bat"],[["bat"],["tan","nat"],["eat","tea","ate"]]),(["a"],[["a"]])],ids=["Test Case 1","Test Case 2"])

def test_groupAnagrams(strs, expected):
    assert groupAnagrams(strs) == unordered(expected)