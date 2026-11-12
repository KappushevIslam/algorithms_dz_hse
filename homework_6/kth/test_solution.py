import pytest

from solution import find_kth_largest


def test_statement_example_first():
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5


def test_statement_example_second():
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


@pytest.mark.parametrize("nums,k,expected", [
    ([4, 1, 9], 1, 9),
    ([4, 1, 9], 3, 1),
    ([7, 7, 7], 2, 7),
    ([-5, -1, -3], 2, -3),
    ([4, 4, 2], 3, 2),
    ([42], 1, 42),
])
def test_basic_cases(nums, k, expected):
    assert find_kth_largest(nums, k) == expected


def test_input_not_mutated():
    nums = [3, 2, 1, 5, 6, 4]
    find_kth_largest(nums, 2)
    assert nums == [3, 2, 1, 5, 6, 4]


@pytest.mark.parametrize("nums,k", [
    ([1, 2, 3], 0),
    ([1, 2, 3], 4),
    ([1, 2, 3], -1),
    ([], 1),
])
def test_invalid_k_raises(nums, k):
    with pytest.raises(ValueError):
        find_kth_largest(nums, k)


def test_all_k_match_sorted_oracle():
    nums = [5, 3, 5, 1, 4, 2, 4, 6]
    oracle = sorted(nums, reverse=True)
    for k in range(1, len(nums) + 1):
        assert find_kth_largest(nums, k) == oracle[k - 1]


def test_sorted_input():
    assert find_kth_largest([1, 2, 3, 4, 5], 2) == 4


def test_reversed_input():
    assert find_kth_largest([5, 4, 3, 2, 1], 2) == 4
