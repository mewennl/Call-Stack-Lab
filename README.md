# Call-Stack-Lab
This is a small side project I wanted to do to explore what call stacks are. 

I'm starting by building stack data structure and evolving it along versions into a full simulation of how a call stack works. I'm not trying to write a Python interpreter and reimplement CPython (for now). The goal of this little side project is to make the mechanics behind a call stack easy to reason about.

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
