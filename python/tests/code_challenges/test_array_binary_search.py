'''import pytest
from ...code_challenges.array_binary_search import binary_search

nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
low = 0
high = len(nums)-1

def test_search_zero():
    actual = binary_search(nums, 0, low, high)
    expected = -1
    assert actual == expected

def test_search_one():
    actual = binary_search(nums, 1, low, high)
    expected = 1
    assert actual == expected

def test_search_five():
    actual = binary_search(nums, 5, low, high)
    expected = 5
    assert actual == expected

def test_search_eight():
    actual = binary_search(nums, 8, low, high)
    expected = 8
    assert actual == expected

def test_search_ten():
    actual = binary_search(nums, 10, low, high)
    expected = -1
    assert actual == expected'''
