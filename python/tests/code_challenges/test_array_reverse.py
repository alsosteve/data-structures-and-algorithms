import pytest_lazyfixture
from ...code_challenges.array_reverse import reverse

nums = [ 1, 2, 3, 4, 6, 7, 8, 9 ]

def test_reverse():
    actual = reverse(nums)
    expected = [ 9, 8, 7, 6, 5, 4, 3, 2, 1 ]
    assert actual == expected