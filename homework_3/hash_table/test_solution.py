import pytest

from solution import HashTable


def test_insert_and_get_int_keys():
    table = HashTable()
    table.insert(1, "one")
    table.insert(2, "two")
    assert table.get(1) == "one"
    assert table.get(2) == "two"


def test_insert_and_get_str_keys():
    table = HashTable()
    table.insert("eat", 1)
    table.insert("tea", 2)
    assert table.get("eat") == 1
    assert table.get("tea") == 2


def test_insert_updates_value_without_growth():
    table = HashTable()
    table.insert("k", 1)
    table.insert("k", 2)
    assert table.get("k") == 2
    assert len(table) == 1


def test_collisions_in_small_table():
    table = HashTable(capacity=2)
    table.insert(0, "a")
    table.insert(2, "b")
    table.insert(4, "c")
    assert table.get(0) == "a"
    assert table.get(2) == "b"
    assert table.get(4) == "c"
    assert len(table) == 3


def test_remove_existing_key():
    table = HashTable()
    table.insert("a", 1)
    table.insert("b", 2)
    table.remove("a")
    assert len(table) == 1
    with pytest.raises(KeyError):
        table.get("a")
    assert table.get("b") == 2


def test_remove_missing_key_raises():
    table = HashTable()
    with pytest.raises(KeyError):
        table.remove("missing")


def test_get_missing_key_raises():
    table = HashTable()
    table.insert("a", 1)
    with pytest.raises(KeyError):
        table.get("absent")


def test_resize_keeps_all_data():
    table = HashTable(capacity=4)
    for i in range(20):
        table.insert(i, i * 10)
    assert len(table) == 20
    for i in range(20):
        assert table.get(i) == i * 10


def test_storage_uses_only_lists():
    table = HashTable()
    table.insert("a", 1)
    table.insert(2, "b")
    assert type(table._buckets) is list
    for bucket in table._buckets:
        assert type(bucket) is list
        for entry in bucket:
            assert type(entry) is list
            assert len(entry) == 2


def test_len_and_contains():
    table = HashTable()
    assert len(table) == 0
    assert ("x" in table) is False
    table.insert("x", 5)
    assert len(table) == 1
    assert ("x" in table) is True
    table.remove("x")
    assert ("x" in table) is False
