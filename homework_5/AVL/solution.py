"""Задача. AVL дерево с вставкой, удалением и поиском с балансировкой.

Идея. Шаг 1 выполняет обычную вставку и удаление по правилам BST.
Шаг 2 обновляет высоту узла и считает разницу высот потомков. Шаг 3
применяет повороты влево и вправо при выходе разницы за пределы 1.

Структуры. Класс Node хранит ключ, ссылки и высоту поддерева. Класс AVL
хранит корень. Высота листа равна 1, пустая ветвь имеет высоту 0.
"""
# Сложность времени: O(log n) на вставку, удаление и поиск, высота держится логарифмической.
# Сложность памяти: O(n) под узлы плюс O(log n) под стек рекурсии.
# Обоснование: каждый спуск идет от корня к листу по высоте дерева. Поворот
# выполняет постоянное число операций. Балансировка держит высоту O(log n).
from __future__ import annotations


class Node:
    def __init__(self, key: int):
        self.key = key
        self.left: Node | None = None
        self.right: Node | None = None
        # высота листа равна 1 для прямого вычисления баланса
        self.height = 1


class AVL:
    def __init__(self) -> None:
        # root хранит корень дерева, None означает пустое дерево
        self.root: Node | None = None

    def insert(self, key: int) -> None:
        # вставка идет рекурсивным спуском с балансировкой на подъеме
        self.root = self._insert(self.root, key)

    def delete(self, key: int) -> None:
        # удаление ищет ключ, убирает узел и балансирует путь к корню
        self.root = self._delete(self.root, key)

    def search(self, key: int) -> bool:
        # поиск спускается сравнением без изменения структуры
        current = self.root
        while current is not None:
            # совпадение завершает поиск
            if key == current.key:
                return True
            # меньший ключ уходит влево, больший вправо
            current = current.left if key < current.key else current.right
        return False

    def inorder(self) -> list[int]:
        # порядок левое, узел, правое дает отсортированные ключи
        result: list[int] = []
        self._inorder(self.root, result)
        return result

    def _height(self, node: Node | None) -> int:
        # пустая ветвь имеет высоту ноль
        return node.height if node is not None else 0

    def _update(self, node: Node) -> None:
        # высота равна максимуму потомков плюс сам узел
        node.height = max(self._height(node.left), self._height(node.right)) + 1

    def _factor(self, node: Node) -> int:
        # положительный фактор означает перевес левого поддерева
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, node: Node) -> Node:
        # правый поворот поднимает левого потомка на место узла
        left = node.left
        assert left is not None
        # среднее поддерево переходит от левого потомка к узлу
        node.left = left.right
        left.right = node
        # высота обновляется снизу вверх: сначала узел, потом новый корень
        self._update(node)
        self._update(left)
        return left

    def _rotate_left(self, node: Node) -> Node:
        # левый поворот поднимает правого потомка на место узла
        right = node.right
        assert right is not None
        # среднее поддерево переходит от правого потомка к узлу
        node.right = right.left
        right.left = node
        # высота обновляется снизу вверх: сначала узел, потом новый корень
        self._update(node)
        self._update(right)
        return right

    def _rebalance(self, node: Node) -> Node:
        # высота пересчитывается до проверки фактора
        self._update(node)
        factor = self._factor(node)
        # левый перевес с левым наростом правится одним правым поворотом
        if factor > 1:
            assert node.left is not None
            # лево правое искривление сначала выравнивается левым поворотом
            if self._factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        # правый перевес с правым наростом правится одним левым поворотом
        if factor < -1:
            assert node.right is not None
            # право левое искривление сначала выравнивается правым поворотом
            if self._factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _insert(self, node: Node | None, key: int) -> Node:
        # пустое место создает лист
        if node is None:
            return Node(key)
        # дубликат игнорируется для строгого свойства поиска
        if key == node.key:
            return node
        # меньший ключ уходит влево, больший вправо
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        # подъем балансирует каждый узел на пути
        return self._rebalance(node)

    def _min_node(self, node: Node) -> Node:
        # минимум BST лежит в самом левом узле
        while node.left is not None:
            node = node.left
        return node

    def _delete(self, node: Node | None, key: int) -> Node | None:
        # отсутствующий ключ оставляет поддерево без изменений
        if node is None:
            return None
        # спуск ищет ключ сравнением
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        # лист и узел с одним потомком заменяются напрямую
        elif node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        # узел с двумя потомками берет преемника из правого поддерева
        else:
            successor = self._min_node(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)
        # подъем балансирует каждый узел на пути
        return self._rebalance(node)

    def _inorder(self, node: Node | None, out: list[int]) -> None:
        # пустая ветвь дает пустой вклад
        if node is None:
            return
        self._inorder(node.left, out)
        out.append(node.key)
        self._inorder(node.right, out)


if __name__ == "__main__":
    demo = AVL()
    for value in [10, 20, 30]:
        demo.insert(value)
    print(demo.inorder())
    print(demo.search(20))
    demo.delete(20)
    print(demo.inorder())

# Визуализация. Пример вставки [10, 20, 30] и удаления 20.
# Шаг 1. Вставка 10. Корень 10. Высота 1.
# Шаг 2. Вставка 20. Правый потомок 10. Факторы в норме.
# Шаг 3. Вставка 30. Правый потомок 20. Узел 10 имеет фактор минус 2.
# Шаг 4. Левый поворот вокруг 10. Корень 20. Потомки 10 и 30. Высота 2.
# Шаг 5. Поиск 20. Сравнение с корнем дает совпадение. Ответ True.
# Шаг 6. Удаление 20. Преемник 30 поднимается в корень. Потомок 10 слева.
# Шаг 7. Корень 30 имеет фактор 1. Повороты не нужны. Высота 2.
# Итог. Inorder после вставок [10, 20, 30]. Inorder после удаления [10, 30].
