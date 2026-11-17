"""Type stubs for `speech_recognition` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Dict, List, Mapping, Optional

from appui_operations import OperationHandle, ResourceBudget
from appui_resources import FileResource

class SpeechRecognitionError(RuntimeError):
    code: Optional[Any]
    domain: Optional[str]
    def __init__(self, message: str, code: Optional[Any] = ..., domain: Optional[str] = ...) -> None: ...

def is_available() -> bool: ...

def supported_locales() -> List[str]: ...

def start(locale: str = ..., on_device: bool = ..., partial: bool = ...) -> bool: ...

def status() -> Dict[str, Any]: ...

def text() -> str: ...

def is_listening() -> bool: ...

def stop() -> str: ...

def cancel() -> None: ...

def recognize_file(path: str | FileResource, locale: str = ..., on_device: bool = ...) -> str: ...

def permission_status() -> Dict[str, Any]: ...

def listen(
    seconds: float,
    locale: str = ...,
    on_device: bool = ...,
    partial: bool = ...,
    *,
    poll_interval: float = ...,
    budget: ResourceBudget | Mapping[str, Any] | None = ...,
) -> OperationHandle: ...

def recognize_file_async(
    path: str | FileResource,
    locale: str = ...,
    on_device: bool = ...,
    *,
    budget: ResourceBudget | Mapping[str, Any] | None = ...,
) -> OperationHandle: ...

__all__ = [
    'is_available', 'supported_locales',
    'start', 'status', 'text', 'is_listening', 'stop', 'cancel',
    'recognize_file', 'permission_status', 'listen', 'recognize_file_async',
    'SpeechRecognitionError',
]
