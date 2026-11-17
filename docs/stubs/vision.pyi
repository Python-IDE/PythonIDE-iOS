"""Type stubs for `vision` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union
from appui_operations import OperationHandle, ResourceBudget
from appui_resources import FileResource

def setup_vision_framework() -> dict[str, Any] | None: ...

def is_vision_available() -> bool: ...

def recognize_text_from_image_data(image_data: bytes) -> str | None: ...

def recognize_text(image_data: bytes) -> str | None: ...
def recognize_text_async(image_data: bytes, *, budget: ResourceBudget | Mapping[str, Any] | None = ...) -> OperationHandle: ...
def recognize_text_file(path: str | FileResource, *, max_bytes: int = ...) -> str | None: ...
def recognize_text_file_async(path: str | FileResource, *, budget: ResourceBudget | Mapping[str, Any] | None = ...) -> OperationHandle: ...

__all__ = [
    'setup_vision_framework', 'is_vision_available',
    'recognize_text_from_image_data', 'recognize_text',
    'recognize_text_async', 'recognize_text_file',
    'recognize_text_file_async',
]
