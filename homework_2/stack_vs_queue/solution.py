"""Задача. Реализовать стек и очередь на основе связных списков.

Идея. Узел хранит значение и ссылку на следующий узел. Стек хранит ссылку
только на вершину и добавляет и снимает узлы с одного конца. Очередь хранит
ссылки на голову и хвост и добавляет узлы с хвоста а снимает с головы.

Структуры. Односвязный список из узлов _Node. Дополнительных массивов нет.
Выбор объясняется операциями за O(1) без сдвига элементов.
"""
# Сложность времени: O(1) на каждую операцию push pop enqueue dequeue peek.
# Сложность памяти: O(n) под n хранящихся узлов.
# Обоснование: каждая операция меняет фиксированное число ссылок. Обход
# списка не выполняется ни в одной операции.


class _Node:
    def __init__(self, val: int, next: "_Node | None" = None):
        self.val = val
        self.next = next


class LinkedStack:
    def __init__(self) -> None:
        # top указывает на вершину стека
        self._top: "_Node | None" = None
        # size хранит число элементов
        self._size = 0

    def push(self, val: int) -> None:
        # новый узел становится вершиной
        self._top = _Node(val, self._top)
        self._size += 1

    def pop(self) -> int:
        # снятие с пустого стека считается ошибкой
        if self._top is None:
            raise IndexError("pop from empty stack")
        # вершина сдвигается на следующий узел
        val = self._top.val
        self._top = self._top.next
        self._size -= 1
        return val

    def peek(self) -> int:
        # чтение вершины без снятия
        if self._top is None:
            raise IndexError("peek from empty stack")
        return self._top.val

    def is_empty(self) -> bool:
        return self._top is None

    def __len__(self) -> int:
        return self._size


class LinkedQueue:
    def __init__(self) -> None:
        # head указывает на начало очереди
        self._head: "_Node | None" = None
        # tail указывает на конец очереди
        self._tail: "_Node | None" = None
        # size хранит число элементов
        self._size = 0

    def enqueue(self, val: int) -> None:
        # новый узел встает в хвост очереди
        node = _Node(val)
        if self._tail is None:
            self._head = node
            self._tail = node
        else:
            self._tail.next = node
            self._tail = node
        self._size += 1

    def dequeue(self) -> int:
        # снятие с пустой очереди считается ошибкой
        if self._head is None:
            raise IndexError("dequeue from empty queue")
        # голова сдвигается на следующий узел
        val = self._head.val
        self._head = self._head.next
        if self._head is None:
            self._tail = None
        self._size -= 1
        return val

    def peek(self) -> int:
        # чтение головы без снятия
        if self._head is None:
            raise IndexError("peek from empty queue")
        return self._head.val

    def is_empty(self) -> bool:
        return self._head is None

    def __len__(self) -> int:
        return self._size


if __name__ == "__main__":
    stack = LinkedStack()
    stack.push(1)
    stack.push(2)
    print(stack.pop())
    queue = LinkedQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.dequeue())

# Визуализация. Стек: push 1, push 2, push 3, pop.
# Шаг 1. Push 1. Вершина 1. Список: 1.
# Шаг 2. Push 2. Вершина 2. Список: 2 -> 1.
# Шаг 3. Push 3. Вершина 3. Список: 3 -> 2 -> 1.
# Шаг 4. Pop. Возврат 3. Вершина 2. Список: 2 -> 1.
# Итог. Порядок снятия обратный порядку добавления.
# Визуализация. Очередь: enqueue 1, enqueue 2, enqueue 3, dequeue.
# Шаг 1. Enqueue 1. Голова 1 хвост 1. Список: 1.
# Шаг 2. Enqueue 2. Голова 1 хвост 2. Список: 1 -> 2.
# Шаг 3. Enqueue 3. Голова 1 хвост 3. Список: 1 -> 2 -> 3.
# Шаг 4. Dequeue. Возврат 1. Голова 2 хвост 3. Список: 2 -> 3.
# Итог. Порядок снятия совпадает с порядком добавления.
