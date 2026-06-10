"""widget — Python IDE 小组件模块 — Type stubs."""

import sys
from datetime import datetime
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

# ── Type aliases ──

ColorLike = Union[str, Tuple[str, str], Dict[str, Any]]
"""Solid color, (light, dark) pair, or structured Widget V3 color token."""

ImageLike = Union[str, Tuple[str, str], Dict[str, Any]]
"""Image reference string or light/dark image pair."""

WidgetBackground = Union[str, Tuple[str, str], Dict[str, Any]]
"""Widget root/surface/button background: solid, (light, dark), ``\"system\"``, or gradient dict."""

RichTextPart = Union[str, Tuple[Any, ...], Dict[str, Any]]
"""One rich text run: string, tuple like ``(text, color, weight)``, or dict."""

PathPoint = Union[Tuple[float, float], List[float], Dict[str, float]]
"""One path point as ``(x, y)``, ``[x, y]``, or ``{"x": x, "y": y}``."""

# ── Size / family constants (match iOS WidgetFamily) ──

SMALL = "small"
MEDIUM = "medium"
LARGE = "large"
CIRCULAR = "circular"
RECTANGULAR = "rectangular"
INLINE = "inline"

# ── Dynamic / module state ──

family: str
"""Current widget family (from ``WIDGET_FAMILY`` env, default ``medium``)."""

# ── Internal helper types exposed only for attribute typing ──


class _Params:
    def get(self, key: str, default: Any = None) -> Any: ...
    def declare(
        self,
        name: str,
        default: Any = "",
        *,
        title: Optional[str] = None,
        kind: str = "text",
        min: Optional[float] = None,
        max: Optional[float] = None,
        step: Optional[float] = None,
        options: Optional[Sequence[Any]] = None,
        extensions: Optional[Sequence[str]] = None,
        description: Optional[str] = None,
        group: Optional[str] = None,
        unit: Optional[str] = None,
        order: Optional[float] = None,
        hidden: bool = False,
        placeholder: Optional[str] = None,
        role: Optional[str] = None,
        live: Optional[bool] = None,
    ) -> Any: ...
    def text(
        self,
        name: str,
        default: str = "",
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        group: Optional[str] = None,
        order: Optional[float] = None,
        hidden: bool = False,
        placeholder: Optional[str] = None,
        role: Optional[str] = None,
        live: Optional[bool] = None,
    ) -> str: ...
    def color(
        self,
        name: str,
        default: ColorLike = "#2563EB",
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        group: Optional[str] = None,
        order: Optional[float] = None,
        hidden: bool = False,
        role: Optional[str] = None,
        live: bool = True,
    ) -> str: ...
    def file(
        self,
        name: str,
        default: str = "",
        *,
        title: Optional[str] = None,
        extensions: Optional[Sequence[str]] = None,
        description: Optional[str] = None,
        group: Optional[str] = None,
        order: Optional[float] = None,
        hidden: bool = False,
        placeholder: Optional[str] = None,
        role: Optional[str] = None,
        live: Optional[bool] = None,
    ) -> str: ...
    def number(
        self,
        name: str,
        default: Union[int, float] = 0,
        *,
        title: Optional[str] = None,
        min: Optional[float] = None,
        max: Optional[float] = None,
        step: Optional[float] = None,
        description: Optional[str] = None,
        group: Optional[str] = None,
        unit: Optional[str] = None,
        order: Optional[float] = None,
        hidden: bool = False,
        role: Optional[str] = None,
        live: bool = True,
    ) -> Union[int, float]: ...

    def slider(
        self,
        name: str,
        default: Union[int, float] = 0,
        *,
        title: Optional[str] = None,
        min: float = 0,
        max: float = 1,
        step: float = 0.01,
        description: Optional[str] = None,
        group: Optional[str] = None,
        unit: Optional[str] = None,
        order: Optional[float] = None,
        hidden: bool = False,
        role: Optional[str] = None,
        live: bool = True,
    ) -> Union[int, float]: ...
    def bool(
        self,
        name: str,
        default: bool = False,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        group: Optional[str] = None,
        order: Optional[float] = None,
        hidden: bool = False,
        role: Optional[str] = None,
        live: bool = True,
    ) -> bool: ...
    def choice(
        self,
        name: str,
        options: Sequence[Any],
        default: Optional[Any] = None,
        *,
        title: Optional[str] = None,
        description: Optional[str] = None,
        group: Optional[str] = None,
        order: Optional[float] = None,
        hidden: bool = False,
        role: Optional[str] = None,
        live: Optional[bool] = None,
    ) -> str: ...
    def __getattr__(self, name: str) -> Any: ...


class _WidgetColorProxy:
    def fixed(self, value: ColorLike) -> Dict[str, Any]: ...
    def adaptive(self, light: ColorLike, dark: ColorLike) -> Dict[str, Any]: ...
    def role(self, name: str) -> Dict[str, Any]: ...
    def semantic(self, name: str) -> Dict[str, Any]: ...


class _Storage:
    def get(self, key: str, default: Any = None) -> Any: ...
    def set(self, key: str, value: Any) -> None: ...


param: _Params
"""Studio-editable widget parameter declarations. Prefer ``widget.param`` in new scripts."""

params: _Params
"""Compatibility alias for ``widget.param``."""

color: _WidgetColorProxy
storage: _Storage


