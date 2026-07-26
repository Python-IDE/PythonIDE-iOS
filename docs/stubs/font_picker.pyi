"""Type stubs for `font_picker` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Dict, Optional

class FontPickerError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def pick() -> Optional[Dict[str, Any]]: ...

__all__ = ['pick', 'FontPickerError']
