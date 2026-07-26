"""Type stubs for `permission` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

def status(module: str) -> dict[str, Any]: ...

def request(module: str) -> dict[str, Any]: ...

def status_all() -> dict[str, Any]: ...

MODULES: list[str]

__all__ = ['status', 'request', 'status_all', 'MODULES']
