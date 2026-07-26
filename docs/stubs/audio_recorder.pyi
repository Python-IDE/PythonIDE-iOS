"""Type stubs for `audio_recorder` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Dict, Optional

class AudioRecorderError(RuntimeError):
    code: Optional[Any]
    domain: Optional[str]
    def __init__(self, message: str, code: Optional[Any] = ..., domain: Optional[str] = ...) -> None: ...

def start(
    path: Optional[str] = ...,
    format: str = ...,
    quality: str = ...,
    sample_rate: int = ...,
    channels: int = ...,
) -> Optional[str]: ...

def stop() -> Optional[Dict[str, Any]]: ...

def pause() -> None: ...

def resume() -> None: ...

def cancel() -> None: ...

def status() -> Dict[str, Any]: ...

def is_recording() -> bool: ...

def duration() -> float: ...

def metering() -> Dict[str, float]: ...

__all__ = [
    'start', 'stop', 'pause', 'resume', 'cancel',
    'status', 'is_recording', 'duration', 'metering',
    'AudioRecorderError',
]
