"""Type stubs for `weather` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Dict, List, Optional

class WeatherError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def current(latitude: float, longitude: float) -> Dict[str, Any]: ...

def current_location() -> Dict[str, Any]: ...

def daily(latitude: float, longitude: float, days: int = ...) -> List[Dict[str, Any]]: ...

def hourly(latitude: float, longitude: float, hours: int = ...) -> List[Dict[str, Any]]: ...

__all__ = ['current', 'current_location', 'daily', 'hourly', 'WeatherError']
