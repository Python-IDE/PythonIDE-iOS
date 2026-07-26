"""Type stubs for `audio_session` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Dict, Iterable, Optional

class AudioSessionError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def set_category(category: str, mode: Optional[str] = ..., options: Optional[Iterable[str]] = ...) -> None: ...

def set_active(active: bool = ...) -> None: ...

def current_route() -> Dict[str, Any]: ...

__all__ = ['set_category', 'set_active', 'current_route', 'AudioSessionError']
