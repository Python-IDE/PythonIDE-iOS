"""Type stubs for `assistant` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional

class AssistantError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def is_available() -> bool: ...

def list_tools() -> List[Dict[str, Any]]: ...

def run(prompt: str, tools: Optional[Iterable[str]] = ...) -> Dict[str, Any]: ...

__all__ = ['is_available', 'list_tools', 'run', 'AssistantError']
