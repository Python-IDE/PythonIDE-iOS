"""Type stubs for `clipboard` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

def get() -> str: ...

def set(text: str) -> None: ...

def clear() -> None: ...

get_text: Any

set_text: Any

__all__ = ['get', 'set', 'clear', 'get_text', 'set_text']