class _ContainerContext:
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[BaseException],
        exc_tb: Optional[Any],
    ) -> None: ...
    def shadow(
        self,
        color: ColorLike = "#000000",
        radius: float = 4,
        x: float = 0,
        y: float = 2,
    ) -> Self: ...
    def background(self, value: WidgetBackground) -> Self: ...
    def overlay(self, color: ColorLike = "#000000", opacity: float = 0.18) -> Self: ...
    def overlay_view(self, align: str = "center") -> Self: ...
    def clip(self, kind: str = "roundedRectangle", corner_radius: Optional[float] = None) -> Self: ...
    def clip_shape(self, kind: str = "roundedRectangle", corner_radius: Optional[float] = None) -> Self: ...
    def mask(self, kind: str = "roundedRectangle", corner_radius: Optional[float] = None) -> Self: ...
    def reverse_mask(self, kind: str = "roundedRectangle", corner_radius: Optional[float] = None) -> Self: ...
    def mask_view(self, align: str = "center") -> Self: ...
    def link(self, url: str) -> Self: ...
    def accessibility(
        self,
        label: Optional[str] = None,
        value: Optional[str] = None,
        hint: Optional[str] = None,
        hidden: Optional[bool] = None,
    ) -> Self: ...
    def animation(self, value: str = "default") -> Self: ...
    def content_transition(self, value: str = "opacity") -> Self: ...
    def transition(self, value: str = "opacity", edge: Optional[str] = None) -> Self: ...
    def id(self, value: Any) -> Self: ...
    def invalidatable(self, enabled: bool = True) -> Self: ...
    def plain(self, enabled: bool = True) -> Self: ...
    def button_style(self, value: str = "plain") -> Self: ...
    def toggle_style(self, value: str = "checkbox") -> Self: ...
    def control_style(self, value: str = "plain") -> Self: ...
    def control_layout(self, value: str = "overlay") -> Self: ...
    def pressed(self, **style: Any) -> Self: ...
    def normal(self, **style: Any) -> Self: ...
    def checked_marker(
        self,
        state: Optional[Any] = None,
        item: Optional[Any] = None,
        *,
        checked: Optional[bool] = None,
        color: ColorLike = "#F59E0B",
        dark_color: Optional[ColorLike] = None,
        width: Optional[float] = None,
        width2: Optional[float] = None,
        height: Optional[float] = None,
        tilt: Optional[float] = None,
        drift: Optional[float] = None,
    ) -> Self: ...
    def intent(self, action: Union[str, WidgetIntentSpec]) -> Self: ...
    def rotation(self, degrees: float) -> Self: ...
    def rotate(self, degrees: float) -> Self: ...
    def scale(self, value: float) -> Self: ...
    def accentable(self, enabled: bool = True) -> Self: ...
    def privacy_sensitive(self, enabled: bool = True) -> Self: ...
    def redacted(self, reason: str = "placeholder") -> Self: ...
    def capsule(
        self,
        tone: Optional[str] = None,
        padding: Optional[Union[int, float]] = None,
    ) -> Self: ...
    def soft_background(
        self,
        tone: Optional[str] = None,
        corner_radius: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
    ) -> Self: ...
    def slot(self, value: str) -> Self: ...
    def alignment(self, value: str) -> Self: ...
    def place(self, x: Optional[float] = None, y: Optional[float] = None, unit: str = "relative") -> Self: ...
    def position(self, x: Optional[float] = None, y: Optional[float] = None, unit: str = "points") -> Self: ...
    def pixel_perfect_center(self, enabled: bool = True) -> Self: ...
    def frame(self, **kwargs: Any) -> Self: ...
    def offset(self, x: float = 0, y: float = 0) -> Self: ...
    def layout_priority(self, value: float = 1) -> Self: ...
    def fixed_size(self, horizontal: bool = True, vertical: bool = True) -> Self: ...
    def importance(self, value: str = "primary") -> Self: ...
    def preserve(self, enabled: bool = True) -> Self: ...
    def overflow(
        self,
        action: Optional[str] = None,
        *,
        importance: Optional[str] = None,
        preserve: Optional[bool] = None,
    ) -> Self: ...
    def hide(self, *families: str) -> Self: ...


class _CanvasSize:
    width: float
    height: float
    family: str
    def __iter__(self) -> Any: ...


class _WidgetContext:
    family: str
    width: float
    height: float
    content_width: float
    content_height: float
    size: _CanvasSize
    content_size: _CanvasSize
    def is_family(self, *families: str) -> bool: ...
    def value(self, default: Any = None, **values: Any) -> Any: ...


class _CanvasFrame:
    x: float
    y: float
    width: float
    height: float
    center_x: float
    center_y: float
    center: Tuple[float, float]
    frame: Dict[str, float]
    def inset(
        self,
        value: Union[int, float] = 0,
        *,
        horizontal: Optional[float] = None,
        vertical: Optional[float] = None,
        top: Optional[float] = None,
        leading: Optional[float] = None,
        bottom: Optional[float] = None,
        trailing: Optional[float] = None,
    ) -> "_CanvasFrame": ...
    def apply(self, target: Union["_WidgetNodeHandle", _ContainerContext]) -> Union["_WidgetNodeHandle", _ContainerContext]: ...


class _CanvasGrid:
    bounds: _CanvasFrame
    rows: int
    columns: int
    cell_width: float
    cell_height: float
    def cell(
        self,
        index: Optional[int] = None,
        column: Optional[int] = None,
        row: Optional[int] = None,
        *,
        col: Optional[int] = None,
        row_span: int = 1,
        column_span: int = 1,
        col_span: Optional[int] = None,
        inset: Union[int, float] = 0,
    ) -> _CanvasFrame: ...
    def horizontal_rule(self, index: int, thickness: Optional[float] = None) -> _CanvasFrame: ...
    def vertical_rule(self, index: int, thickness: Optional[float] = None) -> _CanvasFrame: ...
    def horizontal_rules(self, thickness: Optional[float] = None) -> List[_CanvasFrame]: ...
    def vertical_rules(self, thickness: Optional[float] = None) -> List[_CanvasFrame]: ...


class _CanvasContext(_ContainerContext):
    size: _CanvasSize
    def frame(
        self,
        x: float = 0,
        y: float = 0,
        width: Optional[float] = None,
        height: Optional[float] = None,
        *,
        inset: Union[int, float] = 0,
    ) -> _CanvasFrame: ...
    def grid(
        self,
        rows: int,
        columns: int,
        *,
        padding: Union[int, float] = 0,
        gap: Union[int, float] = 0,
        row_gap: Optional[float] = None,
        column_gap: Optional[float] = None,
        line_width: Optional[float] = None,
        border: bool = False,
        x: float = 0,
        y: float = 0,
        width: Optional[float] = None,
        height: Optional[float] = None,
    ) -> _CanvasGrid: ...
    def place_in(self, target: Union["_WidgetNodeHandle", _ContainerContext], frame: _CanvasFrame) -> Union["_WidgetNodeHandle", _ContainerContext]: ...
    def rect_in(
        self,
        frame: _CanvasFrame,
        color: Optional[ColorLike] = None,
        *,
        corner_radius: Optional[float] = None,
        opacity: Optional[float] = None,
    ) -> "_WidgetNodeHandle": ...
    def line(
        self,
        x1: float,
        y1: float,
        x2: float,
        y2: float,
        color: Optional[ColorLike] = None,
        *,
        width: Union[float, str] = 1,
        opacity: Optional[float] = None,
        cap: Optional[str] = None,
        join: Optional[str] = None,
        dash: Optional[Sequence[float]] = None,
        miter_limit: Optional[float] = None,
    ) -> "_WidgetNodeHandle": ...


class _TableContext(_ContainerContext):
    rows: int
    columns: int
    def cell(
        self,
        row: int,
        column: Optional[int] = None,
        *,
        col: Optional[int] = None,
        row_span: int = 1,
        column_span: int = 1,
        col_span: Optional[int] = None,
        inset: Optional[float] = None,
        align: str = "center",
    ) -> _ContainerContext: ...


