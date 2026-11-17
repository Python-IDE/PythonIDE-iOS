"""Type stubs for `shortcuts` public PythonIDE module."""

from __future__ import annotations

from os import PathLike
from typing import List, Optional, Union

def run_shortcut(name: str) -> bool: ...

def open_url(url: str) -> bool: ...

def open_settings() -> bool: ...

def input_files() -> List[str]: ...

def output_file(name: str) -> str: ...

def return_file(path: Union[str, PathLike[str]], name: Optional[str] = None) -> str: ...

__all__ = [
    'run_shortcut',
    'open_url',
    'open_settings',
    'input_files',
    'output_file',
    'return_file',
]
