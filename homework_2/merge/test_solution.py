import pytest

from solution import from_list, merge_lists, to_list


@pytest.mark.parametrize("values1,values2,expected", [
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ([], [], []),
    ([], [0], [0]),
    ([0], [], [0]),
    ([1], [2], [1, 2]),
    ([2], [1], [1, 2]),
    ([1, 1, 1], [1, 1], [1, 1, 1, 1, 1]),
    ([1, 2], [3, 4, 5], [1, 2, 3, 4, 5]),
    ([5], [1, 2, 3, 4], [1, 2, 3, 4, 5]),
])
def test_merge_lists(values1, values2, expected):
    assert to_list(merge_lists(from_list(values1), from_list(values2))) == expected


def test_merge_lists_reuses_input_nodes():
    list1 = from_list([1, 3])
    list2 = from_list([2, 4])
    before: set[int] = set()
    node = list1
    while node is not None:
        before.add(id(node))
        node = node.next
    node = list2
    while node is not None:
        before.add(id(node))
        node = node.next
    merged = merge_lists(list1, list2)
    assert to_list(merged) == [1, 2, 3, 4]
    after: set[int] = set()
    node = merged
    while node is not None:
        after.add(id(node))
        node = node.next
    assert after == before
