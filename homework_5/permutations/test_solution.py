import pytest

from solution import permute


@pytest.mark.parametrize("nums,expected", [
    ([1], [[1]]),
    ([0, 1], [[0, 1], [1, 0]]),
    ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
])
def test_permute_examples(nums, expected):
    assert sorted(permute(nums)) == sorted(expected)


def test_empty_returns_single_empty():
    assert permute([]) == [[]]


def test_input_not_mutated():
    nums = [1, 2, 3]
    permute(nums)
    assert nums == [1, 2, 3]


def test_count_is_factorial():
    assert len(permute([1, 2, 3, 4])) == 24


def test_all_unique():
    result = permute([1, 2, 3])
    assert len({tuple(p) for p in result}) == 6


def test_tracer_shows_stack(capsys):
    permute([1, 2])
    out = capsys.readouterr().out
    # вход верхнего уровня идет без отступа
    assert "call backtrack([], [1, 2])" in out
    # вложенный вход сдвинут на два пробела
    assert "  call backtrack([1], [2])" in out
    # каждый вход закрыт строкой возврата
    assert out.count("call backtrack") == out.count("return backtrack")
