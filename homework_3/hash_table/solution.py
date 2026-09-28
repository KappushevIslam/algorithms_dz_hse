"""Задача. Реализовать хеш-таблицу с вставкой, поиском и удалением.

Идея. Шаг 1 вычисляет индекс корзины хешем ключа по модулю емкости.
Шаг 2 хранит пары в цепочке внутри корзины. Шаг 3 удваивает емкость
и перестраивает таблицу при превышении порога заполнения.

Структуры. Хранение построено только на list. Список корзин содержит
списки цепочек. Каждая запись является списком из ключа и значения.
Выбор объясняется требованием использовать только list для хранения.
"""
# Сложность времени: O(1) в среднем на вставку, поиск и удаление.
# Сложность памяти: O(n) под n хранящихся пар.
# Обоснование: цепочки остаются короткими при своевременном расширении.
# Худший случай O(n) возможен при вырожденном хеше всех ключей в одну корзину.


class HashTable:
    def __init__(self, capacity: int = 8) -> None:
        # минимальная емкость защищает от вырожденных значений
        if capacity < 1:
            capacity = 1
        # buckets хранит цепочки пар, каждая корзина является списком
        self._buckets: list[list[list]] = [[] for _ in range(capacity)]
        # size хранит число пар
        self._size = 0

    def _hash(self, key: object) -> int:
        # целые ключи используются напрямую
        if isinstance(key, int) and not isinstance(key, bool):
            return key
        # строки хешируются полиномом с основанием 31
        if isinstance(key, str):
            code = 0
            for char in key:
                code = (code * 31 + ord(char)) & 0xFFFFFFFF
            return code
        # прочие типы используют встроенный хеш
        return hash(key)

    def _index(self, key: object) -> int:
        # остаток от деления привязывает хеш к диапазону корзин
        return self._hash(key) % len(self._buckets)

    def _find(self, key: object) -> list | None:
        # поиск записи в цепочке корзины по равенству ключей
        for entry in self._buckets[self._index(key)]:
            if entry[0] == key and type(entry[0]) is type(key):
                return entry
        return None

    def _resize(self) -> None:
        # old хранит все записи до расширения
        old: list[list] = []
        for bucket in self._buckets:
            for entry in bucket:
                old.append(entry)
        # емкость удваивается, цепочки создаются заново пустыми
        self._buckets = [[] for _ in range(len(self._buckets) * 2)]
        self._size = 0
        for entry in old:
            self._buckets[self._index(entry[0])].append(entry)
            self._size += 1

    def insert(self, key: object, value: object) -> None:
        # повторный ключ обновляет значение без роста размера
        found = self._find(key)
        if found is not None:
            found[1] = value
            return
        self._buckets[self._index(key)].append([key, value])
        self._size += 1
        # порог заполнения 0.75 запускает расширение
        if self._size > len(self._buckets) * 3 // 4:
            self._resize()

    def get(self, key: object) -> object:
        # отсутствие ключа считается ошибкой
        found = self._find(key)
        if found is None:
            raise KeyError(key)
        return found[1]

    def remove(self, key: object) -> None:
        # удаление ищет запись в цепочке корзины
        bucket = self._buckets[self._index(key)]
        for i, entry in enumerate(bucket):
            if entry[0] == key and type(entry[0]) is type(key):
                del bucket[i]
                self._size -= 1
                return
        raise KeyError(key)

    def keys(self) -> list:
        # собирает ключи проходом по всем корзинам
        result: list = []
        for bucket in self._buckets:
            for entry in bucket:
                result.append(entry[0])
        return result

    def __len__(self) -> int:
        return self._size

    def __contains__(self, key: object) -> bool:
        return self._find(key) is not None


if __name__ == "__main__":
    table = HashTable(capacity=4)
    table.insert("eat", 1)
    table.insert("tea", 2)
    table.insert(10, 3)
    print(table.get("tea"))
    print(sorted([str(k) for k in table.keys()]))
    table.remove("eat")
    print(len(table))

# Визуализация. Емкость 4. Вставка eat, tea, ключа 10.
# Шаг 1. Хеш eat по модулю 4 дает корзину 0. Корзина 0 пуста.
# Состояние: [[eat, 1]] [] [] [].
# Шаг 2. Хеш tea по модулю 4 дает корзину 0. Коллизия с eat.
# Цепочка корзины 0 удлинилась.
# Состояние: [[eat, 1], [tea, 2]] [] [] [].
# Шаг 3. Хеш 10 по модулю 4 дает корзину 2. Коллизий нет.
# Состояние: [[eat, 1], [tea, 2]] [] [[10, 3]] [].
# Шаг 4. Размер 3 равен порогу 3. Расширения нет. Поиск tea идет
# в корзину 0 и перебирает цепочку из 2 записей.
# Итог. Get tea вернул 2. Remove eat оставил цепочку из 1 записи.
