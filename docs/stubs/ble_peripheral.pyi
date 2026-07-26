"""Type stubs for `ble_peripheral` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Dict, Optional

class BlePeripheralError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def start_advertising(name: str, service_uuid: str, characteristic_uuid: Optional[str] = ..., initial_value: Optional[str] = ...) -> Dict[str, Any]: ...

def stop_advertising() -> None: ...

def status() -> Dict[str, Any]: ...

def update_value(value: str) -> None: ...

__all__ = ['start_advertising', 'stop_advertising', 'status', 'update_value', 'BlePeripheralError']
