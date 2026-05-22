"""widget — Python IDE 小组件模块 — Type stubs."""

import sys
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple, Union

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

# ── Type aliases ──

ColorLike = Union[str, Tuple[str, str]]
"""Solid color string or (light, dark) tuple for Widget DSL color parameters."""

WidgetBackground = Union[str, Tuple[str, str], Dict[str, Any]]
"""Widget root/card/button background: solid, (light, dark), ``\"system\"``, or gradient dict."""

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
    def __getattr__(self, name: str) -> Any: ...


class _Storage:
    def get(self, key: str, default: Any = None) -> Any: ...
    def set(self, key: str, value: Any) -> None: ...


params: _Params
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
    def mask(self, kind: str = "roundedRectangle", corner_radius: Optional[float] = None) -> Self: ...
    def mask_view(self, align: str = "center") -> Self: ...
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
    def place(self, x: Optional[float] = None, y: Optional[float] = None, unit: str = "relative") -> Self: ...
    def frame(self, **kwargs: Any) -> Self: ...
    def offset(self, x: float = 0, y: float = 0) -> Self: ...
    def layout_priority(self, value: float = 1) -> Self: ...
    def fixed_size(self, horizontal: bool = True, vertical: bool = True) -> Self: ...
    def hide(self, *families: str) -> Self: ...
    def show(self, *families: str) -> Self: ...


class _WidgetNodeHandle:
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
    def font_weight(self, weight: str) -> Self: ...
    def font_width(self, width: str) -> Self: ...
    def monospaced(self, enabled: bool = True) -> Self: ...
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
    def line_width(self, value: float) -> Self: ...
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
    def mask(self, kind: str = "roundedRectangle", corner_radius: Optional[float] = None) -> Self: ...
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
    def place(self, x: Optional[float] = None, y: Optional[float] = None, unit: str = "relative") -> Self: ...
    def frame(self, **kwargs: Any) -> Self: ...
    def offset(self, x: float = 0, y: float = 0) -> Self: ...
    def layout_priority(self, value: float = 1) -> Self: ...
    def fixed_size(self, horizontal: bool = True, vertical: bool = True) -> Self: ...
    def hide(self, *families: str) -> Self: ...
    def show(self, *families: str) -> Self: ...


def save_image(source: Union[str, bytes], name: str) -> str: ...


def preview(family: Optional[str] = None) -> None: ...


def reload_user_widgets() -> None: ...


def reload_test_widgets() -> None: ...


def family_value(default: Any = None, **values: Any) -> Any: ...


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


def validate_layout(layout: Union[Dict[str, Any], "Widget"], family: Optional[str] = None) -> Dict[str, Any]: ...


def show(
    title: str,
    value: str = "",
    subtitle: str = "",
    *,
    progress: Optional[float] = None,
    color: Optional[str] = None,
    icon: Optional[str] = None,
    rows: Optional[List[Dict[str, Any]]] = None,
    display_type: Optional[str] = None,
    style: Optional[str] = None,
    background: Optional[str] = None,
    text_color: Optional[str] = None,
) -> None: ...


