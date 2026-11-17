"""Type stubs for `now_playing` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Mapping, Optional
from appui_resources import FileResource
from appui_operations import OperationHandle, ResourceBudget

class NowPlayingError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def status() -> dict[str, Any]: ...

def set_info(
    title: str,
    artist: str = ...,
    album: str = ...,
    duration: float = ...,
    elapsed: float = ...,
    artwork_path: Optional[str | FileResource] = ...,
    playback_rate: float = ...,
) -> None: ...

def update_elapsed(seconds: float, playback_rate: float = ...) -> None: ...

def clear() -> None: ...
def set_info_async(title: str, artist: str = ..., album: str = ..., duration: float = ..., elapsed: float = ..., artwork_path: Optional[str | FileResource] = ..., playback_rate: float = ..., *, budget: ResourceBudget | Mapping[str, Any] | None = ...) -> OperationHandle: ...

__all__ = ['status', 'set_info', 'update_elapsed', 'clear', 'set_info_async', 'NowPlayingError']
