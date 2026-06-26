from src.call_stack.call_stack import CallStack

def print_stack(cs):
    print("____Stack State____")
    for frame in cs.get_frames():
        print(frame)
    print()

callStack = CallStack()
callStack.call("factorial", (3,), {"n":3})
print_stack(callStack)
callStack.call("factorial", (2,), {"n":2})
print_stack(callStack)
callStack.call("factorial", (1,), {"n":1})
print_stack(callStack)
callStack.return_(1)
print_stack(callStack)
callStack.return_(2)
print_stack(callStack)
callStack.return_(3)
print_stack(callStack)


callStack = CallStack()
callStack.call("factorial", (3,), {"n":3})
callStack.call("factorial", (2,), {"n":2})
callStack.call("factorial", (0,), {"n":0})
print(callStack.raise_exception(exception=ValueError, message="cannot divide by zero"))
print_stack(callStack)