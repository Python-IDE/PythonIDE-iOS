"""Type stubs for `live_activity` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

def start(title: str = ..., message: str = ..., progress: Any | None = ..., icon: Any | None = ..., compact_text: Any | None = ...) -> Any: ...

def update(title: Any | None = ..., message: Any | None = ..., progress: Any | None = ..., icon: Any | None = ..., compact_text: Any | None = ...) -> Any: ...

def end(message: Any | None = ..., dismiss_delay: Any | None = ...) -> Any: ...

def is_supported() -> bool: ...

__all__ = ['start', 'update', 'end', 'is_supported']
