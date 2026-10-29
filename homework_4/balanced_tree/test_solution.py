import pytest

from solution import TreeNode, is_balanced


@pytest.mark.parametrize("root,expected", [
    (TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(7, TreeNode(6), TreeNode(8))), True),
    (TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4)))), False),
    (TreeNode(1, None, TreeNode(2, None, TreeNode(3))), False),
    (TreeNode(1), True),
    (None, True),
])
def test_parametrized_shapes(root, expected):
    assert is_balanced(root) is expected


def test_full_tree_is_balanced():
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6, TreeNode(5), TreeNode(7)))
    assert is_balanced(root) is True


def test_single_side_child_is_balanced():
    root = TreeNode(1, TreeNode(2))
    assert is_balanced(root) is True


def test_deep_subtree_breaks_balance():
    root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1))), TreeNode(7))
    assert is_balanced(root) is False


def test_missing_one_leaf_keeps_balance():
    root = TreeNode(5, TreeNode(3, TreeNode(2), None), TreeNode(7, TreeNode(6), TreeNode(8)))
    assert is_balanced(root) is True
