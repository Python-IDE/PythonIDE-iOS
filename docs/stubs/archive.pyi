"""Type stubs for the native ``archive`` ZIP module."""

from __future__ import annotations

from typing import Any, Dict, List, Optional, Union

PathLike = Union[str, bytes]

MAX_ENTRIES: int
MAX_ENTRY_SIZE: int
MAX_TOTAL_SIZE: int
MAX_ARCHIVE_SIZE: int
MAX_COMPRESSION_RATIO: float

class ArchiveError(RuntimeError):
    code: Optional[str]
    def __init__(self, message: str, code: Optional[str] = ...) -> None: ...

def new_operation_id() -> str: ...

def inspect(
    path: PathLike,
    *,
    operation_id: Optional[str] = ...,
    max_entries: int = ...,
    max_entry_size: int = ...,
    max_total_size: int = ...,
    max_archive_size: int = ...,
    max_compression_ratio: float = ...,
) -> Dict[str, Any]: ...

def list(
    path: PathLike,
    *,
    include_directories: bool = ...,
    operation_id: Optional[str] = ...,
    max_entries: int = ...,
    max_entry_size: int = ...,
    max_total_size: int = ...,
    max_archive_size: int = ...,
    max_compression_ratio: float = ...,
) -> List[Dict[str, Any]]: ...

def extract(
    path: PathLike,
    destination_path: PathLike,
    *,
    overwrite: bool = ...,
    operation_id: Optional[str] = ...,
    max_entries: int = ...,
    max_entry_size: int = ...,
    max_total_size: int = ...,
    max_archive_size: int = ...,
    max_compression_ratio: float = ...,
) -> Dict[str, Any]: ...

def create(
    source_path: PathLike,
    destination_path: PathLike,
    *,
    compression: str = ...,
    include_root: bool = ...,
    overwrite: bool = ...,
    operation_id: Optional[str] = ...,
    max_entries: int = ...,
    max_entry_size: int = ...,
    max_total_size: int = ...,
    max_archive_size: int = ...,
    max_compression_ratio: float = ...,
) -> Dict[str, Any]: ...

def cancel(operation_id: str) -> bool: ...

__all__ = [
    "ArchiveError",
    "inspect",
    "list",
    "extract",
    "create",
    "cancel",
    "new_operation_id",
]
