"""Type stubs for `http_server` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Dict, Optional

class HttpServerError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def start(port: int = ..., root_dir: Optional[str] = ...) -> str: ...

def stop() -> None: ...

def status() -> Dict[str, Any]: ...

__all__ = ['start', 'stop', 'status', 'HttpServerError']
