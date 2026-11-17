"""Type stubs for `audio_recorder` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Dict, Mapping, Optional

from appui_operations import OperationHandle, ResourceBudget
from appui_resources import FileResource

FileOutput = str | FileResource

class AudioRecorderError(RuntimeError):
    code: Optional[Any]
    domain: Optional[str]
    def __init__(self, message: str, code: Optional[Any] = ..., domain: Optional[str] = ...) -> None: ...

def start(
    path: Optional[FileOutput] = ...,
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

def permission_status() -> Dict[str, Any]: ...

def start_async(
    path: Optional[FileOutput] = ...,
    format: str = ...,
    quality: str = ...,
    sample_rate: int = ...,
    channels: int = ...,
    *,
    budget: ResourceBudget | Mapping[str, Any] | None = ...,
) -> OperationHandle: ...

def stop_async(*, budget: ResourceBudget | Mapping[str, Any] | None = ...) -> OperationHandle: ...

def record(
    seconds: float,
    path: Optional[FileOutput] = ...,
    format: str = ...,
    quality: str = ...,
    sample_rate: int = ...,
    channels: int = ...,
    *,
    metering_interval: float = ...,
    budget: ResourceBudget | Mapping[str, Any] | None = ...,
) -> OperationHandle: ...

__all__ = [
    'start', 'stop', 'pause', 'resume', 'cancel',
    'status', 'is_recording', 'duration', 'metering',
    'permission_status', 'start_async', 'stop_async', 'record',
    'AudioRecorderError',
]
