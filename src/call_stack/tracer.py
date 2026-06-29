from src.call_stack.call_stack import CallStack
import inspect



#tracer decorator
def tracer(call_stack):
    def decorator(func):
        def wrapper(*args, **kwargs):
            sig = inspect.signature(func)
            params = list(sig.parameters.keys())
            local_variables = dict(zip(params, args))

            call_stack.call(func.__name__, args, local_variables)
            print("----push----")
            for frame in call_stack.get_frames():
                print(frame)
            res = func(*args, **kwargs)
            call_stack.return_(res)
            print("----pop----")
            for frame in call_stack.get_frames():
                print(frame)
            return res
        return wrapper
    return decorator
