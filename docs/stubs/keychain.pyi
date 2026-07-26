"""Type stubs for `keychain` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

def get_password(service: str, account: str = ...) -> str: ...

def set_password(service: str, account: str, password: str) -> bool: ...

def delete_password(service: str, account: str = ...) -> bool: ...

def get_services() -> list: ...

__all__ = ['get_password', 'set_password', 'delete_password', 'get_services']
