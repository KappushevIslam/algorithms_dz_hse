import time

import pytest

from solution import merge_sort, quick_sort, timing


@pytest.mark.parametrize("data", [
    [],
    [7],
    [2, 2, 1],
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [-3, 0, -3, 5],
    [5, 2, 8, 1, 7, 3, 6, 4],
])
def test_sorts_match_sorted(data: list[int]) -> None:
    assert merge_sort(data) == sorted(data)
    assert quick_sort(data) == sorted(data)
    assert merge_sort(data) == quick_sort(data)


def test_sorts_do_not_mutate() -> None:
    # проверка выполняет обе сортировки на равных копиях
    first = [5, 2, 8, 1, 7, 3, 6, 4]
    second = list(first)
    merge_sort(first)
    quick_sort(second)
    assert first == [5, 2, 8, 1, 7, 3, 6, 4]
    assert second == [5, 2, 8, 1, 7, 3, 6, 4]


def test_timing_keeps_value_and_prints(capsys: pytest.CaptureFixture[str]) -> None:
    wrapped = timing(merge_sort)
    result = wrapped([3, 1, 2])
    out = capsys.readouterr().out
    assert result == [1, 2, 3]
    # строка замера имеет вид имя: число s
    line = out.strip()
    assert line.startswith("merge_sort: ")
    assert line.endswith(" s")


@pytest.mark.parametrize("data", [
    list(range(1000)),
    list(range(1000, 0, -1)),
])
def test_quick_slower_than_merge(data: list[int]) -> None:
    # реальное отношение на отсортированном входе на порядок выше порога
    start = time.perf_counter()
    merge_sort(data)
    merge_elapsed = time.perf_counter() - start
    start = time.perf_counter()
    quick_sort(data)
    quick_elapsed = time.perf_counter() - start
    assert quick_elapsed > merge_elapsed * 2
