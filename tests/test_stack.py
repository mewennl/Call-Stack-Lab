import pytest
from collections import deque
from src.call_stack.stack import Stack

class TestStack:
    def test_init(self):
        stack = Stack()
        assert stack.size() == 0
        assert stack.stack == deque([])

    def test_add(self):
        stack = Stack()
        stack.push(1)
        assert stack.size() == 1
        stack.push(2)
        assert stack.size() == 2

    def test_remove(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.size() == 0

    def test_top(self):
        stack = Stack()
        stack.push(1)
        assert stack.peek() == 1
        assert stack.size() == 1

    def test_is_empty(self):
        stack = Stack()
        stack.push(1)
        assert stack.is_empty() == False
        stack.pop()
        assert stack.is_empty() == True




