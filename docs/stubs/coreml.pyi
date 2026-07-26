"""Type stubs for `coreml` public PythonIDE module."""

from __future__ import annotations

from typing import Any


def list_models() -> list[str]: ...

def load_model(name: str) -> Any: ...

def predict_image(model: Any, image_path: str) -> list[dict[str, Any]]: ...

def model_info(model: Any) -> dict[str, Any]: ...


__all__ = ["list_models", "load_model", "predict_image", "model_info"]
