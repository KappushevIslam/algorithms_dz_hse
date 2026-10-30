"""Задача. Вернуть все перестановки массива чисел без повторов позиций.

Идея. Шаг 1 строит путь из выбранных элементов и остаток из невыбранных.
Шаг 2 при пустом остатке фиксирует копию пути в ответ. Шаг 3 перебирает
каждый элемент остатка, уходит в рекурсию и отменяет выбор возвратом.

Структуры. Список path хранит текущий префикс. Список remaining хранит
неиспользованные элементы. Список result копит готовые перестановки.
Декоратор tracer из первой задачи показывает стек вызовов backtrack.
"""
# Сложность времени: O(n * n!) во всех случаях, всего n! перестановок длиной n.
# Сложность памяти: O(n) под стек рекурсии плюс O(n * n!) под ответ.
# Обоснование: каждый уровень перебирает остаток, глубина рекурсии равна n.
# Копия пути при фиксации стоит O(n).
from __future__ import annotations

import functools
from typing import Any, Callable


def _format_args(args: tuple[Any, ...], kwargs: dict[str, Any]) -> str:
    # собирает позиционные и именованные аргументы в одну строку через repr
    parts = [repr(a) for a in args]
    parts.extend(f"{key}={value!r}" for key, value in kwargs.items())
    return ", ".join(parts)


def tracer(fn: Callable[..., Any]) -> Callable[..., Any]:
    # depth хранит текущую глубину вложенных вызовов
    depth = 0
    # log хранит копию каждой строки для тестов и ручного разбора
    log: list[str] = []

    @functools.wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        nonlocal depth
        # arg_str фиксируется один раз для симметрии строк входа и возврата
        arg_str = _format_args(args, kwargs)
        # pad отражает глубину: два пробела на уровень
        pad = "  " * depth
        entry = f"{pad}call {fn.__name__}({arg_str})"
        print(entry)
        log.append(entry)
        # глубина растет до рекурсивного спуска
        depth += 1
        try:
            result = fn(*args, **kwargs)
        except Exception as exc:
            # глубина уменьшается до печати, строка ошибки держит исходный отступ
            depth -= 1
            failure = f"{pad}raise {fn.__name__}({arg_str}) {exc!r}"
            print(failure)
            log.append(failure)
            raise
        # глубина уменьшается после возврата из вложенных вызовов
        depth -= 1
        done = f"{pad}return {fn.__name__}({arg_str}) = {result!r}"
        print(done)
        log.append(done)
        return result

    # trace_log дает доступ к журналу без перехвата stdout
    wrapper.trace_log = log  # type: ignore[attr-defined]
    return wrapper


def permute(nums: list[int]) -> list[list[int]]:
    # result копит готовые перестановки как копии пути
    result: list[list[int]] = []

    @tracer
    def backtrack(path: list[int], remaining: list[int]) -> None:
        # пустой остаток означает готовую перестановку
        if not remaining:
            result.append(list(path))
            return
        # каждый элемент остатка пробуется на текущей позиции
        for i in range(len(remaining)):
            # выбор фиксирует элемент в конец пути
            path.append(remaining[i])
            # рекурсия получает путь длиннее на один и остаток короче на один
            backtrack(path, remaining[:i] + remaining[i + 1:])
            # отмена выбора возвращает путь для следующего варианта
            path.pop()

    # старт идет с пустого пути и копии входа для защиты от мутации
    backtrack([], list(nums))
    return result


if __name__ == "__main__":
    print(permute([1, 2]))

# Визуализация. Пример permute([1, 2]).
# Шаг 1. Вход backtrack([], [1, 2]). Глубина 0. Остаток не пуст.
# Шаг 2. Выбор 1. Вход backtrack([1], [2]). Глубина 1. Отступ два пробела.
# Шаг 3. Выбор 2. Вход backtrack([1, 2], []). Глубина 2. Остаток пуст.
# Шаг 4. Фиксация [1, 2]. Возврат с отступом четыре пробела. Отмена выбора 2.
# Шаг 5. Отмена выбора 1. Выбор 2. Вход backtrack([2], [1]). Глубина 1.
# Шаг 6. Выбор 1. Вход backtrack([2, 1], []). Глубина 2. Фиксация [2, 1].
# Итог. Ответ [[1, 2], [2, 1]]. Журнал содержит 5 входов и 5 возвратов.
