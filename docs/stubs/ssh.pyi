"""Type stubs for `ssh` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Dict, Optional

class SSHError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def connect(host: str, username: str, password: Optional[str] = ..., port: int = ..., private_key: Optional[str] = ..., passphrase: Optional[str] = ...) -> str: ...

def execute(session_id: str, command: str, timeout: float = ...) -> Dict[str, Any]: ...

def upload(session_id: str, local_path: str, remote_path: str) -> None: ...

def download(session_id: str, remote_path: str, local_path: str) -> None: ...

def disconnect(session_id: str) -> None: ...

__all__ = ['connect', 'execute', 'upload', 'download', 'disconnect', 'SSHError']
