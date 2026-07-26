"""Type stubs for `foundation_models` public PythonIDE module."""

from __future__ import annotations

class FoundationModelsError(RuntimeError):
    code: object | None
    def __init__(self, message: str, code: object | None = ...) -> None: ...

def is_available() -> bool: ...

def respond(prompt: str, instructions: str | None = ...) -> str: ...

def summarize(text: str, max_sentences: int = ...) -> str: ...

def explain_error(error: str, code_snippet: str = ...) -> str: ...

__all__ = [
    'is_available', 'respond', 'summarize', 'explain_error',
    'FoundationModelsError',
]
