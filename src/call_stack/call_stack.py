from .stack import Stack
from .frame import StackFrame
from typing import Any

class CallStack:
    def __init__(self):
        self.stack = Stack()

    def call(self, function_name: str, arguments: tuple[Any, ...], local_variables: dict[str, Any]) -> None:
        stack_frame = StackFrame(function_name, arguments, local_variables)
        self.stack.push(stack_frame)

    def return_(self, return_value=None) -> Any:
        frame = self.stack.peek()
        frame.return_value = return_value
        self.stack.pop()
        return return_value

    def peek(self) -> StackFrame:
        return self.stack.peek()

    def get_frames(self) -> list[StackFrame]:
        frame_list = []
        for stack_frame in self.stack:
            frame_list.append(stack_frame)
        return frame_list

    def raise_exception(self, exception: Exception, message: str) -> str:
        frame_list = self.get_frames()
        lines = ["Traceback (most recent call last):"]
        for frame in frame_list:
            lines.append(f" in {frame.function_name}{frame.arguments}")
        while not self.stack.is_empty():
            self.stack.pop()

        lines.append(f"{exception.__name__}: {message}")
        return "\n".join(lines)