"""Type stubs for `alarm` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

class AlarmError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def is_available() -> bool: ...

def request_authorization() -> bool: ...

def schedule(title: str, hour: int, minute: int, repeats: bool = ...) -> str: ...

def cancel(alarm_id: str) -> None: ...

def list_alarms() -> List[Dict[str, Any]]: ...

__all__ = ['is_available', 'request_authorization', 'schedule', 'cancel', 'list_alarms', 'AlarmError']
