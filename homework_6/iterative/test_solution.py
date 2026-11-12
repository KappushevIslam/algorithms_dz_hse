import pytest

from solution import merge_sort, quick_sort


@pytest.mark.parametrize("data", [
    [],
    [7],
    [2, 2, 1],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [-3, 0, -3, 5],
    [8, 3, 6, 1, 7, 2, 5, 4],
])
def test_both_sorts_match_sorted(data):
    assert merge_sort(data) == sorted(data)
    assert quick_sort(data) == sorted(data)


def test_both_sorts_keep_input_unchanged():
    for sort in (merge_sort, quick_sort):
        data = [3, 1, 2]
        sort(data)
        assert data == [3, 1, 2]


def test_both_sorts_handle_large_sorted():
    data = list(range(1000))
    assert merge_sort(data) == sorted(data)
    assert quick_sort(data) == sorted(data)


def test_both_sorts_match_sorted_on_shuffled():
    data = [7, 2, 11, 0, 5, 9, 1, 4, 10, 3, 8, 6]
    assert merge_sort(data) == sorted(data)
    assert quick_sort(data) == sorted(data)
