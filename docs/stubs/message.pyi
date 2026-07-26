"""Type stubs for `message` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Iterable, List, Optional

class MessageError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def can_send() -> bool: ...

def compose(
    recipients: str | Iterable[str],
    body: str = ...,
    attachments: Optional[List[str]] = ...,
) -> str: ...

__all__ = ['can_send', 'compose', 'MessageError']
