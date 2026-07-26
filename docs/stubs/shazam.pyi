from typing import Any

class ShazamError(RuntimeError):
    code: str | None
    domain: str | None
    def __init__(self, message: str, code: str | None = ..., domain: str | None = ...) -> None: ...

def is_available() -> bool: ...
def status() -> dict[str, Any]: ...
def recognize(duration: float = ...) -> dict[str, Any]: ...
def recognize_file(path: str) -> dict[str, Any]: ...
def cancel() -> None: ...

__all__ = [
    'is_available',
    'status',
    'recognize',
    'recognize_file',
    'cancel',
    'ShazamError',
]
