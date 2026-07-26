"""Type stubs for the native ``archive`` ZIP module."""

from __future__ import annotations

from os import PathLike as OSPathLike
from types import TracebackType
from typing import (
    Any, Dict, Iterable, List, Literal, NotRequired, Optional, Required,
    Type, TypedDict, Union,
)

PathLike = Union[str, bytes, OSPathLike[str], OSPathLike[bytes]]
_BytesLike = Union[bytes, bytearray, memoryview]
_CreateCompression = Literal["stored", "deflate"]
_UpdateCompression = Literal["preserve", "stored", "deflate"]

class _ArchiveRemoveOperation(TypedDict):
    action: Literal["remove"]
    entry_path: str

class _ArchiveSourceOperation(TypedDict, total=False):
    action: Required[Literal["add", "replace"]]
    entry_path: Required[str]
    source_path: Required[PathLike]
    compression: NotRequired[_UpdateCompression]
    mode: NotRequired[int]
    modified_at: NotRequired[float]

class _ArchiveDataOperation(TypedDict, total=False):
    action: Required[Literal["add", "replace"]]
    entry_path: Required[str]
    data: Required[_BytesLike]
    compression: NotRequired[_UpdateCompression]
    mode: NotRequired[int]
    modified_at: NotRequired[float]

class _ArchiveBase64Operation(TypedDict, total=False):
    action: Required[Literal["add", "replace"]]
    entry_path: Required[str]
    data_base64: Required[str]
    compression: NotRequired[_UpdateCompression]
    mode: NotRequired[int]
    modified_at: NotRequired[float]

class _ArchiveDirectoryOperation(TypedDict, total=False):
    action: Required[Literal["add", "replace"]]
    entry_path: Required[str]
    is_directory: Required[Literal[True]]
    compression: NotRequired[_UpdateCompression]
    mode: NotRequired[int]
    modified_at: NotRequired[float]

_ArchiveUpdateOperation = Union[
    _ArchiveRemoveOperation,
    _ArchiveSourceOperation,
    _ArchiveDataOperation,
    _ArchiveBase64Operation,
    _ArchiveDirectoryOperation,
]

MAX_ENTRIES: int
MAX_ENTRY_SIZE: int
MAX_TOTAL_SIZE: int
MAX_ARCHIVE_SIZE: int
MAX_COMPRESSION_RATIO: float
MAX_READ_SIZE: int
MAX_BRIDGE_PAYLOAD_BYTES: int
MAX_OPERATION_ID_BYTES: int
MAX_ENTRY_PATH_BYTES: int
MAX_PATH_COMPONENTS: int
MAX_COMPONENT_BYTES: int
MAX_METADATA_BYTES: int
MAX_BRIDGE_RESPONSE_BYTES: int

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

def read_entry(
    path: PathLike,
    entry_path: str,
    *,
    max_bytes: int = ...,
    operation_id: Optional[str] = ...,
    max_entries: int = ...,
    max_entry_size: int = ...,
    max_total_size: int = ...,
    max_archive_size: int = ...,
    max_compression_ratio: float = ...,
) -> bytes: ...

def extract_entry(
    path: PathLike,
    entry_path: str,
    destination_path: PathLike,
    *,
    overwrite: bool = ...,
    preserve_metadata: bool = ...,
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
    compression: _CreateCompression = ...,
    include_root: bool = ...,
    overwrite: bool = ...,
    operation_id: Optional[str] = ...,
    max_entries: int = ...,
    max_entry_size: int = ...,
    max_total_size: int = ...,
    max_archive_size: int = ...,
    max_compression_ratio: float = ...,
) -> Dict[str, Any]: ...

def update(
    path: PathLike,
    operations: Iterable[_ArchiveUpdateOperation],
    *,
    destination_path: Optional[PathLike] = ...,
    overwrite: bool = ...,
    operation_id: Optional[str] = ...,
    max_entries: int = ...,
    max_entry_size: int = ...,
    max_total_size: int = ...,
    max_archive_size: int = ...,
    max_compression_ratio: float = ...,
) -> Dict[str, Any]: ...

class ArchiveTransaction:
    path: PathLike
    options: Dict[str, Any]
    operations: List[Dict[str, Any]]
    result: Optional[Dict[str, Any]]
    def __init__(self, path: PathLike, **options: Any) -> None: ...
    def add(
        self, entry_path: str, *, source_path: Optional[PathLike] = ...,
        data: Optional[_BytesLike] = ..., is_directory: bool = ...,
        compression: _UpdateCompression = ..., mode: Optional[int] = ...,
        modified_at: Optional[float] = ...,
    ) -> ArchiveTransaction: ...
    def replace(
        self, entry_path: str, *, source_path: Optional[PathLike] = ...,
        data: Optional[_BytesLike] = ..., is_directory: bool = ...,
        compression: _UpdateCompression = ...,
        mode: Optional[int] = ..., modified_at: Optional[float] = ...,
    ) -> ArchiveTransaction: ...
    def remove(self, entry_path: str) -> ArchiveTransaction: ...
    def commit(self) -> Dict[str, Any]: ...
    def rollback(self) -> None: ...
    def __enter__(self) -> ArchiveTransaction: ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> bool: ...

def transaction(path: PathLike, **options: Any) -> ArchiveTransaction: ...
def add(path: PathLike, entry_path: str, **options: Any) -> Dict[str, Any]: ...
def replace(path: PathLike, entry_path: str, **options: Any) -> Dict[str, Any]: ...
def remove(path: PathLike, entry_path: str, **options: Any) -> Dict[str, Any]: ...

def cancel(operation_id: str) -> bool: ...
def progress(operation_id: str) -> Dict[str, Any]: ...

__all__ = [
    "ArchiveError",
    "inspect",
    "list",
    "extract",
    "read_entry",
    "extract_entry",
    "create",
    "update",
    "transaction",
    "ArchiveTransaction",
    "add",
    "replace",
    "remove",
    "cancel",
    "progress",
    "new_operation_id",
]
