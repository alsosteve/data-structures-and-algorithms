import pytest
from code_challenges.merge_sort import merge_sort

one = [8, 4, 23, 42, 16, 15]
two = [20,18,12,8,5,-2]
three = [5,12,7,5,5,7]
four = [2,3,5,7,13,11]

# @pytest.mark.skip("TODO")
def test_list_one():
    actual = merge_sort(one)
    expected = [4, 8, 15, 16, 23, 42]
    print(actual)
    assert actual == expected

@pytest.mark.skip("TODO")
def test_list_two():
    actual = merge_sort(two)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

@pytest.mark.skip("TODO")
def test_list_three():
    actual = merge_sort(three)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

@pytest.mark.skip("TODO")
def test_list_four():
    actual = merge_sort(four)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
