"""Tests for fourth problem"""
import pytest
from solution import find_missing_positive_intiger

@pytest.mark.parametrize(
    "original_arr, expected",
    [
        ([3, 4, -1, 1], 2),
        ([1, 2, 0], 3),
        [[7,3,1,2,4,0,0,-12,3,1,6,5,9], 8],
        ([7, 8, 9, 11, 12], 1),
        ([1, 2, 3, 4, 5], 6),
        ([-1, -2, -3], 1),
        ([1, 1, 0, -1, -2], 2),
        ([2, 3, 4], 1),
        ([1], 2),
        ([2], 1),
        ([1, 2, 2, 3, 3, 4, 4, 5, 5], 6),
    ],
)
def test_should_return_missing_positive_number(
        original_arr: list, expected: int
    ) -> None:
    """
    Test whether function returns missing positive
    number based on given array 
    """
    assert find_missing_positive_intiger(original_arr) == expected
