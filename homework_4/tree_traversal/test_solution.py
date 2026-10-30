import pytest

from solution import BST


def build(values: list[int]) -> BST:
    # helper живет в тестах, решение хранит только TreeNode и BST
    tree = BST()
    for val in values:
        tree.insert(val)
    return tree


def collect_all(tree: BST) -> dict[str, list[int]]:
    # собирает все шесть обходов в словарь для компактных проверок
    return {
        "preorder": tree.preorder(),
        "inorder": tree.inorder(),
        "postorder": tree.postorder(),
        "reverse_preorder": tree.reverse_preorder(),
        "reverse_inorder": tree.reverse_inorder(),
        "reverse_postorder": tree.reverse_postorder(),
    }


@pytest.mark.parametrize("method,expected", [
    ("preorder", [5, 3, 2, 4, 7, 6, 8]),
    ("inorder", [2, 3, 4, 5, 6, 7, 8]),
    ("postorder", [2, 4, 3, 6, 8, 7, 5]),
    ("reverse_preorder", [5, 7, 8, 6, 3, 4, 2]),
    ("reverse_inorder", [8, 7, 6, 5, 4, 3, 2]),
    ("reverse_postorder", [8, 6, 7, 4, 2, 3, 5]),
])
def test_balanced_tree_traversals(method, expected):
    tree = build([5, 3, 7, 2, 4, 6, 8])
    assert getattr(tree, method)() == expected


def test_empty_tree_returns_empty_lists():
    tree = BST()
    result = collect_all(tree)
    assert result == {
        "preorder": [],
        "inorder": [],
        "postorder": [],
        "reverse_preorder": [],
        "reverse_inorder": [],
        "reverse_postorder": [],
    }


def test_single_node_tree():
    tree = build([10])
    result = collect_all(tree)
    assert result == {
        "preorder": [10],
        "inorder": [10],
        "postorder": [10],
        "reverse_preorder": [10],
        "reverse_inorder": [10],
        "reverse_postorder": [10],
    }


def test_left_skewed_tree():
    tree = build([5, 4, 3, 2, 1])
    assert tree.preorder() == [5, 4, 3, 2, 1]
    assert tree.inorder() == [1, 2, 3, 4, 5]
    assert tree.postorder() == [1, 2, 3, 4, 5]
    assert tree.reverse_inorder() == [5, 4, 3, 2, 1]


def test_right_skewed_tree():
    tree = build([1, 2, 3, 4, 5])
    assert tree.preorder() == [1, 2, 3, 4, 5]
    assert tree.inorder() == [1, 2, 3, 4, 5]
    assert tree.postorder() == [5, 4, 3, 2, 1]
    assert tree.reverse_inorder() == [5, 4, 3, 2, 1]


def test_duplicate_values_ignored():
    tree = build([5, 3, 7, 3, 5, 7])
    assert tree.inorder() == [3, 5, 7]
    assert tree.preorder() == [5, 3, 7]


def test_inorder_returns_sorted_order():
    tree = build([8, 3, 10, 1, 6, 14, 4, 7, 13])
    assert tree.inorder() == [1, 3, 4, 6, 7, 8, 10, 13, 14]


def test_reverse_inorder_returns_descending_order():
    tree = build([8, 3, 10, 1, 6, 14, 4, 7, 13])
    assert tree.reverse_inorder() == [14, 13, 10, 8, 7, 6, 4, 3, 1]


def test_insert_preserves_bst_property():
    tree = build([5, 3, 7, 2, 4, 6, 8])
    tree.insert(0)
    tree.insert(9)
    assert tree.inorder() == [0, 2, 3, 4, 5, 6, 7, 8, 9]
    assert tree.preorder()[0] == 5
