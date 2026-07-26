"""Type stubs for `translation` public PythonIDE module."""

from __future__ import annotations

from typing import Any, List, Optional

class TranslationError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def is_available() -> bool: ...

def supported_languages() -> List[str]: ...

def translate(text: str, target: str = ..., source: Optional[str] = ...) -> str: ...

__all__ = ['is_available', 'supported_languages', 'translate', 'TranslationError']
