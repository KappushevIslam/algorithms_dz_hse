"""Задача. Слить два отсортированных односвязных списка в один.

Идея. Шаг 1 ставит фиктивный узел перед результатом. Шаг 2 на каждом шаге
присоединяет меньший из текущих узлов. Шаг 3 дописывает остаток списка.

Структуры. Используется фиктивный головной узел. Указатель tail отмечает
конец результата. Выбор объясняется слиянием с переиспользованием узлов.
"""
# Сложность времени: O(n + m), где n и m длины списков.
# Сложность памяти: O(1) дополнительно, новые узлы не создаются.
# Обоснование: каждый узел посещается один раз. Память уходит только на
# фиктивный узел и указатели.


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def from_list(values: list[int]) -> "ListNode | None":
    # строит цепочку узлов в порядке значений
    head: "ListNode | None" = None
    tail: "ListNode | None" = None
    for value in values:
        node = ListNode(value)
        if head is None:
            head = node
            tail = node
        else:
            assert tail is not None
            tail.next = node
            tail = node
    return head


def to_list(head: "ListNode | None") -> list[int]:
    # читает значения цепочки по порядку
    values: list[int] = []
    node = head
    while node is not None:
        values.append(node.val)
        node = node.next
    return values


def merge_lists(
    list1: "ListNode | None", list2: "ListNode | None"
) -> "ListNode | None":
    # dummy упрощает присоединение первого узла
    dummy = ListNode()
    # tail всегда указывает на конец результата
    tail = dummy
    # инвариант: слитая часть отсортирована, tail ее конец
    while list1 is not None and list2 is not None:
        # присоединяется меньший текущий узел
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
    # один из списков пуст, остаток дописывается целиком
    if list1 is not None:
        tail.next = list1
    else:
        tail.next = list2
    return dummy.next


if __name__ == "__main__":
    print(to_list(merge_lists(from_list([1, 2, 4]), from_list([1, 3, 4]))))

# Визуализация. Пример list1 [1, 2, 4] list2 [1, 3, 4].
# Шаг 1. Текущие 1 и 1. Условие меньше либо равно истинно. Взят узел list1.
# Результат [1]. Текущие 2 и 1.
# Шаг 2. Текущие 2 и 1. Взят узел list2. Результат [1, 1]. Текущие 2 и 3.
# Шаг 3. Текущие 2 и 3. Взят узел list1. Результат [1, 1, 2]. Текущие 4 и 3.
# Шаг 4. Текущие 4 и 3. Взят узел list2. Результат [1, 1, 2, 3].
# Текущие 4 и 4.
# Шаг 5. Текущие 4 и 4. Условие меньше либо равно истинно. Взят узел list1.
# Результат [1, 1, 2, 3, 4]. Остаток list2 [4] дописан целиком.
# Итог. Ответ [1, 1, 2, 3, 4, 4]. Новые узлы не создавались.
