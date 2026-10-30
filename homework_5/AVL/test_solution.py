import pytest

from solution import AVL


def build(values: list[int]) -> AVL:
    # строит дерево последовательной вставкой значений
    tree = AVL()
    for value in values:
        tree.insert(value)
    return tree


def check_balanced(tree: AVL) -> bool:
    # проверяет разницу высот в каждом узле прямым обходом
    def height(node) -> int:
        if node is None:
            return 0
        left = height(node.left)
        right = height(node.right)
        assert abs(left - right) <= 1
        return max(left, right) + 1

    height(tree.root)
    return True


@pytest.mark.parametrize("key,expected", [
    (20, True),
    (10, True),
    (99, False),
    (0, False),
])
def test_search_after_inserts(key, expected):
    tree = build([10, 20, 30])
    assert tree.search(key) is expected


def test_empty_search_false():
    assert AVL().search(1) is False


def test_single_insert_search_delete():
    tree = build([7])
    assert tree.search(7) is True
    tree.delete(7)
    assert tree.search(7) is False
    assert tree.inorder() == []


def test_left_rotation_balances():
    tree = build([10, 20, 30])
    assert tree.root is not None and tree.root.key == 20
    assert tree.inorder() == [10, 20, 30]


def test_right_rotation_balances():
    tree = build([30, 20, 10])
    assert tree.root is not None and tree.root.key == 20
    assert tree.inorder() == [10, 20, 30]


def test_inorder_sorted():
    tree = build([8, 3, 10, 1, 6, 14, 4, 7, 13])
    assert tree.inorder() == [1, 3, 4, 6, 7, 8, 10, 13, 14]


def test_duplicate_ignored():
    tree = build([5, 3, 7, 3, 5])
    assert tree.inorder() == [3, 5, 7]


def test_delete_leaf_and_missing():
    tree = build([10, 20, 30])
    tree.delete(10)
    tree.delete(99)
    assert tree.inorder() == [20, 30]
    assert check_balanced(tree) is True


def test_delete_root_with_two_children():
    tree = build([10, 20, 30])
    tree.delete(20)
    assert tree.inorder() == [10, 30]
    assert tree.search(20) is False
    assert check_balanced(tree) is True
