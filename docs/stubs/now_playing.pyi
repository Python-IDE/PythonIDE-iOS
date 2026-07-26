"""Type stubs for `now_playing` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Optional

class NowPlayingError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def set_info(
    title: str,
    artist: str = ...,
    album: str = ...,
    duration: float = ...,
    elapsed: float = ...,
    artwork_path: Optional[str] = ...,
    playback_rate: float = ...,
) -> None: ...

def update_elapsed(seconds: float, playback_rate: float = ...) -> None: ...

def clear() -> None: ...

__all__ = ['set_info', 'update_elapsed', 'clear', 'NowPlayingError']
