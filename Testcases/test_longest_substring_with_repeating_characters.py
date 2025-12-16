import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Solution.longest_substring_without_repeating import lengthOfLongestSubstring
import pytest

@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),     # "abc"
        ("bbbbb", 1),        # "b"
        ("pwwkew", 3),       # "wke"
        ("", 0),             # empty string
        (" ", 1),            # single space
        ("au", 2),            # entire string valid
        ("dvdf", 3),          # "vdf"
        ("anviaj", 5),        # "nviaj"
    ],
    ids=[
        "Repeating pattern",
        "All same characters",
        "Repeats with gap",
        "Empty string",
        "Single whitespace",
        "Two unique chars",
        "Overlap repeat",
        "Long unique suffix",
    ]
)
def test_length_of_longest_substring(s, expected):
    assert lengthOfLongestSubstring(s) == expected