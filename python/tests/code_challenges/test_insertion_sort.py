import pytest
from code_challenges.insertion_sort import insertion_sort

one = [8, 4, 23, 42, 16, 15]
two = [20,18,12,8,5,-2]
three = [5,12,7,5,5,7]
four = [2,3,5,7,13,11]

# @pytest.mark.skip("TODO")
def test_list_one():
    actual = insertion_sort(one)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_list_two():
    actual = insertion_sort(two)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_list_three():
    actual = insertion_sort(three)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

# @pytest.mark.skip("TODO")
def test_list_four():
    actual = insertion_sort(four)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
