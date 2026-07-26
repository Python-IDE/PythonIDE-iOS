"""Type stubs for `http_server` public PythonIDE module."""

from __future__ import annotations

from os import PathLike
from typing import Literal, NotRequired, Optional, TypedDict, Union

class HttpServerStatus(TypedDict):
    running: bool
    port: int
    url: Optional[str]
    root_dir: str
    bind_host: str
    range_policy: str
    active_connections: int
    requests_served: int
    bytes_sent: int
    browser_url: NotRequired[str]
    server_id: NotRequired[str]
    started_at: NotRequired[str]

class HttpServerError(RuntimeError):
    code: Optional[str]
    def __init__(self, message: str, code: Optional[str] = ...) -> None: ...

def start(
    port: int = ...,
    root_dir: Optional[Union[str, PathLike[str]]] = ...,
    *,
    url_mode: Literal["universal", "browser"] = ...,
) -> str: ...

def stop() -> None: ...

def status() -> HttpServerStatus: ...

__all__ = ['start', 'stop', 'status', 'HttpServerError']
