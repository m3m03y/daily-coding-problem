"""Tests for first problem"""
import pytest
from solution import if_sum_from_list_eq_k

@pytest.mark.parametrize(
    "k, numbers",
    [
        (17, [10, 15, 3, 7]),
        (2, [1,1]),
        (100, [20, 50, 60, 40, 80]),
        (8, [8, 1, 2, 0, 4]),
    ],
)
def test_should_return_true(
        k: int, numbers: list
    ) -> None:
    """
    Test when list of numbers does contain a pair
    that sum up to k value.
    """
    assert if_sum_from_list_eq_k(k, numbers)

@pytest.mark.parametrize(
    "k, numbers",
    [
        (1, [1, 1, 3, 2]),
        (0, [1]),
        (0, []),
        (1, [1])
    ],
)
def test_should_return_false(
        k: int, numbers: list
    ) -> None:
    """
    Test when list of numbers does not contain a pair
    that sum up to k value.
    """
    assert not if_sum_from_list_eq_k(k, numbers)
