"""Type stubs for `nfc` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Mapping
from appui_operations import OperationHandle, ResourceBudget


def is_available() -> bool: ...

def status() -> str: ...

def scan(message: str = ..., timeout: float = ...) -> dict[str, Any] | None: ...

def scan_async(message: str = ..., timeout: float = ..., *, budget: ResourceBudget | Mapping[str, Any] | None = ...) -> OperationHandle: ...

def write(records: list[dict[str, Any]], message: str = ...) -> bool: ...

def write_async(records: list[dict[str, Any]], message: str = ..., *, budget: ResourceBudget | Mapping[str, Any] | None = ...) -> OperationHandle: ...

def cancel() -> bool: ...


__all__ = ["is_available", "status", "scan", "scan_async", "write", "write_async", "cancel"]
