"""Задача. Декоратор показывает стек вызовов рекурсивной функции.

Идея. Шаг 1 печатает строку входа с отступом по текущей глубине. Шаг 2
увеличивает глубину и вызывает исходную функцию. Шаг 3 уменьшает глубину
и печатает строку возврата с результатом и тем же отступом.

Структуры. Замыкание хранит счетчик глубины и список строк trace_log.
Счетчик задает отступ из двух пробелов на уровень. Список сохраняет
копию каждой напечатанной строки для проверок.
"""
# Сложность времени: O(d) на один вызов для форматирования аргументов, где d число аргументов.
# Сложность памяти: O(d) под счетчик глубины и O(t) под накопленный журнал из t строк.
# Обоснование: обертка выполняет постоянное число операций плюс печать одной строки
# на вход и одной на выход. Глубина рекурсии равна глубине стека исходной функции.
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


if __name__ == "__main__":
    @tracer
    def fact(n: int) -> int:
        if n <= 1:
            return 1
        return n * fact(n - 1)

    print(fact(3))

# Визуализация. Пример fact(3).
# Шаг 1. Вход fact(3). Глубина 0. Отступ пустой.
# Шаг 2. Вход fact(2). Глубина 1. Отступ два пробела.
# Шаг 3. Вход fact(1). Глубина 2. Отступ четыре пробела.
# Шаг 4. База n 1. Возврат 1. Строка возврата с отступом четыре пробела.
# Шаг 5. Возврат fact(2) 2. Строка возврата с отступом два пробела.
# Шаг 6. Возврат fact(3) 6. Строка возврата без отступа.
# Итог. Ответ 6. Журнал содержит 6 строк: 3 входа и 3 возврата.
