import pytest

from solution import two_sum


@pytest.mark.parametrize("arr,k,expected", [
    ([1, 3, 4, 10], 7, (1, 2)),
    ([5, 5, 1, 4], 10, (0, 1)),
    ([2, 7], 9, (0, 1)),
    ([0, 4, 3, 0], 0, (0, 3)),
    ([-3, 4, 3, 90], 0, (0, 2)),
    ([1, 2, 3, 9], 12, (2, 3)),
    ([3, 2, 4], 6, (1, 2)),
])
def test_two_sum(arr, k, expected):
    assert two_sum(arr, k) == expected


def test_two_sum_does_not_mutate_input():
    arr = [1, 3, 4, 10]
    two_sum(arr, 7)
    assert arr == [1, 3, 4, 10]


def test_two_sum_indices_sum_to_k():
    arr = [10, -2, 8, 1, 5]
    k = 6
    i, j = two_sum(arr, k)
    assert i < j
    assert arr[i] + arr[j] == k
