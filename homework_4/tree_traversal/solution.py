"""Задача. Реализовать BST со вставкой и шестью обходами дерева.

Идея. Шаг 1 вставляет значение сравнением с узлами от корня до листа.
Шаг 2 выполняет прямой и обратный обходы рекурсивным спуском. Шаг 3
собирает значения в список в порядке посещения узлов.

Структуры. Узел TreeNode хранит значение и ссылки left и right. Класс BST
хранит корень. Обратный обход меняет левого и правого потомка местами.
Дубликаты игнорируются для сохранения строгого свойства BST.
"""
# Сложность времени: O(n) на каждый обход, где n число узлов.
# Сложность памяти: O(n) под результат плюс O(h) под стек рекурсии, где h высота.
# Обоснование: каждый узел посещается один раз. Глубина рекурсии равна высоте
# дерева. Вставка стоит O(h) сравнений от корня до листа.
# Качество: сбалансированное дерево держит h около логарифма, скошенное дает h равное n.


class TreeNode:
    def __init__(self, val: int):
        # класс продублирован между папками для самодостаточности ссылок Stepik
        self.val = val
        self.left: "TreeNode | None" = None
        self.right: "TreeNode | None" = None


class BST:
    def __init__(self) -> None:
        # root хранит корень дерева, None означает пустое дерево
        self.root: "TreeNode | None" = None

    def insert(self, val: int) -> None:
        # вставка в пустое дерево создает корень
        if self.root is None:
            self.root = TreeNode(val)
            return
        # current спускается от корня до листа сравнением значений
        current = self.root
        while True:
            # дубликат игнорируется для строгого свойства BST
            if val == current.val:
                return
            # меньшее значение уходит в левое поддерево
            if val < current.val:
                if current.left is None:
                    current.left = TreeNode(val)
                    return
                current = current.left
            # большее значение уходит в правое поддерево
            else:
                if current.right is None:
                    current.right = TreeNode(val)
                    return
                current = current.right

    def preorder(self) -> list[int]:
        # порядок: узел, левое, правое
        result: list[int] = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node: "TreeNode | None", out: list[int]) -> None:
        # базовый случай: пустая ветвь дает пустой вклад
        if node is None:
            return
        out.append(node.val)
        self._preorder(node.left, out)
        self._preorder(node.right, out)

    def inorder(self) -> list[int]:
        # порядок: левое, узел, правое
        result: list[int] = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: "TreeNode | None", out: list[int]) -> None:
        # базовый случай: пустая ветвь дает пустой вклад
        if node is None:
            return
        self._inorder(node.left, out)
        out.append(node.val)
        self._inorder(node.right, out)

    def postorder(self) -> list[int]:
        # порядок: левое, правое, узел
        result: list[int] = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node: "TreeNode | None", out: list[int]) -> None:
        # базовый случай: пустая ветвь дает пустой вклад
        if node is None:
            return
        self._postorder(node.left, out)
        self._postorder(node.right, out)
        out.append(node.val)

    def reverse_preorder(self) -> list[int]:
        # порядок: узел, правое, левое
        result: list[int] = []
        self._reverse_preorder(self.root, result)
        return result

    def _reverse_preorder(self, node: "TreeNode | None", out: list[int]) -> None:
        # базовый случай: пустая ветвь дает пустой вклад
        if node is None:
            return
        out.append(node.val)
        self._reverse_preorder(node.right, out)
        self._reverse_preorder(node.left, out)

    def reverse_inorder(self) -> list[int]:
        # порядок: правое, узел, левое
        result: list[int] = []
        self._reverse_inorder(self.root, result)
        return result

    def _reverse_inorder(self, node: "TreeNode | None", out: list[int]) -> None:
        # базовый случай: пустая ветвь дает пустой вклад
        if node is None:
            return
        self._reverse_inorder(node.right, out)
        out.append(node.val)
        self._reverse_inorder(node.left, out)

    def reverse_postorder(self) -> list[int]:
        # порядок: правое, левое, узел
        result: list[int] = []
        self._reverse_postorder(self.root, result)
        return result

    def _reverse_postorder(self, node: "TreeNode | None", out: list[int]) -> None:
        # базовый случай: пустая ветвь дает пустой вклад
        if node is None:
            return
        self._reverse_postorder(node.right, out)
        self._reverse_postorder(node.left, out)
        out.append(node.val)


if __name__ == "__main__":
    demo = BST()
    for val in [5, 3, 7, 2, 4, 6, 8]:
        demo.insert(val)
    print(demo.preorder())
    print(demo.inorder())
    print(demo.postorder())
    print(demo.reverse_preorder())
    print(demo.reverse_inorder())
    print(demo.reverse_postorder())

# Визуализация. Пример вставки [5, 3, 7, 2, 4, 6, 8].
# Шаг 1. Вставка 5. Корень 5.
# Шаг 2. Вставка 3. Значение 3 меньше 5. Левый потомок 5.
# Шаг 3. Вставка 7. Значение 7 больше 5. Правый потомок 5.
# Шаг 4. Вставка 2. Спуск 5 3. Значение 2 меньше 3. Левый потомок 3.
# Шаг 5. Вставка 4. Спуск 5 3. Значение 4 больше 3. Правый потомок 3.
# Шаг 6. Вставка 6. Спуск 5 7. Значение 6 меньше 7. Левый потомок 7.
# Шаг 7. Вставка 8. Спуск 5 7. Значение 8 больше 7. Правый потомок 7.
# Итог. Дерево высотой 3. Preorder [5, 3, 2, 4, 7, 6, 8].
# Inorder [2, 3, 4, 5, 6, 7, 8]. Postorder [2, 4, 3, 6, 8, 7, 5].
