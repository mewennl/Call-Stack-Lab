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

    def test_get_frames_on_empty(self):
        call_stack = CallStack()
        frames = call_stack.get_frames()
        assert frames == []

    def test_get_frames_number_of_returns(self):
        call_stack = CallStack()
        call_stack.call(function_name="add", arguments=(1, 2), local_variables={"x": 1, "y": 2})
        num_frames = len(call_stack.get_frames())
        assert num_frames == 1

    def test_get_frames_order(self):
        call_stack = CallStack()
        call_stack.call(function_name="first", arguments=(1,), local_variables={"a":1})
        call_stack.call(function_name="second", arguments=(2,), local_variables={"b":2})
        call_stack.call(function_name="third", arguments=(3,), local_variables={"c":3})
        frames = call_stack.get_frames()
        assert frames[0].function_name == "first"
        assert frames[1].function_name == "second"
        assert frames[2].function_name == "third"

    def test_get_frames_after_return(self):
        call_stack = CallStack()
        call_stack.call(function_name="first", arguments=(1,), local_variables={"a":1})
        assert call_stack.get_frames() != []
        call_stack.return_(return_value=3)
        assert call_stack.get_frames() == []

    def test_raise_exception_on_empty(self):
        call_stack = CallStack()
        assert call_stack.raise_exception(exception=ZeroDivisionError, message="division by zero") == "Traceback (most recent call last):\nZeroDivisionError: division by zero"

    def test_stack_is_empty_after_raise_exception(self):
        call_stack = CallStack()
        call_stack.call(function_name="first", arguments=(1,), local_variables={"a":1})
        call_stack.raise_exception(exception=ZeroDivisionError, message="division by zero")
        assert call_stack.get_frames() == []

    def test_raise_exception_output(self):
        call_stack = CallStack()
        call_stack.call(function_name="first", arguments=(1,), local_variables={"a":1})
        call_stack.call(function_name="second", arguments=(2,), local_variables={"b":2})
        result = call_stack.raise_exception(exception=ZeroDivisionError, message="division by zero")
        assert "first" in result
        assert "ZeroDivisionError" in result
        assert "division by zero" in result