class _WidgetNodeHandle:
    def __enter__(self) -> Self: ...
    def __exit__(
        self,
        exc_type: Optional[type],
        exc_val: Optional[BaseException],
        exc_tb: Optional[Any],
    ) -> None: ...
    def _set_color(self, value: ColorLike, key: str = "color") -> Self: ...
    def _set_background(self, value: WidgetBackground) -> Self: ...
    def _set_frame(self, frame: Dict[str, Any]) -> Self: ...
    def color(self, value: ColorLike) -> Self: ...
    def tone(self, value: str) -> Self: ...
    def font(
        self,
        value: Optional[Union[str, int, float, Dict[str, Any]]] = None,
        *,
        size: Optional[Union[float, Dict[str, Any]]] = None,
        weight: Optional[str] = None,
        **size_values: Any,
    ) -> Self: ...
    def font_style(self, style: str) -> Self: ...
    def font_size(self, size: float) -> Self: ...
    def font_weight(self, weight: str) -> Self: ...
    def font_width(self, width: str) -> Self: ...
    def monospaced(self, enabled: bool = True) -> Self: ...
    def monospaced_digit(self, enabled: bool = True) -> Self: ...
    def compressed(self, enabled: bool = True) -> Self: ...
    def height(self, value: Optional[Union[float, Dict[str, Any]]] = None, **values: Any) -> Self: ...
    def width(self, value: Optional[Union[float, Dict[str, Any]]] = None, **values: Any) -> Self: ...
    def padding(
        self,
        value: Optional[Union[int, float]] = None,
        *,
        horizontal: Optional[float] = None,
        vertical: Optional[float] = None,
        top: Optional[float] = None,
        leading: Optional[float] = None,
        bottom: Optional[float] = None,
        trailing: Optional[float] = None,
    ) -> Self: ...
    def align(self, value: str) -> Self: ...
    def corner_radius(self, value: float) -> Self: ...
    def opacity(self, value: float) -> Self: ...
    def guide_lines(self, count: Union[bool, int] = True, color: Optional[ColorLike] = None) -> Self: ...
    def grid(self, count: Union[bool, int] = True, color: Optional[ColorLike] = None) -> Self: ...
    def points(self, enabled: bool = True) -> Self: ...
    def fill(self, enabled: bool = True) -> Self: ...
    def line_width(self, value: Union[float, str]) -> Self: ...
    def stroke(
        self,
        color: Optional[ColorLike] = None,
        *,
        width: Optional[Union[float, str]] = None,
        dash: Optional[Sequence[float]] = None,
        cap: Optional[str] = None,
        join: Optional[str] = None,
        miter_limit: Optional[float] = None,
    ) -> Self: ...
    def fill_color(self, value: ColorLike) -> Self: ...
    def track_color(self, value: ColorLike) -> Self: ...
    def bar_spacing(self, value: float) -> Self: ...
    def segment_colors(self, colors: List[ColorLike]) -> Self: ...
    def baseline(self, value: float = 0, color: Optional[ColorLike] = None) -> Self: ...
    def threshold(self, value: float, color: Optional[ColorLike] = None) -> Self: ...
    def labels(
        self,
        start: Optional[Union[str, int, float]] = None,
        end: Optional[Union[str, int, float]] = None,
        color: Optional[ColorLike] = None,
    ) -> Self: ...
    def line_limit(self, value: int) -> Self: ...
    def min_scale(self, value: float) -> Self: ...
    def animation(
        self,
        value: str = "default",
        *,
        duration: Optional[float] = None,
        value_by: Optional[Any] = None,
    ) -> Self: ...
    def content_transition(self, value: str = "opacity") -> Self: ...
    def transition(self, value: str = "opacity", edge: Optional[str] = None) -> Self: ...
    def id(self, value: Any) -> Self: ...
    def invalidatable(self, enabled: bool = True) -> Self: ...
    def plain(self, enabled: bool = True) -> Self: ...
    def button_style(self, value: str = "plain") -> Self: ...
    def toggle_style(self, value: str = "checkbox") -> Self: ...
    def control_style(self, value: str = "plain") -> Self: ...
    def control_layout(self, value: str = "overlay") -> Self: ...
    def pressed(self, **style: Any) -> Self: ...
    def normal(self, **style: Any) -> Self: ...
    def intent(self, action: Union[str, WidgetIntentSpec]) -> Self: ...
    def rotation(self, degrees: float) -> Self: ...
    def rotate(self, degrees: float) -> Self: ...
    def scale(self, value: Union[float, str]) -> Self: ...
    def rendering(self, mode: str, colors: Optional[Sequence[ColorLike]] = None) -> Self: ...
    def palette(self, colors: Sequence[ColorLike]) -> Self: ...
    def variant(self, value: str) -> Self: ...
    def accentable(self, enabled: bool = True) -> Self: ...
    def privacy_sensitive(self, enabled: bool = True) -> Self: ...
    def redacted(self, reason: str = "placeholder") -> Self: ...
    def shadow(
        self,
        color: ColorLike = "#000000",
        radius: float = 4,
        x: float = 0,
        y: float = 2,
    ) -> Self: ...
    def background(self, value: WidgetBackground) -> Self: ...
    def overlay(self, color: ColorLike = "#000000", opacity: float = 0.18) -> Self: ...
    def overlay_view(self, align: str = "center") -> _ContainerContext: ...
    def clip(self, kind: str = "roundedRectangle", corner_radius: Optional[float] = None) -> Self: ...
    def clip_shape(self, kind: str = "roundedRectangle", corner_radius: Optional[float] = None) -> Self: ...
    def mask(self, kind: str = "roundedRectangle", corner_radius: Optional[float] = None) -> Self: ...
    def reverse_mask(self, kind: str = "roundedRectangle", corner_radius: Optional[float] = None) -> Self: ...
    def mask_view(self, align: str = "center") -> _ContainerContext: ...
    def link(self, url: str) -> Self: ...
    def accessibility(
        self,
        label: Optional[str] = None,
        value: Optional[str] = None,
        hint: Optional[str] = None,
        hidden: Optional[bool] = None,
    ) -> Self: ...
    def capsule(
        self,
        tone: Optional[str] = None,
        padding: Optional[Union[int, float]] = None,
    ) -> Self: ...
    def soft_background(
        self,
        tone: Optional[str] = None,
        corner_radius: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
    ) -> Self: ...
    def slot(self, value: str) -> Self: ...
    def alignment(self, value: str) -> Self: ...
    def place(self, x: Optional[float] = None, y: Optional[float] = None, unit: str = "relative") -> Self: ...
    def position(self, x: Optional[float] = None, y: Optional[float] = None, unit: str = "points") -> Self: ...
    def pixel_perfect_center(self, enabled: bool = True) -> Self: ...
    def frame(self, **kwargs: Any) -> Self: ...
    def offset(self, x: float = 0, y: float = 0) -> Self: ...
    def layout_priority(self, value: float = 1) -> Self: ...
    def fixed_size(self, horizontal: bool = True, vertical: bool = True) -> Self: ...
    def importance(self, value: str = "primary") -> Self: ...
    def preserve(self, enabled: bool = True) -> Self: ...
    def overflow(
        self,
        action: Optional[str] = None,
        *,
        importance: Optional[str] = None,
        preserve: Optional[bool] = None,
    ) -> Self: ...
    def hide(self, *families: str) -> Self: ...


