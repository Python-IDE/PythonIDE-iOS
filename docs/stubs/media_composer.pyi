"""Type stubs for `media_composer` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Iterable, Mapping, Optional
from appui_operations import OperationHandle, ResourceBudget
from appui_resources import FileResource

FileInput = str | FileResource

class MediaComposerError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def merge_videos(paths: Iterable[FileInput], output_path: FileInput) -> str: ...

def merge_audio(video_path: FileInput, audio_path: FileInput, output_path: FileInput) -> str: ...

def export(input_path: FileInput, output_path: FileInput, format: str = ...) -> str: ...

def merge_videos_async(paths: Iterable[FileInput], output_path: FileInput, *, budget: ResourceBudget | Mapping[str, Any] | None = ...) -> OperationHandle: ...

def merge_audio_async(video_path: FileInput, audio_path: FileInput, output_path: FileInput, *, budget: ResourceBudget | Mapping[str, Any] | None = ...) -> OperationHandle: ...

def export_async(input_path: FileInput, output_path: FileInput, format: str = ..., *, budget: ResourceBudget | Mapping[str, Any] | None = ...) -> OperationHandle: ...

__all__ = [
    'merge_videos', 'merge_audio', 'export', 'merge_videos_async',
    'merge_audio_async', 'export_async', 'MediaComposerError',
]
