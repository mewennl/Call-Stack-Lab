import pytest
from src.call_stack.frame import StackFrame

class TestStackFrame:
    def test_init(self):
        frame = StackFrame(
            function_name="add", arguments=(1, 2), local_variables={"x":1, "y":2}, return_value=3
        )
        assert frame.function_name == "add"
        assert frame.arguments == (1, 2)
        assert frame.local_variables == {"x":1, "y":2}
        assert frame.return_value == 3

    def test_return_value_defaults_none(self):
        frame = StackFrame(
            function_name="add", arguments=(1, 2), local_variables={"x":1, "y":2}
        )
        assert frame.return_value is None

    def test_return_value_can_update(self):
        frame = StackFrame(
            function_name="add", arguments=(1, 2), local_variables={"x":1, "y":2}
        )
        frame.return_value = 3
        assert frame.return_value == 3


