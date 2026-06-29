# Call-Stack-Lab
This is a small side project I wanted to do to explore what call stacks are. 

I'm evolving a stack data structure along versions into a full simulation of how a call stack works. I'm not trying to write a Python interpreter and reimplement CPython (for now). The goal of this little side project is to make the mechanics behind a call stack easy to reason about.
In the future I want to learn C in order to actually execute code instead of simulate, be able to build stack frames for builtins (print, len, etc.), and play with memory management.

Starting with v1: A clean and simple stack abstraction. 

# V1

Features:
* push(value) - add item to the top of the stack
* pop() - remove item from the top of the stack and return
* peek() - return item from the top of the stack but not returning it
* is_empty() - check if stack is empty
* size() - return number of items inside the stack
* Type hints throughout the code as would be for custom data structures
* Test with pytest for good practice

# V2

Features:
* Built the StackFrame and CallStack classes
* StackFrame is implemented using a python dataclass in order to store the function name, args, local variables used, and a possible return value
* CallStack uses the Stack datastructure to call and return frames, in essence pushing and popping them
* Added peek method to CallStack to allow inspection of last frame without exposing internals
* Tested each class and corresponding methods

# V3

Features:
* Expanded the CallStack class with a get_frames method to display the frames in the stack
* Added a demo.py file meant to simulate what v5 will do without the manual input and instead automatically
* demo.py visualizes how frames are pushed and popped at each step
* Added iter method to stack for clean iteration without breaking encapsulation

# V4

Features:
* Added exception propogation via raise_exception method in call stack
* All frames get popped after raise_exception()
* Allows for stack trace rendering, copying how traceback looks
* Updated demo to show both normal exceution and exception propogation, two scenarios

# V5

Features:
* Automatic stack tracing using a decorator function wrapping the target function between call_stack call and return_ methods, including print statements
* Wrapped the decorator inside another function called tracer to create a decorator factory and have control over passing a call stack in
* Used inspect.signature to grab the function signature of the target function, as the call method requires such parameters
* Output shows the entire call stack after pushing and popping operations
