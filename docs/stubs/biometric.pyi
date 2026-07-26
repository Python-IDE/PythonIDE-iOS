"""Type stubs for `biometric` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

def biometric_type() -> Any: ...

def is_available() -> bool: ...

def authenticate(reason: str = ...) -> Any: ...

def authenticate_with_passcode(reason: str = ...) -> Any: ...

__all__ = ['biometric_type', 'is_available', 'authenticate', 'authenticate_with_passcode']
