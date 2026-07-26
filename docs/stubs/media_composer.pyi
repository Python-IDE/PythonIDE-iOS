"""Type stubs for `media_composer` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Iterable, Optional

class MediaComposerError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def merge_videos(paths: Iterable[str], output_path: str) -> str: ...

def merge_audio(video_path: str, audio_path: str, output_path: str) -> str: ...

def export(input_path: str, output_path: str, format: str = ...) -> str: ...

__all__ = ['merge_videos', 'merge_audio', 'export', 'MediaComposerError']