class Widget:
    def __init__(
        self,
        background: Optional[WidgetBackground] = None,
        padding: Optional[Union[int, float]] = None,
        *,
        style: Optional[str] = None,
        layout: str = "auto",
    ) -> None: ...

    # -- Semantic primitives --

    def title(self, content: Union[str, int, float]) -> _WidgetNodeHandle: ...
    def headline(self, content: Union[str, int, float]) -> _WidgetNodeHandle: ...
    def subheadline(self, content: Union[str, int, float]) -> _WidgetNodeHandle: ...
    def caption(self, content: Union[str, int, float]) -> _WidgetNodeHandle: ...
    def body(self, content: Union[str, int, float]) -> _WidgetNodeHandle: ...
    def label(self, content: Union[str, int, float]) -> _WidgetNodeHandle: ...
    def detail(self, content: Union[str, int, float]) -> _WidgetNodeHandle: ...
    def footnote(self, content: Union[str, int, float]) -> _WidgetNodeHandle: ...
    def note(self, content: Union[str, int, float]) -> _WidgetNodeHandle: ...
    def value(
        self,
        value: Union[str, int, float],
        unit: Optional[str] = None,
        subtitle: Optional[str] = None,
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
    def symbol(self, name: str) -> _WidgetNodeHandle: ...
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
    def metric(
        self,
        label: Union[str, int, float],
        value: Union[str, int, float],
        unit: Optional[str] = None,
        icon: Optional[str] = None,
        tone: Optional[str] = None,
        style: str = "plain",
    ) -> _WidgetNodeHandle: ...
    def kpi(
        self,
        label: Union[str, int, float],
        value: Union[str, int, float],
        unit: Optional[str] = None,
        icon: Optional[str] = None,
        tone: Optional[str] = None,
        style: str = "prominent",
    ) -> _WidgetNodeHandle: ...
    def stat(
        self,
        label: Union[str, int, float],
        value: Union[str, int, float],
        unit: Optional[str] = None,
        icon: Optional[str] = None,
        tone: Optional[str] = None,
        style: str = "plain",
    ) -> _WidgetNodeHandle: ...
    def pair(
        self,
        label: Union[str, int, float],
        value: Union[str, int, float],
        unit: Optional[str] = None,
        icon: Optional[str] = None,
        tone: Optional[str] = None,
    ) -> _WidgetNodeHandle: ...
    def line(
        self,
        data: List[Union[int, float]],
        labels: Optional[List[Union[str, int, float]]] = None,
        colors: Optional[List[ColorLike]] = None,
    ) -> _WidgetNodeHandle: ...
    def trend(
        self,
        data: List[Union[int, float]],
        labels: Optional[List[Union[str, int, float]]] = None,
        colors: Optional[List[ColorLike]] = None,
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
    def progress_bar(
        self,
        value: Union[int, float],
        total: float = 1.0,
        color: Optional[ColorLike] = None,
        height: Optional[float] = None,
        track_color: Optional[ColorLike] = None,
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
    ) -> _ContainerContext: ...
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
    ) -> _WidgetNodeHandle: ...
    def path(
        self,
        points: List[PathPoint],
        stroke: Optional[ColorLike] = None,
        fill: Optional[ColorLike] = None,
        line_width: Optional[float] = None,
        closed: bool = False,
        height: Optional[float] = None,
        coordinate_space: str = "relative",
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        frame: Optional[Dict[str, Any]] = None,
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
        line_width: Optional[float] = None,
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
    def time(self, target: Optional[Union[datetime, str]] = None) -> _WidgetNodeHandle: ...
    def relative_time(self, target: Optional[Union[datetime, str]] = None) -> _WidgetNodeHandle: ...
    def timer_text(self, target: Optional[Union[datetime, str]] = None) -> _WidgetNodeHandle: ...
    def background_image(
        self,
        asset: str,
        content_mode: str = "fill",
        dim: Optional[Union[bool, float]] = None,
        scrim: Optional[Union[bool, str]] = None,
        scrim_opacity: Optional[float] = None,
        focal: str = "center",
        overlay_color: ColorLike = "#000000",
    ) -> "Widget": ...
    def background(self, value: WidgetBackground) -> "Widget": ...

    def image(
        self,
        name: str,
        width: Optional[float] = None,
        height: Optional[float] = None,
        corner_radius: Optional[float] = None,
        opacity: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        content_mode: Optional[str] = None,
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

    def button(
        self,
        title: str,
        action: Optional[str] = None,
        url: Optional[str] = None,
        color: Optional[ColorLike] = None,
        background: Optional[WidgetBackground] = None,
        size: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
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
        title: str,
        is_on: Union[bool, str] = False,
        action: Optional[str] = None,
        url: Optional[str] = None,
        color: Optional[ColorLike] = None,
        background: Optional[WidgetBackground] = None,
        size: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
    ) -> _WidgetNodeHandle: ...

    # -- Containers (context managers) --

    def hstack(
        self,
        spacing: Optional[Union[int, float]] = None,
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
        style: Optional[str] = None,
    ) -> _ContainerContext: ...

    def vstack(
        self,
        spacing: Optional[Union[int, float]] = None,
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
    ) -> _ContainerContext: ...

    def zstack(
        self,
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
    ) -> _ContainerContext: ...

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
    ) -> _ContainerContext: ...

    def card(
        self,
        background: Optional[WidgetBackground] = None,
        corner_radius: Optional[float] = None,
        padding: Optional[Union[int, float]] = None,
        spacing: Optional[Union[int, float]] = None,
        opacity: Optional[float] = None,
        align: Optional[str] = None,
        border_color: Optional[ColorLike] = None,
        border_width: Optional[float] = None,
        url: Optional[str] = None,
        shadow_color: Optional[ColorLike] = None,
        shadow_radius: Optional[float] = None,
        shadow_x: float = 0,
        shadow_y: float = 2,
    ) -> _ContainerContext: ...

    # -- Output --

    def validate(self, family: Optional[str] = None) -> Dict[str, Any]: ...

    def render(self, url: Optional[str] = None) -> None: ...


__all__ = [
    "SMALL", "MEDIUM", "LARGE", "CIRCULAR", "RECTANGULAR", "INLINE",
    "Widget", "show", "save_image", "preview", "family_value",
    "history", "cache_json", "schema", "agent_schema", "validate_layout",
    "reload_user_widgets", "reload_test_widgets",
    "family", "params", "storage",
]
