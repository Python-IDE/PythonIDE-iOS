"""Type stubs for `objc_util` public PythonIDE module."""

from __future__ import annotations

from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

c: Any

LP64: Any

CGFloat: Any

NSInteger: Any

NSUInteger: Any

NSNotFound: Any

NSUTF8StringEncoding: int

NS_UTF8: Any

class CGPoint:
    ...

class CGSize:
    ...

class CGVector:
    ...

class CGRect:
    ...

class CGAffineTransform:
    ...

class UIEdgeInsets:
    ...

class NSRange:
    ...

def sel(sel_name: Any) -> Any: ...

class ObjCClass:
    def __init__(self, name: Any) -> None: ...
    @classmethod
    def get_names(cls, prefix: Any | None = ...) -> Any: ...
    @classmethod
    def create(cls, *args: Any, **kwargs: Any) -> Any: ...

class ObjCInstance:
    ...

class ObjCClassMethod:
    def __init__(self, cls, method_name: Any) -> None: ...

class ObjCInstanceMethod:
    def __init__(self, obj: Any, method_name: Any, allow_property: bool = ...) -> None: ...

NSObject: Any

NSArray: Any

NSMutableArray: Any

NSDictionary: Any

NSMutableDictionary: Any

NSSet: Any

NSMutableSet: Any

NSString: Any

NSMutableString: Any

NSData: Any

NSMutableData: Any

NSNumber: Any

NSURL: Any

NSEnumerator: Any

NSThread: Any

NSBundle: Any

UIColor: Any

UIImage: Any

UIBezierPath: Any

UIApplication: Any

UIView: Any

class ObjCBlock:
    def __init__(self, func: Any, restype: Any | None = ..., argtypes: Any | None = ...) -> None: ...
    @classmethod
    def from_param(cls, param: Any) -> Any: ...

def ns(py_obj: Any) -> Any: ...

def nsurl(url_or_path: Any) -> Any: ...

def retain_global(obj: Any) -> Any: ...

def release_global(obj: Any) -> Any: ...

def on_main_thread(func: Any) -> Any: ...

def create_objc_class(name: Any, superclass: Any = ..., methods: list[Any] = ..., classmethods: list[Any] = ..., protocols: list[Any] = ..., debug: bool = ...) -> Any: ...

Structure: Any

sizeof: Any

byref: Any

c_void_p: Any

c_char: Any

c_byte: Any

c_char_p: Any

c_double: Any

c_float: Any

c_int: Any

c_longlong: Any

c_short: Any

c_bool: Any

c_long: Any

c_int32: Any

c_ubyte: Any

c_uint: Any

c_ushort: Any

c_ulong: Any

c_ulonglong: Any

POINTER: Any

pointer: Any

def load_framework(name: Any) -> Any: ...

def nsdata_to_bytes(data: Any) -> Any: ...

def uiimage_to_png(img: Any) -> Any: ...

def autoreleasepool() -> Any: ...

__all__ = ['c', 'LP64', 'CGFloat', 'NSInteger', 'NSUInteger', 'NSNotFound', 'NSUTF8StringEncoding', 'NS_UTF8', 'CGPoint', 'CGSize', 'CGVector', 'CGRect', 'CGAffineTransform', 'UIEdgeInsets', 'NSRange', 'sel', 'ObjCClass', 'ObjCInstance', 'ObjCClassMethod', 'ObjCInstanceMethod', 'NSObject', 'NSArray', 'NSMutableArray', 'NSDictionary', 'NSMutableDictionary', 'NSSet', 'NSMutableSet', 'NSString', 'NSMutableString', 'NSData', 'NSMutableData', 'NSNumber', 'NSURL', 'NSEnumerator', 'NSThread', 'NSBundle', 'UIColor', 'UIImage', 'UIBezierPath', 'UIApplication', 'UIView', 'ObjCBlock', 'ns', 'nsurl', 'retain_global', 'release_global', 'on_main_thread', 'create_objc_class', 'Structure', 'sizeof', 'byref', 'c_void_p', 'c_char', 'c_byte', 'c_char_p', 'c_double', 'c_float', 'c_int', 'c_longlong', 'c_short', 'c_bool', 'c_long', 'c_int32', 'c_ubyte', 'c_uint', 'c_ushort', 'c_ulong', 'c_ulonglong', 'POINTER', 'pointer', 'load_framework', 'nsdata_to_bytes', 'uiimage_to_png', 'autoreleasepool']
