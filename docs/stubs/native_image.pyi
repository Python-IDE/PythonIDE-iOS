from __future__ import annotations

from typing import Any, Dict, List, Optional, Sequence

class NativeImageError(RuntimeError):
    code: Optional[str]
    def __init__(self, message: str, code: Optional[str] = ...) -> None: ...

def inspect(source_path: str, *, frame_index: int = ...) -> Dict[str, Any]: ...
def process(
    source_path: str,
    destination_path: str,
    *,
    resize: Optional[Dict[str, Any]] = ...,
    crop: Optional[Dict[str, Any]] = ...,
    rotate_degrees: float = ...,
    flip_horizontal: bool = ...,
    flip_vertical: bool = ...,
    filters: Optional[Sequence[Dict[str, Any]]] = ...,
    format: Optional[str] = ...,
    quality: float = ...,
    frame_index: int = ...,
) -> Dict[str, Any]: ...
def resize(
    source_path: str,
    destination_path: str,
    width: int,
    height: int,
    *,
    mode: str = ...,
    format: Optional[str] = ...,
    quality: float = ...,
    frame_index: int = ...,
) -> Dict[str, Any]: ...
def thumbnail(
    source_path: str,
    destination_path: str,
    max_size: int,
    *,
    format: Optional[str] = ...,
    quality: float = ...,
    frame_index: int = ...,
) -> Dict[str, Any]: ...
def crop(
    source_path: str,
    destination_path: str,
    x: float,
    y: float,
    width: float,
    height: float,
    *,
    format: Optional[str] = ...,
    quality: float = ...,
    frame_index: int = ...,
) -> Dict[str, Any]: ...
def rotate(
    source_path: str,
    destination_path: str,
    degrees: float,
    *,
    format: Optional[str] = ...,
    quality: float = ...,
    frame_index: int = ...,
) -> Dict[str, Any]: ...

__all__ = [
    "inspect",
    "process",
    "resize",
    "thumbnail",
    "crop",
    "rotate",
    "NativeImageError",
]
