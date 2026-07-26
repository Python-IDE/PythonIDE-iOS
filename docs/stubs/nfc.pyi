"""Type stubs for `nfc` public PythonIDE module."""

from __future__ import annotations

from typing import Any


def is_available() -> bool: ...

def scan(message: str = ..., timeout: float = ...) -> dict[str, Any] | None: ...

def write(records: list[dict[str, Any]], message: str = ...) -> bool: ...


__all__ = ["is_available", "scan", "write"]
