"""Type stubs for the durable ``background_download`` task center."""

from __future__ import annotations

from typing import Dict, List, Literal, Mapping, Optional, TypedDict

TransferState = Literal[
    'running', 'pausing', 'paused', 'finalizing', 'completed', 'failed', 'cancelled'
]
TransferStatusState = Literal[
    'running', 'pausing', 'paused', 'finalizing', 'completed', 'failed', 'cancelled',
    'unknown',
]
TransferKind = Literal['download', 'upload']

class TransferEvent(TypedDict):
    sequence: int
    timestamp: float
    type: str
    state: TransferState
    progress: float
    code: Optional[str]
    message: Optional[str]

class TransferStatus(TypedDict, total=False):
    task_id: str
    provider: Literal['background_transfer']
    kind: TransferKind
    owner_app_id: Optional[str]
    origin_session_id: str
    origin_run_state: Literal['current', 'interrupted', 'host']
    state: TransferStatusState
    progress: float
    path: Optional[str]
    error: Optional[str]
    error_code: Optional[str]
    attempt: int
    retry_count: int
    resume_count: int
    can_pause: bool
    can_resume: bool
    can_retry: bool
    retry_requires_headers: List[str]
    http_status: Optional[int]
    response_headers: Dict[str, str]
    bytes_received: int
    bytes_expected_to_receive: int
    bytes_sent: int
    bytes_expected_to_send: int
    expected_sha256: Optional[str]
    sha256: Optional[str]
    created_at: float
    updated_at: float
    last_retry_at: Optional[float]
    events: List[TransferEvent]

class BackgroundDownloadError(RuntimeError):
    code: Optional[str]
    def __init__(self, message: str, code: Optional[str] = ...) -> None: ...

def download(
    url: str,
    destination_path: str,
    task_id: Optional[str] = ...,
    *,
    method: str = ...,
    headers: Optional[Mapping[str, str]] = ...,
    sha256: Optional[str] = ...,
) -> str: ...

def upload(
    url: str,
    source_path: str,
    task_id: Optional[str] = ...,
    *,
    method: str = ...,
    headers: Optional[Mapping[str, str]] = ...,
    sha256: Optional[str] = ...,
) -> str: ...

def status(task_id: str) -> TransferStatus: ...
def list(
    *,
    state: Optional[TransferState] = ...,
    kind: Optional[TransferKind] = ...,
    limit: int = ...,
) -> List[TransferStatus]: ...
def cancel(task_id: str) -> None: ...
def pause(task_id: str) -> TransferStatus: ...
def resume(task_id: str) -> TransferStatus: ...
def retry(
    task_id: str,
    *,
    headers: Optional[Mapping[str, str]] = ...,
) -> TransferStatus: ...

__all__ = [
    'download', 'upload', 'status', 'list', 'cancel', 'pause', 'resume',
    'retry', 'BackgroundDownloadError',
]
