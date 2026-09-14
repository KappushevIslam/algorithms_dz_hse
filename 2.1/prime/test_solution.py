import pytest

from solution import count_primes


@pytest.mark.parametrize("n,expected", [
    (10, 4),
    (1, 0),
    (0, 0),
    (2, 0),
    (3, 1),
    (4, 2),
    (20, 8),
    (30, 10),
    (100, 25),
])
def test_count_primes(n, expected):
    assert count_primes(n) == expected


def test_count_primes_negative_returns_zero():
    assert count_primes(-5) == 0