class _WidgetBlockHandle:
    def color(self, value: ColorLike) -> Self: ...
    def tone(self, value: str) -> Self: ...
    def accent(self, value: ColorLike) -> Self: ...
    def height(self, value: Optional[Union[float, Dict[str, Any]]] = None, **values: Any) -> Self: ...
    def width(self, value: Optional[Union[float, Dict[str, Any]]] = None, **values: Any) -> Self: ...
    def padding(
        self,
        value: Optional[Union[int, float]] = None,
        *,
        horizontal: Optional[float] = None,
        vertical: Optional[float] = None,
        top: Optional[float] = None,
        leading: Optional[float] = None,
        bottom: Optional[float] = None,
        trailing: Optional[float] = None,
    ) -> Self: ...
    def background(self, value: WidgetBackground) -> Self: ...
    def corner_radius(self, value: float) -> Self: ...
    def opacity(self, value: float) -> Self: ...
    def align(self, value: str) -> Self: ...
    def slot(self, value: str) -> Self: ...
    def font(
        self,
        value: Optional[Union[str, int, float, Dict[str, Any]]] = None,
        *,
        size: Optional[Union[float, Dict[str, Any]]] = None,
        weight: Optional[str] = None,
        **sizes: Any,
    ) -> Self: ...
    def monospaced(self, enabled: bool = True) -> Self: ...
    def compressed(self, enabled: bool = True) -> Self: ...
    def line_limit(self, value: int) -> Self: ...
    def min_scale(self, value: float) -> Self: ...
    def shadow(
        self,
        color: ColorLike = "#000000",
        radius: float = 4,
        x: float = 0,
        y: float = 2,
    ) -> Self: ...
    def animation(self, value: str = "default") -> Self: ...
    def transition(self, value: str = "opacity", edge: Optional[str] = None) -> Self: ...
    def id(self, value: Any) -> Self: ...
    def importance(self, value: str = "primary") -> Self: ...
    def preserve(self, enabled: bool = True) -> Self: ...
    def overflow(
        self,
        action: Optional[str] = None,
        *,
        importance: Optional[str] = None,
        preserve: Optional[bool] = None,
    ) -> Self: ...
    def hide(self, *families: str) -> Self: ...


def save_image(source: Union[str, bytes], name: str, *, variant: Optional[str] = None) -> str: ...


def preview(family: Optional[str] = None) -> None: ...


def reload_user_widgets() -> None: ...


def reload_test_widgets() -> None: ...


def family_value(default: Any = None, **values: Any) -> Any: ...


context: _WidgetContext


def history(
    key: str,
    value: Any = None,
    limit: int = 7,
    *,
    bucket: Optional[str] = "day",
    default: Any = None,
) -> Any: ...


def cache_json(
    url: str,
    *,
    ttl: Optional[float] = 3600,
    default: Any = None,
    params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    key: Optional[str] = None,
    timeout: float = 8,
) -> Any: ...


def schema() -> Dict[str, Any]: ...


def agent_schema() -> Dict[str, Any]: ...


def validate_layout(document: Union[Dict[str, Any], "Widget"], family: Optional[str] = None) -> Dict[str, Any]: ...


class WidgetIntentSpec:
    id: str
    kind: str
    args: Dict[str, str]
    requires_app_launch: bool
    def to_ir(self) -> Dict[str, Any]: ...


class _WidgetStateText(str):
    key: str
    state_type: str
    default: Any
    def text(self, template: str = "{}") -> "_WidgetStateText": ...
    def format(self, template: str = "{}") -> "_WidgetStateText": ...
    def prefix(self, value: Any) -> "_WidgetStateText": ...
    def suffix(self, value: Any) -> "_WidgetStateText": ...
    def set(self, value: Any) -> WidgetIntentSpec: ...


class _WidgetStateInt(int):
    key: str
    state_type: str
    default: int
    def text(self, template: str = "{}") -> _WidgetStateText: ...
    def format(self, template: str = "{}") -> _WidgetStateText: ...
    def prefix(self, value: Any) -> _WidgetStateText: ...
    def suffix(self, value: Any) -> _WidgetStateText: ...
    def set(self, value: Union[int, float]) -> WidgetIntentSpec: ...
    def increment(self, by: Union[int, float] = 1) -> WidgetIntentSpec: ...
    def decrement(self, by: Union[int, float] = 1) -> WidgetIntentSpec: ...


class _WidgetStateFloat(float):
    key: str
    state_type: str
    default: float
    def text(self, template: str = "{}") -> _WidgetStateText: ...
    def format(self, template: str = "{}") -> _WidgetStateText: ...
    def prefix(self, value: Any) -> _WidgetStateText: ...
    def suffix(self, value: Any) -> _WidgetStateText: ...
    def set(self, value: Union[int, float]) -> WidgetIntentSpec: ...
    def increment(self, by: Union[int, float] = 1) -> WidgetIntentSpec: ...
    def decrement(self, by: Union[int, float] = 1) -> WidgetIntentSpec: ...


class _WidgetStateString(str):
    key: str
    state_type: str
    default: str
    def text(self, template: str = "{}") -> _WidgetStateText: ...
    def format(self, template: str = "{}") -> _WidgetStateText: ...
    def prefix(self, value: Any) -> _WidgetStateText: ...
    def suffix(self, value: Any) -> _WidgetStateText: ...
    def set(self, value: str) -> WidgetIntentSpec: ...


class _WidgetStateBool:
    key: str
    state_type: str
    default: bool
    def __bool__(self) -> bool: ...
    def text(self, template: str = "{}") -> _WidgetStateText: ...
    def format(self, template: str = "{}") -> _WidgetStateText: ...
    def prefix(self, value: Any) -> _WidgetStateText: ...
    def suffix(self, value: Any) -> _WidgetStateText: ...
    def set(self, value: bool) -> WidgetIntentSpec: ...
    def toggle(self) -> WidgetIntentSpec: ...


class _WidgetStateList(List[Any]):
    key: str
    state_type: str
    default: List[Any]
    def contains(self, item: Any) -> bool: ...
    def toggle_item(self, item: Any) -> WidgetIntentSpec: ...


class _WidgetStateProxy:
    def get(self, key: str, default: Any = None) -> Any: ...
    def set(self, key: str, value: Any) -> Any: ...
    def int(self, key: str, default: int = 0) -> _WidgetStateInt: ...
    def float(self, key: str, default: float = 0.0) -> _WidgetStateFloat: ...
    def bool(self, key: str, default: bool = False) -> _WidgetStateBool: ...
    def str(self, key: str, default: str = "") -> _WidgetStateString: ...
    def list(self, key: str, default: Optional[Sequence[Any]] = None) -> _WidgetStateList: ...
    def set_intent(self, key: str, value: Any) -> WidgetIntentSpec: ...
    def toggle_intent(self, key: str) -> WidgetIntentSpec: ...
    def toggle_item_intent(self, key: str, item: Any) -> WidgetIntentSpec: ...
    def increment_intent(self, key: str, by: Union[int, float] = 1) -> WidgetIntentSpec: ...
    def decrement_intent(self, key: str, by: Union[int, float] = 1) -> WidgetIntentSpec: ...


