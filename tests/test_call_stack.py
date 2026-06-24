import pytest
from src.call_stack.call_stack import CallStack

class TestCallStack:
    def test_call(self):
        call_stack = CallStack()
        call_stack.call(function_name="add", arguments=(1, 2), local_variables={"x": 1, "y": 2})
        last_frame = call_stack.peek()
        assert last_frame.function_name == "add"
        assert last_frame.arguments == (1, 2)
        assert last_frame.local_variables == {"x": 1, "y": 2}

    def test_return(self):
        call_stack = CallStack()
        call_stack.call(function_name="add", arguments=(1, 2), local_variables={"x": 1, "y": 2})
        frame = call_stack.peek()
        value = call_stack.return_(return_value=3)
        assert value == 3
        assert frame.return_value == 3
        with pytest.raises(IndexError):
            call_stack.peek()

    def test_return_empty_raises(self):
        call_stack = CallStack()
        with pytest.raises(IndexError):
            call_stack.return_(return_value=None)

