"""Tests for first problem"""
import pytest
from solution import create_new_array_from_sums

@pytest.mark.parametrize(
    "original_arr, new_arr",
    [
        ([1, 2, 3, 4, 5], [120, 60, 40, 30, 24]),
        ([3, 2, 1], [2, 3, 6]),
    ],
)
def test_should_return_true(
        original_arr: list, new_arr: list
    ) -> None:
    """
    Test whether new array contains elements
    that are a products of subsets in original
    array
    """
    assert create_new_array_from_sums(original_arr) == new_arr
