import pytest

from solution import max_even_sum


@pytest.mark.parametrize("data,expected", [
    ([5, 7, 13, 2, 14], 36),
    ([3], 0),
    ([], 0),
    ([2, 4, 6], 12),
    ([1, 3, 5], 8),
    ([2], 2),
    ([1, 2], 2),
    ([7, 7, 7], 14),
    ([100, 1], 100),
])
def test_max_even_sum(data, expected):
    assert max_even_sum(data) == expected


def test_max_even_sum_does_not_mutate_input():
    data = [5, 7, 13, 2, 14]
    max_even_sum(data)
    assert data == [5, 7, 13, 2, 14]
