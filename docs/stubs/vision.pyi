"""Type stubs for `vision` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

def setup_vision_framework() -> dict[str, Any] | None: ...

def is_vision_available() -> bool: ...

def recognize_text_from_image_data(image_data: bytes) -> str | None: ...

__all__ = ['setup_vision_framework', 'is_vision_available', 'recognize_text_from_image_data']
