import pytest

from solution import validate


@pytest.mark.parametrize("pushed,popped,expected", [
    ([1, 2, 3, 4, 5], [1, 3, 5, 4, 2], True),
    ([1, 2, 3], [3, 1, 2], False),
    ([], [], True),
    ([1], [1], True),
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2, 3], [3, 2, 1], True),
    ([1, 2, 3, 4], [3, 1, 2, 4], False),
    ([3, 2, 1], [1, 2, 3], True),
    (list(range(10000)), list(range(10000)), True),
])
def test_validate(pushed, popped, expected):
    assert validate(pushed, popped) == expected


def test_validate_does_not_mutate_input():
    pushed = [1, 2, 3, 4, 5]
    popped = [1, 3, 5, 4, 2]
    validate(pushed, popped)
    assert pushed == [1, 2, 3, 4, 5]
    assert popped == [1, 3, 5, 4, 2]
