"""Type stubs for `mail` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Iterable, List, Optional

class MailError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def can_send() -> bool: ...

def compose(
    to: str | Iterable[str],
    subject: str = ...,
    body: str = ...,
    cc: str | Iterable[str] | None = ...,
    bcc: str | Iterable[str] | None = ...,
    attachments: Optional[List[dict[str, Any]]] = ...,
) -> str: ...

__all__ = ['can_send', 'compose', 'MailError']
