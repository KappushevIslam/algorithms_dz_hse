import pytest

from solution import is_palindrome


@pytest.mark.parametrize("value,expected", [
    (121, True),
    (31, False),
    (0, True),
    (7, True),
    (10, False),
    (11, True),
    (1221, True),
    (12321, True),
    (100, False),
    (123454321, True),
])
def test_is_palindrome(value, expected):
    assert is_palindrome(value) == expected


def test_is_palindrome_negative_returns_false():
    assert is_palindrome(-121) is False