state: _WidgetStateProxy


class _WidgetEntryText(str):
    key: str
    def text(self, template: str = "{}") -> "_WidgetEntryText": ...
    def format(self, template: str = "{}") -> "_WidgetEntryText": ...
    def prefix(self, value: Any) -> "_WidgetEntryText": ...
    def suffix(self, value: Any) -> "_WidgetEntryText": ...


class _WidgetEntryValue(str):
    key: str
    entry_type: str
    default: Any
    def text(self, template: str = "{}") -> _WidgetEntryText: ...
    def format(self, template: str = "{}") -> _WidgetEntryText: ...
    def prefix(self, value: Any) -> _WidgetEntryText: ...
    def suffix(self, value: Any) -> _WidgetEntryText: ...


class _WidgetEntryProxy:
    def value(self, key: str, default: Any = "", type: str = "str") -> _WidgetEntryValue: ...
    def int(self, key: str, default: int = 0) -> _WidgetEntryValue: ...
    def float(self, key: str, default: float = 0.0) -> _WidgetEntryValue: ...
    def bool(self, key: str, default: bool = False) -> _WidgetEntryValue: ...
    def str(self, key: str, default: str = "") -> _WidgetEntryValue: ...
    def __getattr__(self, key: str) -> _WidgetEntryValue: ...
    def __getitem__(self, key: str) -> _WidgetEntryValue: ...


entry: _WidgetEntryProxy


class _WidgetActionProxy:
    def set(self, key: str, value: Any) -> WidgetIntentSpec: ...
    def toggle(self, key: str) -> WidgetIntentSpec: ...
    def toggle_item(self, key: str, item: Any) -> WidgetIntentSpec: ...
    def increment(self, key: str, by: Union[int, float] = 1) -> WidgetIntentSpec: ...
    def decrement(self, key: str, by: Union[int, float] = 1) -> WidgetIntentSpec: ...
    def refresh(self) -> WidgetIntentSpec: ...
    def open_app(self, **kwargs: Any) -> WidgetIntentSpec: ...
    def open_project(self, project_id: Optional[str] = None, **kwargs: Any) -> WidgetIntentSpec: ...
    def run_last_script(self, **kwargs: Any) -> WidgetIntentSpec: ...
    def new_script(self, **kwargs: Any) -> WidgetIntentSpec: ...
    def custom(self, action_id: str, *, kind: Optional[str] = None, requires_app_launch: bool = True, **kwargs: Any) -> WidgetIntentSpec: ...


action: _WidgetActionProxy


class _WidgetIntentFactory(_WidgetActionProxy):
    def __call__(
        self,
        action: Any = None,
        *,
        kind: Optional[str] = None,
        requires_app_launch: Optional[bool] = None,
        **kwargs: Any,
    ) -> WidgetIntentSpec: ...


intent: _WidgetIntentFactory


