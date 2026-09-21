import pytest

from solution import LinkedQueue, LinkedStack


@pytest.mark.parametrize("values", [
    [],
    [5],
    [1, 2, 3, 4, 5],
])
def test_stack_returns_lifo_order(values):
    stack = LinkedStack()
    for val in values:
        stack.push(val)
    result = []
    while not stack.is_empty():
        result.append(stack.pop())
    assert result == values[::-1]


@pytest.mark.parametrize("values", [
    [],
    [5],
    [1, 2, 3, 4, 5],
])
def test_queue_returns_fifo_order(values):
    queue = LinkedQueue()
    for val in values:
        queue.enqueue(val)
    result = []
    while not queue.is_empty():
        result.append(queue.dequeue())
    assert result == values


def test_stack_pop_empty_raises():
    stack = LinkedStack()
    with pytest.raises(IndexError):
        stack.pop()


def test_stack_peek_empty_raises():
    stack = LinkedStack()
    with pytest.raises(IndexError):
        stack.peek()


def test_queue_dequeue_empty_raises():
    queue = LinkedQueue()
    with pytest.raises(IndexError):
        queue.dequeue()


def test_queue_peek_empty_raises():
    queue = LinkedQueue()
    with pytest.raises(IndexError):
        queue.peek()


def test_stack_peek_and_len():
    stack = LinkedStack()
    assert stack.is_empty()
    assert len(stack) == 0
    stack.push(10)
    stack.push(20)
    assert stack.peek() == 20
    assert len(stack) == 2
    assert stack.pop() == 20
    assert stack.peek() == 10
    assert len(stack) == 1


def test_queue_peek_and_len():
    queue = LinkedQueue()
    assert queue.is_empty()
    assert len(queue) == 0
    queue.enqueue(10)
    queue.enqueue(20)
    assert queue.peek() == 10
    assert len(queue) == 2
    assert queue.dequeue() == 10
    assert queue.peek() == 20
    assert len(queue) == 1


def test_stack_interleaved_operations():
    stack = LinkedStack()
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 1
    assert stack.is_empty()


def test_queue_interleaved_operations():
    queue = LinkedQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    queue.enqueue(3)
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.is_empty()


def test_large_sequence():
    stack = LinkedStack()
    queue = LinkedQueue()
    for val in range(1000):
        stack.push(val)
        queue.enqueue(val)
    for val in reversed(range(1000)):
        assert stack.pop() == val
    for val in range(1000):
        assert queue.dequeue() == val
