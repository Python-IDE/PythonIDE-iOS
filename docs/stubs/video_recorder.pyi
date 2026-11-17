"""Type stubs for `video_recorder` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Dict, Mapping, Optional

from appui_operations import OperationHandle, ResourceBudget
from appui_resources import FileResource

FileOutput = str | FileResource

class VideoRecorderError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def start(path: Optional[FileOutput] = ..., camera: str = ..., quality: str = ...) -> Optional[str]: ...

def stop() -> Optional[Dict[str, Any]]: ...

def cancel() -> None: ...

def status() -> Dict[str, Any]: ...

def permission_status() -> Dict[str, Any]: ...

def start_async(
    path: Optional[FileOutput] = ...,
    camera: str = ...,
    quality: str = ...,
    *,
    budget: ResourceBudget | Mapping[str, Any] | None = ...,
) -> OperationHandle: ...

def stop_async(*, budget: ResourceBudget | Mapping[str, Any] | None = ...) -> OperationHandle: ...

def record(
    seconds: float,
    path: Optional[FileOutput] = ...,
    camera: str = ...,
    quality: str = ...,
    *,
    progress_interval: float = ...,
    budget: ResourceBudget | Mapping[str, Any] | None = ...,
) -> OperationHandle: ...

__all__ = [
    'start', 'stop', 'cancel', 'status', 'permission_status',
    'start_async', 'stop_async', 'record', 'VideoRecorderError',
]