class Widget:
    def __init__(
        self,
        background: Optional[WidgetBackground] = None,
        padding: Optional[Union[int, float]] = None,
        *,
        style: Optional[str] = None,
        layout: str = "auto",
    ) -> None: ...
    @property
    def context(self) -> _WidgetContext: ...
    def background(self, value: WidgetBackground) -> "Widget": ...
    def container_background(
        self,
        value: Optional[WidgetBackground] = None,
        *,
        removable: Optional[bool] = None,
    ) -> "Widget": ...
    def content_margins(
        self,
        enabled: bool = True,
        padding: Optional[Union[int, float, Sequence[float], Dict[str, float]]] = None,
    ) -> "Widget": ...
    def transparent_background(self, enabled: bool = True) -> "Widget": ...

    # -- Semantic primitives --

    def title(self, content: Union[str, int, float]) -> _WidgetNodeHandle: ...
    def headline(self, content: Union[str, int, float]) -> _WidgetNodeHandle: ...
    def subheadline(self, content: Union[str, int, float]) -> _WidgetNodeHandle: ...
    def caption(self, content: Union[str, int, float]) -> _WidgetNodeHandle: ...
    def body(self, content: Union[str, int, float]) -> _WidgetNodeHandle: ...
    def label(
        self,
        content: Union[str, int, float],
        icon: Optional[str] = None,
        color: Optional[ColorLike] = None,
        size: Optional[float] = None,
        weight: Optional[str] = None,
        spacing: Optional[float] = None,
    ) -> _WidgetNodeHandle: ...
    def detail(self, content: Union[str, int, float]) -> _WidgetNodeHandle: ...
    def footnote(self, content: Union[str, int, float]) -> _WidgetNodeHandle: ...
    def note(self, content: Union[str, int, float]) -> _WidgetNodeHandle: ...
    def value(
        self,
        value: Union[str, int, float, _WidgetStateInt, _WidgetStateFloat, _WidgetStateString, _WidgetStateText],
        unit: Optional[str] = None,
        subtitle: Optional[str] = None,
        format: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...
    def number(
        self,
        value: Union[str, int, float],
        unit: Optional[str] = None,
        subtitle: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...
    def currency(
        self,
        value: Union[str, int, float],
        symbol: str = "¥",
        unit: Optional[str] = None,
        digits: int = 2,
    ) -> _WidgetNodeHandle: ...
    def percent(
        self,
        value: Union[int, float],
        total: float = 1.0,
        digits: int = 0,
        unit: str = "%",
    ) -> _WidgetNodeHandle: ...
    def change(
        self,
        primary: Union[str, int, float],
        secondary: Optional[Union[str, int, float]] = None,
        direction: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...
    def symbol(
        self,
        name: str,
        rendering: Optional[str] = None,
        palette: Optional[Sequence[ColorLike]] = None,
        variant: Optional[str] = None,
        scale: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...
    def svg(
        self,
        name: Optional[ImageLike] = None,
        width: Optional[float] = None,
        height: Optional[float] = None,
        color: Optional[ColorLike] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        content_mode: str = "fit",
        *,
        light: Optional[str] = None,
        dark: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...
    def sf_symbol(self, name: str) -> _WidgetNodeHandle: ...
    def badge(
        self,
        text: Union[str, int, float],
        icon: Optional[str] = None,
        tone: str = "accent",
        style: str = "plain",
    ) -> _WidgetNodeHandle: ...
    def status(
        self,
        text: Union[str, int, float],
        tone: str = "neutral",
        icon: Optional[str] = None,
        style: str = "plain",
    ) -> _WidgetNodeHandle: ...
    def tag(
        self,
        text: Union[str, int, float],
        tone: str = "neutral",
        icon: Optional[str] = None,
        style: str = "plain",
    ) -> _WidgetNodeHandle: ...
    def pill(
        self,
        text: Union[str, int, float],
        tone: str = "accent",
        icon: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...
    def line(
        self,
        data: Optional[Union[List[Union[int, float]], float]] = None,
        labels: Optional[List[Union[str, int, float]]] = None,
        colors: Optional[List[ColorLike]] = None,
        *args: float,
        x1: Optional[float] = None,
        y1: Optional[float] = None,
        x2: Optional[float] = None,
        y2: Optional[float] = None,
        color: Optional[ColorLike] = None,
        width: Union[float, str] = 1,
        cap: Optional[str] = None,
        join: Optional[str] = None,
        dash: Optional[Sequence[float]] = None,
        miter_limit: Optional[float] = None,
        coordinate_space: str = "points",
    ) -> _WidgetNodeHandle: ...
    def area(
        self,
        data: List[Union[int, float]],
        labels: Optional[List[Union[str, int, float]]] = None,
        colors: Optional[List[ColorLike]] = None,
    ) -> _WidgetNodeHandle: ...
    def spark(
        self,
        data: List[Union[int, float]],
        labels: Optional[List[Union[str, int, float]]] = None,
        colors: Optional[List[ColorLike]] = None,
    ) -> _WidgetNodeHandle: ...
    def bar(
        self,
        data: List[Union[int, float]],
        labels: Optional[List[Union[str, int, float]]] = None,
        colors: Optional[List[ColorLike]] = None,
    ) -> _WidgetNodeHandle: ...
    def bars(
        self,
        data: List[Union[int, float]],
        labels: Optional[List[Union[str, int, float]]] = None,
        colors: Optional[List[ColorLike]] = None,
    ) -> _WidgetNodeHandle: ...
    def ring(
        self,
        value: Union[int, float],
        total: float = 1.0,
        label: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...
    def donut(
        self,
        value: Union[int, float],
        total: float = 1.0,
        label: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...
    def radial(
        self,
        value: Union[int, float],
        total: float = 1.0,
        label: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...
    def meter(
        self,
        value: Union[int, float],
        total: float = 1.0,
        label: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...
    def row(
        self,
        spacing: Optional[Union[int, float]] = None,
        align: Optional[str] = None,
    ) -> _ContainerContext: ...
    def column(
        self,
        spacing: Optional[Union[int, float]] = None,
        align: Optional[str] = None,
    ) -> _ContainerContext: ...
    def layer(
        self,
        align: str = "center",
        padding: Optional[Union[int, float]] = None,
        background: Optional[WidgetBackground] = None,
        corner_radius: Optional[float] = None,
    ) -> _ContainerContext: ...
    def when(self, *families: str, layout: str = "layer") -> _ContainerContext: ...
    def unless(self, *families: str, layout: str = "layer") -> _ContainerContext: ...
    def canvas(
        self,
        height: Optional[float] = None,
        coordinate_space: str = "relative",
        align: str = "center",
        background: Optional[WidgetBackground] = None,
        padding: Optional[Union[int, float]] = None,
        corner_radius: Optional[float] = None,
        border_color: Optional[ColorLike] = None,
        border_width: Optional[float] = None,
        opacity: Optional[float] = None,
        frame: Optional[Dict[str, Any]] = None,
        fill: bool = False,
    ) -> _CanvasContext: ...
    def surface(
        self,
        role: str = "panel",
        spacing: Optional[Union[int, float]] = None,
        align: Optional[str] = None,
        padding: Optional[Union[int, float]] = None,
        background: Optional[WidgetBackground] = None,
        corner_radius: Optional[float] = None,
        border_color: Optional[ColorLike] = None,
        border_width: Optional[float] = None,
        shadow_color: Optional[ColorLike] = None,
        shadow_radius: Optional[float] = None,
    ) -> _ContainerContext: ...
    def section(
        self,
        title: Optional[Union[str, int, float]] = None,
        spacing: Optional[Union[int, float]] = None,
        subtitle: Optional[Union[str, int, float]] = None,
        style: Optional[str] = None,
    ) -> _ContainerContext: ...
    def list(
        self,
        items: List[Any],
        title: Optional[Union[str, int, float]] = None,
        limit: Optional[int] = None,
        empty_text: Optional[Union[str, int, float]] = None,
        dividers: bool = False,
    ) -> _ContainerContext: ...
    def countdown(
        self,
        title: Optional[Union[str, int, float]] = "Countdown",
        target: Optional[Union[datetime, str]] = None,
        subtitle: Optional[Union[str, int, float]] = None,
        icon: Optional[str] = None,
        tone: Optional[str] = None,
        accent: Optional[ColorLike] = None,
    ) -> _WidgetBlockHandle: ...
    def overlay(
        self,
        slot: str = "center",
        spacing: Optional[Union[int, float]] = None,
        align: Optional[str] = None,
    ) -> _ContainerContext: ...
    def region(
        self,
        slot: str = "center",
        spacing: Optional[Union[int, float]] = None,
        align: Optional[str] = None,
    ) -> _ContainerContext: ...
    def top(self, spacing: Optional[Union[int, float]] = None, align: Optional[str] = None) -> _ContainerContext: ...
    def top_leading(self, spacing: Optional[Union[int, float]] = None, align: Optional[str] = None) -> _ContainerContext: ...
    def top_trailing(self, spacing: Optional[Union[int, float]] = None, align: Optional[str] = None) -> _ContainerContext: ...
    def leading(self, spacing: Optional[Union[int, float]] = None, align: Optional[str] = None) -> _ContainerContext: ...
    def center(self, spacing: Optional[Union[int, float]] = None, align: Optional[str] = None) -> _ContainerContext: ...
    def trailing(self, spacing: Optional[Union[int, float]] = None, align: Optional[str] = None) -> _ContainerContext: ...
    def bottom(self, spacing: Optional[Union[int, float]] = None, align: Optional[str] = None) -> _ContainerContext: ...
    def bottom_leading(self, spacing: Optional[Union[int, float]] = None, align: Optional[str] = None) -> _ContainerContext: ...
    def bottom_trailing(self, spacing: Optional[Union[int, float]] = None, align: Optional[str] = None) -> _ContainerContext: ...

    # -- Basic elements --

    def text(
        self,
        content: Union[str, int, float],
        size: Optional[float] = None,
        weight: Optional[str] = None,
        color: Optional[ColorLike] = None,
        align: Optional[str] = None,
        max_lines: Optional[int] = None,
        design: Optional[str] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        frame: Optional[Dict[str, Any]] = None,
        minimum_scale_factor: Optional[float] = None,
        font_width: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...

    def rich_text(
        self,
        parts: List[RichTextPart],
        size: Optional[float] = None,
        weight: Optional[str] = None,
        color: Optional[ColorLike] = None,
        align: Optional[str] = None,
        max_lines: Optional[int] = None,
        design: Optional[str] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        frame: Optional[Dict[str, Any]] = None,
        minimum_scale_factor: Optional[float] = None,
        font_width: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...

    def icon(
        self,
        name: str,
        size: Optional[float] = None,
        color: Optional[ColorLike] = None,
        weight: Optional[str] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        frame: Optional[Dict[str, Any]] = None,
        rendering: Optional[str] = None,
        palette: Optional[Sequence[ColorLike]] = None,
        variant: Optional[str] = None,
        symbol_scale: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...

    def spacer(self, length: Optional[Union[int, float]] = None) -> _WidgetNodeHandle: ...

    def divider(
        self,
        color: Optional[ColorLike] = None,
        opacity: Optional[float] = None,
    ) -> _WidgetNodeHandle: ...

    def shape(
        self,
        kind: str = "rectangle",
        color: Optional[ColorLike] = None,
        width: Optional[float] = None,
        height: Optional[float] = None,
        size: Optional[float] = None,
        corner_radius: Optional[float] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        frame: Optional[Dict[str, Any]] = None,
        border_color: Optional[ColorLike] = None,
        border_width: Optional[float] = None,
        shadow_color: Optional[ColorLike] = None,
        shadow_radius: Optional[float] = None,
        shadow_x: float = 0,
        shadow_y: float = 2,
        stroke_color: Optional[ColorLike] = None,
        stroke_width: Optional[Union[float, str]] = None,
        dash: Optional[Sequence[float]] = None,
        line_cap: Optional[str] = None,
        line_join: Optional[str] = None,
        miter_limit: Optional[float] = None,
        top_leading_radius: Optional[float] = None,
        top_trailing_radius: Optional[float] = None,
        bottom_leading_radius: Optional[float] = None,
        bottom_trailing_radius: Optional[float] = None,
    ) -> _WidgetNodeHandle: ...
    def path(
        self,
        points: List[PathPoint],
        stroke: Optional[ColorLike] = None,
        fill: Optional[ColorLike] = None,
        line_width: Optional[Union[float, str]] = None,
        closed: bool = False,
        height: Optional[float] = None,
        coordinate_space: str = "relative",
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        frame: Optional[Dict[str, Any]] = None,
        line_cap: Optional[str] = None,
        line_join: Optional[str] = None,
        dash: Optional[Sequence[float]] = None,
        miter_limit: Optional[float] = None,
    ) -> _WidgetNodeHandle: ...

    def rectangle(
        self,
        color: Optional[ColorLike] = None,
        width: Optional[float] = None,
        height: Optional[float] = None,
        corner_radius: Optional[float] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        frame: Optional[Dict[str, Any]] = None,
        border_color: Optional[ColorLike] = None,
        border_width: Optional[float] = None,
    ) -> _WidgetNodeHandle: ...
    def rect(
        self,
        color: Optional[ColorLike] = None,
        width: Optional[float] = None,
        height: Optional[float] = None,
        corner_radius: Optional[float] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        frame: Optional[Dict[str, Any]] = None,
        border_color: Optional[ColorLike] = None,
        border_width: Optional[float] = None,
    ) -> _WidgetNodeHandle: ...

    def circle(
        self,
        color: Optional[ColorLike] = None,
        size: Optional[float] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        frame: Optional[Dict[str, Any]] = None,
        border_color: Optional[ColorLike] = None,
        border_width: Optional[float] = None,
    ) -> _WidgetNodeHandle: ...

    def capsule(
        self,
        color: Optional[ColorLike] = None,
        width: Optional[float] = None,
        height: Optional[float] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        frame: Optional[Dict[str, Any]] = None,
        border_color: Optional[ColorLike] = None,
        border_width: Optional[float] = None,
    ) -> _WidgetNodeHandle: ...

    def emoji(
        self,
        content: Union[str, int],
        size: Optional[float] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
    ) -> _WidgetNodeHandle: ...

    def progress(
        self,
        value: Union[int, float],
        total: float = 1.0,
        color: Optional[ColorLike] = None,
        height: Optional[float] = None,
        track_color: Optional[ColorLike] = None,
        *,
        title: Optional[str] = None,
        subtitle: Optional[str] = None,
        unit: Optional[str] = None,
        icon: Optional[str] = None,
        tone: Optional[str] = None,
        accent: Optional[str] = None,
        style: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...

    def sparkline(
        self,
        values: List[Union[int, float]],
        color: Optional[ColorLike] = None,
        height: Optional[float] = None,
        min_value: Optional[float] = None,
        max_value: Optional[float] = None,
        fill: bool = True,
        show_points: bool = False,
        line_width: Optional[float] = None,
        track_color: Optional[ColorLike] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        frame: Optional[Dict[str, Any]] = None,
        segment_colors: Optional[List[ColorLike]] = None,
        baseline: Optional[float] = None,
        threshold: Optional[float] = None,
        labels: Optional[Union[List[Any], Dict[str, Any]]] = None,
        label_color: Optional[ColorLike] = None,
    ) -> _WidgetNodeHandle: ...

    def line_chart(
        self,
        values: List[Union[int, float]],
        color: Optional[ColorLike] = None,
        height: Optional[float] = None,
        min_value: Optional[float] = None,
        max_value: Optional[float] = None,
        fill: bool = True,
        show_points: bool = True,
        line_width: Optional[float] = None,
        track_color: Optional[ColorLike] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        frame: Optional[Dict[str, Any]] = None,
        segment_colors: Optional[List[ColorLike]] = None,
        baseline: Optional[float] = None,
        threshold: Optional[float] = None,
        labels: Optional[Union[List[Any], Dict[str, Any]]] = None,
        label_color: Optional[ColorLike] = None,
    ) -> _WidgetNodeHandle: ...

    def bar_chart(
        self,
        values: List[Union[int, float]],
        color: Optional[ColorLike] = None,
        height: Optional[float] = None,
        min_value: Optional[float] = None,
        max_value: Optional[float] = None,
        spacing: Optional[float] = None,
        corner_radius: Optional[float] = None,
        track_color: Optional[ColorLike] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        frame: Optional[Dict[str, Any]] = None,
        segment_colors: Optional[List[ColorLike]] = None,
        baseline: Optional[float] = None,
        threshold: Optional[float] = None,
        labels: Optional[Union[List[Any], Dict[str, Any]]] = None,
        label_color: Optional[ColorLike] = None,
    ) -> _WidgetNodeHandle: ...

    def ring_chart(
        self,
        value: Union[int, float],
        total: float = 1.0,
        label: Optional[str] = None,
        color: Optional[ColorLike] = None,
        track_color: Optional[ColorLike] = None,
        size: Optional[float] = None,
        line_width: Optional[float] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        frame: Optional[Dict[str, Any]] = None,
    ) -> _WidgetNodeHandle: ...

    def gauge(
        self,
        value: Union[int, float],
        total: float = 1.0,
        label: Optional[str] = None,
        size: Optional[float] = None,
        color: Optional[ColorLike] = None,
        track_color: Optional[ColorLike] = None,
        line_width: Optional[Union[float, str]] = None,
        style: Optional[str] = None,
        current_value_label: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...

    def timer(
        self,
        target: Optional[Union[datetime, str]] = None,
        style: str = "timer",
        size: Optional[float] = None,
        weight: Optional[str] = None,
        color: Optional[ColorLike] = None,
        design: Optional[str] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        frame: Optional[Dict[str, Any]] = None,
        font_width: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...
    def date(self, target: Optional[Union[datetime, str]] = None, style: str = "date") -> _WidgetNodeHandle: ...
    def dynamic_date(self, target: Optional[Union[datetime, str]] = None, style: str = "date") -> _WidgetNodeHandle: ...
    def time(self, target: Optional[Union[datetime, str]] = None) -> _WidgetNodeHandle: ...
    def relative_time(self, target: Optional[Union[datetime, str]] = None) -> _WidgetNodeHandle: ...
    def timer_text(self, target: Optional[Union[datetime, str]] = None) -> _WidgetNodeHandle: ...
    def background_image(
        self,
        asset: Optional[ImageLike] = None,
        content_mode: str = "fill",
        dim: Optional[Union[bool, float]] = None,
        scrim: Optional[Union[bool, str]] = None,
        scrim_opacity: Optional[float] = None,
        focal: str = "center",
        overlay_color: ColorLike = "#000000",
        *,
        light: Optional[str] = None,
        dark: Optional[str] = None,
    ) -> "Widget": ...
    def background(self, value: WidgetBackground) -> "Widget": ...

    def image(
        self,
        name: Optional[ImageLike] = None,
        width: Optional[float] = None,
        height: Optional[float] = None,
        corner_radius: Optional[float] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        content_mode: Optional[str] = None,
        *,
        light: Optional[str] = None,
        dark: Optional[str] = None,
        rendering_mode: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...
    def photo(
        self,
        name: str,
        width: Optional[float] = None,
        height: Optional[float] = None,
        corner_radius: Optional[float] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        content_mode: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...
    def avatar(
        self,
        name: str,
        size: Optional[float] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
    ) -> _WidgetNodeHandle: ...
    def thumbnail(
        self,
        name: str,
        width: Optional[float] = None,
        height: Optional[float] = None,
        corner_radius: Optional[float] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
    ) -> _WidgetNodeHandle: ...

    def flip(
        self,
        value: Any,
        previous: Optional[Any] = None,
        *,
        direction: str = "up",
        width: Optional[float] = None,
        height: Optional[float] = None,
        size: Optional[float] = None,
        weight: str = "bold",
        color: Optional[ColorLike] = None,
        background: Optional[WidgetBackground] = None,
        corner_radius: Optional[float] = None,
        duration: float = 0.55,
        delta: Optional[float] = None,
        perspective: float = 0.62,
        shadow_opacity: float = 0.18,
        padding: Optional[Union[int, float]] = None,
        frame: Optional[Dict[str, Any]] = None,
        design: Optional[str] = "monospaced",
    ) -> _WidgetNodeHandle: ...

    def button(
        self,
        title: Optional[str] = None,
        action: Optional[Union[str, WidgetIntentSpec]] = None,
        url: Optional[str] = None,
        color: Optional[ColorLike] = None,
        background: Optional[WidgetBackground] = None,
        size: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        *,
        style: Optional[str] = None,
        layout: Optional[str] = None,
        press: Optional[Dict[str, Any]] = None,
        normal: Optional[Dict[str, Any]] = None,
    ) -> _WidgetNodeHandle: ...

    def link(
        self,
        title: str,
        url: str,
        icon: Optional[str] = None,
        color: Optional[ColorLike] = None,
    ) -> Union[_WidgetNodeHandle, _ContainerContext]: ...

    def toggle(
        self,
        title: Optional[str] = None,
        is_on: Union[bool, str] = False,
        action: Optional[Union[str, WidgetIntentSpec]] = None,
        url: Optional[str] = None,
        color: Optional[ColorLike] = None,
        background: Optional[WidgetBackground] = None,
        size: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        *,
        value: Optional[Union[bool, str]] = None,
        state: Optional[_WidgetStateBool] = None,
        style: Optional[str] = None,
        layout: Optional[str] = None,
        press: Optional[Dict[str, Any]] = None,
        normal: Optional[Dict[str, Any]] = None,
    ) -> _WidgetNodeHandle: ...

    # -- Containers (context managers) --

    def table(
        self,
        rows: int,
        columns: int,
        *,
        line_color: Optional[ColorLike] = None,
        line_width: Union[float, str] = "hairline",
        line_cap: str = "butt",
        line_join: str = "miter",
        dash: Optional[Sequence[float]] = None,
        miter_limit: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        frame: Optional[Dict[str, Any]] = None,
        width: Optional[float] = None,
        height: Optional[float] = None,
        background: Optional[WidgetBackground] = None,
        opacity: Optional[float] = None,
        corner_radius: Optional[float] = None,
        border: bool = True,
        fill: bool = True,
        align: str = "center",
    ) -> _TableContext: ...

    def grid(
        self,
        columns: int = 2,
        spacing: Optional[Union[int, float]] = None,
        row_spacing: Optional[Union[int, float]] = None,
        column_spacing: Optional[Union[int, float]] = None,
        align: Optional[str] = None,
        padding: Optional[Union[int, float]] = None,
        background: Optional[WidgetBackground] = None,
        opacity: Optional[float] = None,
        corner_radius: Optional[float] = None,
        border_color: Optional[ColorLike] = None,
        border_width: Optional[float] = None,
        url: Optional[str] = None,
        shadow_color: Optional[ColorLike] = None,
        shadow_radius: Optional[float] = None,
        shadow_x: float = 0,
        shadow_y: float = 2,
        rows: Optional[int] = None,
        equal: bool = False,
        fill: bool = False,
    ) -> _ContainerContext: ...

    # -- Output --

    def validate(self, family: Optional[str] = None) -> Dict[str, Any]: ...

    def timeline(
        self,
        entries: Optional[List[Dict[str, Any]]] = None,
        *,
        update: str = "after",
        after: Any = None,
        interval: Optional[float] = None,
    ) -> "Widget": ...

    def render(self, url: Optional[str] = None) -> None: ...


__all__ = [
    "SMALL", "MEDIUM", "LARGE", "CIRCULAR", "RECTANGULAR", "INLINE",
    "Widget", "save_image",
    "preview", "family_value", "context",
    "entry", "history", "cache_json", "state", "action", "intent",
    "schema", "agent_schema", "validate_layout",
    "reload_user_widgets", "reload_test_widgets",
    "family", "param", "storage",
]
