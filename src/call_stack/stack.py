from collections import deque

#using generics to preserve functionality for different data types

class Stack[T]:
    def __init__(self) -> None:
        #initializing the stack as an empty deque
        self.stack = deque()
    def push(self, value: T) -> None:
        self.stack.append(value)
    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("Stack is empty, cannot pop.")
        return self.stack.pop()
    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Stack is empty, cannot peek.")
        return self.stack[-1]
    def is_empty(self) -> bool:
        return not self.stack
    def size(self) -> int:
        return len(self.stack)

#all of these operations run in O(1) time


