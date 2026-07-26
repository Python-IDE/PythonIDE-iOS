"""Type stubs for `qrcode` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Optional

class QRCodeError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def generate_base64(text: str, size: int = ..., correction: str = ...) -> str: ...

def generate(text: str, size: int = ..., correction: str = ...) -> bytes: ...

def save(text: str, path: str, size: int = ..., correction: str = ...) -> str: ...

__all__ = ['generate', 'generate_base64', 'save', 'QRCodeError']
