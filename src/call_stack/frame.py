from dataclasses import dataclass
from typing import Any

@dataclass
class StackFrame:
    function_name: str
    arguments: tuple[Any, ...]
    local_variables: dict[str, Any]
    return_value: Any = None
