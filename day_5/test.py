"""Tests for fourth problem"""
import pytest
from solution import cons, car, cdr

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 4, 3),
        (5, 10, 5),
        (-1, 0, -1),
        (100, 200, 100),
        (0, -100, 0),
        (-50, -25, -50),
        (7, 7, 7),
        (999, -999, 999),
        (123456, 654321, 123456),
        (-98765, 98765, -98765),
    ],
)
def test_should_return_first_element(
        a: int, b: int, expected: int
    ) -> None:
    """
    Test whether function returns first element
    of the pair
    """
    assert car(cons(a,b)) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 4, 4),
        (5, 10, 10),
        (-1, 0, 0),
        (100, 200, 200),
        (0, -100, -100),
        (-50, -25, -25),
        (7, 7, 7),
        (999, -999, -999),
        (123456, 654321, 654321),
        (-98765, 98765, 98765),
    ],
)
def test_should_return_last_element(
        a: int, b: int, expected: int
    ) -> None:
    """
    Test whether function returns last element
    of the pair
    """
    assert cdr(cons(a,b)) == expected
