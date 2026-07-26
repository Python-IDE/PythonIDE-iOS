"""Type stubs for `pdf` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Dict, Iterable, Optional

class PDFError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def create_from_text(path: str, text: str, title: Optional[str] = ...) -> str: ...

def create_from_images(path: str, image_paths: Iterable[str]) -> str: ...

def from_html(html: str, path: str) -> str: ...

def extract_text(path: str) -> str: ...

def info(path: str) -> Dict[str, Any]: ...

def page_image(path: str, index: int = ..., scale: float = ...) -> bytes: ...

def preview(path: str) -> bool: ...

__all__ = [
    'create_from_text', 'create_from_images', 'from_html',
    'extract_text', 'info', 'page_image', 'preview',
    'PDFError',
]
