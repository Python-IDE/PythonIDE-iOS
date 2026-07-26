"""Type stubs for `storekit` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Dict, Iterable, List, Optional

class StoreKitError(RuntimeError):
    code: Optional[Any]
    def __init__(self, message: str, code: Optional[Any] = ...) -> None: ...

def load_products(identifiers: Iterable[str]) -> List[Dict[str, Any]]: ...

def purchase(product_id: str) -> Dict[str, Any]: ...

def restore() -> List[str]: ...

def subscription_status() -> List[Dict[str, Any]]: ...

def show_manage_subscriptions() -> None: ...

__all__ = [
    'load_products', 'purchase', 'restore', 'subscription_status',
    'show_manage_subscriptions', 'StoreKitError',
]
