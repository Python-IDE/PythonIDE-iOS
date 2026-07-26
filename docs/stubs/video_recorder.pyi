"""Type stubs for `video_recorder` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Dict, Optional

class VideoRecorderError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def start(path: Optional[str] = ..., camera: str = ..., quality: str = ...) -> Optional[str]: ...

def stop() -> Optional[Dict[str, Any]]: ...

def cancel() -> None: ...

def status() -> Dict[str, Any]: ...

__all__ = ['start', 'stop', 'cancel', 'status', 'VideoRecorderError']
