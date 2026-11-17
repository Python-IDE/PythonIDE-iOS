"""Type stubs for `music_player` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, Literal, Mapping, Optional, Sequence, TypedDict
from appui_resources import FileResource, MediaSource
from appui_operations import OperationHandle, ResourceBudget

MediaInput = str | FileResource | MediaSource

PlayMode = Literal["sequence", "repeat_all", "repeat_one", "shuffle"]

PLAY_MODE_SEQUENCE: PlayMode
PLAY_MODE_REPEAT_ALL: PlayMode
PLAY_MODE_REPEAT_ONE: PlayMode
PLAY_MODE_SHUFFLE: PlayMode

class Song(TypedDict, total=False):
    url: MediaInput
    title: str
    name: str
    artist: str
    singer: str
    album: str
    artwork_path: MediaInput
    artwork_url: MediaInput
    cover: MediaInput
    artwork_cache_key: str
    artwork_cache_version: str
    duration: float
    id: str

class MusicPlayerError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def status() -> Dict[str, Any]: ...
def release() -> Dict[str, Any]: ...

def configure(
    now_playing: Optional[bool] = ...,
    remote_commands: Optional[bool] = ...,
    background: Optional[bool] = ...,
    persist: Optional[bool] = ...,
    auto_advance: Optional[bool] = ...,
    progress_interval: Optional[float] = ...,
    can_next: Optional[bool] = ...,
    can_previous: Optional[bool] = ...,
) -> Dict[str, Any]: ...

def set_queue(
    songs: Sequence[Dict[str, Any] | Song],
    start_index: int = ...,
    play_mode: Optional[PlayMode | str] = ...,
    autoplay: bool = ...,
    preload_count: int = ...,
) -> Dict[str, Any]: ...

def queue() -> Dict[str, Any]: ...

def current() -> Dict[str, Any]: ...

def add(song: Dict[str, Any] | Song, play_next: bool = ..., autoplay: bool = ...) -> Dict[str, Any]: ...

def remove(index: int) -> Dict[str, Any]: ...

def move(from_index: int, to_index: int) -> Dict[str, Any]: ...

def clear() -> None: ...

def prepare(song: Dict[str, Any] | Song, index: Optional[int] = ...) -> Dict[str, Any]: ...

def prefetch_next(count: int = ...) -> Dict[str, Any]: ...

def preload_state() -> Dict[str, Any]: ...

def play() -> bool: ...

def pause() -> None: ...

def toggle() -> bool: ...

def stop() -> None: ...

def next() -> bool: ...

def previous() -> bool: ...

def seek(seconds: float) -> Dict[str, Any]: ...

def set_play_mode(mode: PlayMode | str) -> Dict[str, Any]: ...

def set_volume(volume: float) -> Dict[str, Any]: ...

def set_rate(rate: float) -> Dict[str, Any]: ...

def state() -> Dict[str, Any]: ...

def restore(autoplay: bool = ...) -> Dict[str, Any]: ...

def on_event(callback: str | Callable[[str], Any], events: Optional[str | Iterable[str]] = ...) -> Dict[str, Any]: ...

def off_event(callback_id: Optional[Any] = ...) -> Dict[str, Any]: ...
def set_queue_async(songs: Sequence[Dict[str, Any] | Song], start_index: int = ..., play_mode: Optional[PlayMode | str] = ..., autoplay: bool = ..., preload_count: int = ..., *, budget: ResourceBudget | Mapping[str, Any] | None = ...) -> OperationHandle: ...
def prepare_async(song: Dict[str, Any] | Song, index: Optional[int] = ..., *, budget: ResourceBudget | Mapping[str, Any] | None = ...) -> OperationHandle: ...
def restore_async(autoplay: bool = ..., *, budget: ResourceBudget | Mapping[str, Any] | None = ...) -> OperationHandle: ...

__all__ = [
    'PLAY_MODE_SEQUENCE', 'PLAY_MODE_REPEAT_ALL',
    'PLAY_MODE_REPEAT_ONE', 'PLAY_MODE_SHUFFLE',
    'MusicPlayerError',
    'status', 'release',
    'configure', 'set_queue', 'queue', 'current',
    'add', 'remove', 'move', 'clear',
    'prepare', 'prefetch_next', 'preload_state',
    'play', 'pause', 'toggle', 'stop', 'next', 'previous', 'seek',
    'set_play_mode', 'set_volume', 'set_rate',
    'state', 'restore',
    'on_event', 'off_event',
    'set_queue_async', 'prepare_async', 'restore_async',
]
