import pytest

from solution import TreeNode, is_valid_bst


def balanced() -> TreeNode:
    # собирает корректное дерево на значениях 5 3 7 2 4 6 8
    return TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7, TreeNode(6), TreeNode(8)))


@pytest.mark.parametrize("root,expected", [
    (TreeNode(2, TreeNode(1), TreeNode(3)), True),
    (TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6))), False),
    (TreeNode(1, TreeNode(1)), False),
    (TreeNode(5, TreeNode(7), TreeNode(3)), False),
    (TreeNode(1, None, TreeNode(2, None, TreeNode(3))), True),
])
def test_parametrized_shapes(root, expected):
    assert is_valid_bst(root) is expected


def test_empty_tree_is_valid():
    assert is_valid_bst(None) is True


def test_single_node_is_valid():
    assert is_valid_bst(TreeNode(10)) is True


def test_balanced_bst_is_valid():
    assert is_valid_bst(balanced()) is True


def test_swapped_children_are_invalid():
    root = TreeNode(5, TreeNode(7), TreeNode(3))
    assert is_valid_bst(root) is False


def test_deep_violation_is_invalid():
    root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(6)), TreeNode(7))
    assert is_valid_bst(root) is False


def test_duplicate_value_is_invalid():
    root = TreeNode(5, TreeNode(3), TreeNode(5))
    assert is_valid_bst(root) is False


def test_left_skewed_valid():
    root = TreeNode(5, TreeNode(4, TreeNode(3, TreeNode(2, TreeNode(1)))))
    assert is_valid_bst(root) is True


def test_right_skewed_valid():
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4))))
    assert is_valid_bst(root) is True
