"""Type stubs for `speech_recognition` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

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

def recognize_file(path: str, locale: str = ..., on_device: bool = ...) -> str: ...

__all__ = [
    'is_available', 'supported_locales',
    'start', 'status', 'text', 'is_listening', 'stop', 'cancel',
    'recognize_file',
    'SpeechRecognitionError',
]
