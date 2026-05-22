"""appui — Python SwiftUI Bridge — Type Stubs for IDE autocompletion.

A declarative Python DSL that renders native SwiftUI views on iOS.
Create reactive UIs with ``State``, layout with ``VStack``/``HStack``,
navigate with ``NavigationStack``/``TabView``, and present with ``sheet``/``alert``.

Minimal example::

    import appui

    state = appui.State(count=0)

    def increment():
        state.count += 1

    def body():
        return appui.VStack([
            appui.Text(f"Count: {state.count}").font("title").bold(),
            appui.Button("+1", action=increment),
        ], spacing=16).padding()

    appui.run(body, state=state)
"""

import ctypes
import sys
from typing import (
    Any,
    Callable,
    Dict,
    Iterable,
    List,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Union,
    overload,
)

if sys.version_info >= (3, 11):
    from typing import Self
else:
    from typing_extensions import Self

# ── Type Aliases ──

ColorLike = Union[str, Tuple[float, ...], int, float]
"""Color specification: named string (``'systemBlue'``), hex (``'#FF0000'``),
RGB tuple (``(1.0, 0.0, 0.0)``), RGBA tuple, or gray float (``0.5``)."""

ViewChild = Union["View", List["View"]]
"""A single View or a list of Views accepted as children."""

infinity: float
"""Positive infinity constant — use with ``max_width`` / ``max_height`` in ``.frame()``."""

# ═══════════════════════════════════════════════════════════
#  State Management
# ═══════════════════════════════════════════════════════════

class ObservableList(list):
    """A ``list`` subclass that triggers UI rebuilds on mutation.

    Created automatically when you assign a ``list`` to a ``State`` field.
    You normally do not instantiate this directly.
    """
    def __init__(self, data: Iterable[Any], notify: Callable[[], None]) -> None: ...
    def append(self, v: Any) -> None: ...
    def insert(self, i: int, v: Any) -> None: ...
    def extend(self, iterable: Iterable[Any]) -> None: ...
    def remove(self, v: Any) -> None: ...
    def pop(self, i: int = -1) -> Any: ...
    def clear(self) -> None: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def __iadd__(self, other: Iterable[Any]) -> Self: ...
    def sort(self, **kwargs: Any) -> None: ...
    def reverse(self) -> None: ...


class ObservableDict(dict):
    """A ``dict`` subclass that triggers UI rebuilds on mutation.

    Created automatically when you assign a ``dict`` to a ``State`` field.
    """
    def __init__(self, data: Mapping[Any, Any], notify: Callable[[], None]) -> None: ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def pop(self, key: Any, *args: Any) -> Any: ...
    def update(self, *args: Any, **kwargs: Any) -> None: ...
    def clear(self) -> None: ...
    def setdefault(self, key: Any, default: Any = None) -> Any: ...
    def items(self) -> List[Tuple[Any, Any]]: ...
    def keys(self) -> List[Any]: ...
    def values(self) -> List[Any]: ...
    def copy(self) -> Dict[Any, Any]: ...


class State:
    """Reactive state container — attribute changes automatically trigger UI refresh.

    Supports deep observation for nested ``list`` and ``dict`` values. Inside
    MiniApps, JSON-compatible fields are restored and saved automatically unless
    marked as ``transient``.

    Example::

        state = appui.State(count=0, name='', items=[])
        state.count += 1          # triggers rebuild
        state.items.append('x')   # triggers rebuild (deep observation)
        state.batch_update(count=5, name='Bob')  # single rebuild
    """
    def __init__(self, persist: Optional[Union[bool, Sequence[str]]] = None,
                 persist_key: Optional[str] = None,
                 transient: Optional[Sequence[str]] = None,
                 debounce: float = 0.3,
                 **kwargs: Any) -> None: ...
    def __getattr__(self, key: str) -> Any: ...
    def __setattr__(self, key: str, value: Any) -> None: ...
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def batch_update(self, **kwargs: Any) -> None:
        """Update multiple values in one pass, triggering only one rebuild."""
        ...
    def to_dict(self) -> Dict[str, Any]:
        """Export all fields as a plain dictionary."""
        ...
    def get(self, key: str, default: Any = None) -> Any:
        """Safe access that never raises — useful after hot-reload."""
        ...
    def flush_persisted(self) -> bool:
        """Synchronously save pending persistent state."""
        ...
    def clear_persisted(self) -> bool:
        """Remove this state's saved snapshot."""
        ...


class PersistentState(State):
    """Explicit persistent AppUI state."""
    def __init__(self, persist_key: Optional[str] = None,
                 transient: Optional[Sequence[str]] = None,
                 debounce: float = 0.3,
                 **kwargs: Any) -> None: ...


class ReactiveState:
    """State with automatic binary/JSON channel routing per field.

    Fields declared as ``(initial_value, prop_id)`` tuples are routed
    through the Aurora binary fast-path when a handle is bound.
    Plain values use the normal JSON rebuild path.

    Example::

        state = appui.ReactiveState(
            count=0,                           # JSON path
            slider_val=(0.5, 1),               # binary path (prop_id=1)
        )
        state.slider_val = 0.75   # binary push — no rebuild
        state.count = 42          # JSON rebuild
    """
    def __init__(self, **kwargs: Any) -> None: ...
    def __getattr__(self, key: str) -> Any: ...
    def __setattr__(self, key: str, value: Any) -> None: ...
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def get(self, key: str, default: Any = None) -> Any:
        """Safe access that never raises."""
        ...
    def to_dict(self) -> Dict[str, Any]:
        """Export all fields as a plain dictionary."""
        ...
    def batch_update(self, **kwargs: Any) -> None:
        """Update multiple values, triggering only one rebuild."""
        ...
    def bind(self, field_name: str) -> Dict[str, Any]:
        """Create a two-way binding dict (``value`` + ``on_change``)."""
        ...
    def bind_handles(self, **bindings: int) -> None:
        """Bind Aurora handles to fields for binary fast-path."""
        ...
    def _accept_callback(self, key: str, value: Any) -> None: ...


class Prop:
    """Descriptor for reactive properties on View subclasses.

    When the Aurora binary channel is active, writes are pushed
    without a full JSON rebuild.

    Example on a custom view class::

        class MyView(appui.View):
            title = appui.Prop(prop_id=1, default='Hello')
    """
    prop_id: int
    val_type: str
    default: Any
    def __init__(self, prop_id: int, val_type: str = 'auto', default: Any = None, attr: Optional[str] = None) -> None: ...
    def __set_name__(self, owner: Any, name: str) -> None: ...
    def __get__(self, obj: Any, objtype: Any = None) -> Any: ...
    def __set__(self, obj: Any, value: Any) -> None: ...


class Ref:
    """A mutable reference that does NOT trigger rebuilds.

    Useful for storing counters, handles, or any data that
    should not cause the UI to refresh when changed.

    Example::

        counter = appui.Ref(0)
        counter.current += 1  # no UI refresh
    """
    current: Any
    def __init__(self, initial: Any = None) -> None: ...


def computed(state: Union[State, ReactiveState], depends_on: List[str]) -> Callable:
    """Decorator: cached derived value, recomputed only when deps change.

    Example::

        @appui.computed(state, depends_on=['items', 'filter_text'])
        def filtered():
            return [i for i in state.items if state.filter_text in str(i)]

        # In body():  filtered()  -> returns cached list
    """
    ...

def effect(state: Union[State, ReactiveState], depends_on: List[str]) -> Callable:
    """Decorator: run a side-effect when deps change (after each rebuild).

    The decorated function may return a cleanup callable::

        @appui.effect(state, depends_on=['tab'])
        def on_tab_change():
            print(f'Switched to tab {state.tab}')
            def cleanup():
                print('cleanup')
            return cleanup
    """
    ...

def bind(state: Union[State, ReactiveState], field_name: str) -> Dict[str, Any]:
    """Create a two-way binding dict for interactive components.

    Returns ``{'value': ..., 'on_change': ...}`` suitable for unpacking::

        appui.Slider(**appui.bind(state, 'volume'))
    """
    ...

def dynamic(func: Callable[[], Any], value_type: str = 'auto') -> Any:
    """Create a dependency-tracked dynamic AppUI slot value.

    Use for values that should be eligible for Aurora/C slot updates without
    rebuilding the full tree, for example ``Text(lambda: state.status)`` or
    ``.opacity(appui.dynamic(lambda: state.opacity, 'double'))``.
    """
    ...


# ═══════════════════════════════════════════════════════════
#  Navigation
# ═══════════════════════════════════════════════════════════

class NavigationPath:
    """Programmatic navigation stack — push/pop views by code.

    Example::

        path = appui.NavigationPath()
        path.append(detail_view())
        path.pop()
        path.pop_to_root()
    """
    @property
    def count(self) -> int: ...
    @property
    def is_empty(self) -> bool: ...
    def __init__(self) -> None: ...
    def append(self, view_or_value: Union["View", str, int, Dict[str, Any]]) -> None:
        """Push a view or tagged value onto the navigation stack."""
        ...
    def pop(self, count: int = 1) -> None:
        """Pop *count* items from the navigation stack."""
        ...
    def pop_to_root(self) -> None:
        """Pop all items, returning to the root view."""
        ...
    def replace(self, items: List[Any]) -> None:
        """Replace the entire navigation stack."""
        ...


# ═══════════════════════════════════════════════════════════
#  Timer
# ═══════════════════════════════════════════════════════════

class Timer:
    """Background timer that calls an action at regular intervals.

    Example::

        timer = appui.Timer(interval=1.0, action=tick)
        timer.start()
        # later...
        timer.stop()
    """
    @property
    def is_running(self) -> bool: ...
    def __init__(self, interval: float = 1.0, repeats: bool = True,
                 action: Optional[Callable[[], None]] = None) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...


# ═══════════════════════════════════════════════════════════
#  View Base — all modifiers
# ═══════════════════════════════════════════════════════════

class View:
    """Base class for all appui views.

    Container views support context-manager syntax::

        with appui.VStack(spacing=12) as stack:
            appui.Text("Hello")
            appui.Button("Tap", action=tap)
        # stack now contains both children
    """

    def __init__(self) -> None: ...

    # ── Identity ──

    def id(self, key: str) -> Self:
        """Assign a stable identity key for diffing and scroll targets."""
        ...

    # ── Layout ──

    def padding(self, value: Optional[float] = None, edges: Optional[str] = None, *,
                horizontal: Optional[float] = None, vertical: Optional[float] = None,
                top: Optional[float] = None, bottom: Optional[float] = None,
                leading: Optional[float] = None, trailing: Optional[float] = None,
                **kwargs: Any) -> Self:
        """Add padding around the view.

        Args:
            value: Uniform padding on all edges.
            edges: Edge set — ``'all'``, ``'horizontal'``, ``'vertical'``,
                   ``'top'``, ``'bottom'``, ``'leading'``, ``'trailing'``.
            horizontal/vertical/top/bottom/leading/trailing: Per-edge overrides.
        """
        ...

    def frame(self, width: Optional[float] = None, height: Optional[float] = None,
              min_width: Optional[float] = None, max_width: Optional[Union[float, str]] = None,
              min_height: Optional[float] = None, max_height: Optional[Union[float, str]] = None,
              alignment: Optional[str] = None, **kwargs: Any) -> Self:
        """Constrain the view's size. Use ``appui.infinity`` for unbounded max.

        Args:
            alignment: ``'center'``, ``'leading'``, ``'trailing'``, ``'top'``,
                       ``'bottom'``, ``'topLeading'``, ``'bottomTrailing'``, etc.
        """
        ...

    def aspect_ratio(self, ratio: Optional[float] = None, content_mode: str = 'fit',
                     **kwargs: Any) -> Self:
        """Set aspect ratio. ``content_mode``: ``'fit'`` or ``'fill'``. Works on any view."""
        ...

    def offset(self, x: float = 0, y: float = 0) -> Self:
        """Shift the view by (x, y) points without affecting layout."""
        ...

    def position(self, x: float = 0, y: float = 0) -> Self:
        """Position the view's center at (x, y) within its parent."""
        ...

    def ignore_safe_area(self, edges: str = 'all', regions: str = 'all') -> Self:
        """Extend the view into safe-area insets."""
        ...

    def fixed_size(self, horizontal: bool = True, vertical: bool = True) -> Self:
        """Prevent the view from being compressed below its ideal size."""
        ...

    def layout_priority(self, value: float) -> Self:
        """Set layout priority relative to siblings. Higher = more space."""
        ...

    def alignment_guide(self, alignment: str = 'center', compute_value: Optional[float] = None) -> Self:
        """Provide a custom alignment guide offset.

        Args:
            alignment: ``'leading'``, ``'trailing'``, ``'center'``, ``'top'``,
                       ``'bottom'``, ``'first_text_baseline'``, ``'last_text_baseline'``.
        """
        ...

    def container_relative_frame(self, axis: str = 'vertical', count: int = 1,
                                  span: int = 1, spacing: float = 8) -> Self:
        """Size relative to nearest scroll container (iOS 17+)."""
        ...

    def safe_area_inset(self, edge: str = 'bottom', content: Optional["View"] = None,
                        spacing: Optional[float] = None) -> Self:
        """Pin content to a safe-area edge."""
        ...

    # ── Appearance ──

    def font(self, name: Optional[str] = None, size: Optional[float] = None,
             weight: Optional[str] = None, design: Optional[str] = None) -> Self:
        """Set the font.

        Args:
            name: System style (``'title'``, ``'headline'``, ``'body'``, ``'caption'``,
                  ``'largeTitle'``, ``'footnote'``…) or custom PostScript name via
                  ``appui.custom_font()``.
            weight: ``'regular'``, ``'bold'``, ``'semibold'``, ``'light'``,
                    ``'medium'``, ``'heavy'``, ``'black'``, ``'thin'``, ``'ultraLight'``.
            design: ``'default'``, ``'rounded'``, ``'serif'``, ``'monospaced'``.
        """
        ...

    def bold(self) -> Self:
        """Apply bold weight."""
        ...

    def italic(self) -> Self:
        """Apply italic style."""
        ...

    def foreground_color(self, color: ColorLike) -> Self:
        """Set the text/icon color."""
        ...

    def foreground_style(self, style: Any) -> Self:
        """Set the foreground style (color, gradient, or material name)."""
        ...

    def background(self, color: Optional[ColorLike] = None, corner_radius: float = 0,
                   gradient: Optional[List[ColorLike]] = None,
                   gradient_type: str = 'linear',
                   material: Optional[str] = None,
                   cornerRadius: Optional[float] = None,
                   gradientType: Optional[str] = None,
                   opacity: Optional[float] = None,
                   **kwargs: Any) -> Self:
        """Set background color, gradient, or material.

        Args:
            color: Solid background color.
            corner_radius: Rounded corners for the background.
            gradient: List of colors for a gradient background.
            gradient_type: ``'linear'``, ``'radial'``, ``'angular'``.
            material: iOS material name — ``'ultraThinMaterial'``,
                      ``'thinMaterial'``, ``'regularMaterial'``,
                      ``'thickMaterial'``, ``'ultraThickMaterial'``.
            opacity: Background opacity override.
        """
        ...

    def opacity(self, value: float) -> Self:
        """Set the view's opacity (0.0–1.0)."""
        ...

    def corner_radius(self, value: float) -> Self:
        """Round all corners."""
        ...

    def clip_shape(self, shape: str) -> Self:
        """Clip to a shape — ``'circle'``, ``'capsule'``, ``'rect'``, ``'rounded_rect'``."""
        ...

    def clipped(self) -> Self:
        """Clip content to the view's bounds."""
        ...

    def shadow(self, color: Optional[ColorLike] = None, radius: float = 5,
               x: float = 0, y: float = 2) -> Self:
        """Add a drop shadow."""
        ...

    def border(self, color: ColorLike, width: float = 1) -> Self:
        """Add a border stroke."""
        ...

    def overlay(self, content: "View") -> Self:
        """Layer a view on top."""
        ...

    def tint(self, color: ColorLike) -> Self:
        """Set the accent/tint color."""
        ...

    def mask(self, content: "View") -> Self:
        """Mask the view with another view's alpha channel."""
        ...

    def drawing_group(self) -> Self:
        """Composite the view into a single GPU-backed layer."""
        ...
    def glass_effect(self, tint: Optional[ColorLike] = None, interactive: bool = False,
                     shape: str = 'capsule', corner_radius: Optional[float] = None,
                     cornerRadius: Optional[float] = None) -> Self:
        """Apply the iOS 26 Liquid Glass effect. Shape: ``'capsule'``, ``'rounded_rectangle'``, ``'circle'``."""
        ...
    def background_extension_effect(self, enabled: bool = True,
                                    is_enabled: Optional[bool] = None,
                                    isEnabled: Optional[bool] = None) -> Self:
        """Extend background material into surrounding bars/safe areas on iOS 26+."""
        ...

    # ── Navigation ──

    def navigation_title(self, title: Union[str, "View"]) -> Self:
        """Set the navigation bar title."""
        ...

    def navigation_bar_title_display_mode(self, mode: str) -> Self:
        """Title mode: ``'automatic'``, ``'inline'``, ``'large'``."""
        ...

    def navigation_bar_back_button_hidden(self, value: bool = True) -> Self:
        """Hide the back button in a NavigationStack."""
        ...

    def toolbar(self, items: Any) -> Self:
        """Add toolbar items (list of ``ToolbarItem``)."""
        ...

    def toolbar_background(self, visibility: str = 'visible', bars: str = 'navigation_bar') -> Self:
        """Control toolbar background (iOS 16+). Bars: ``'navigation_bar'``, ``'bottom_bar'``, ``'tab_bar'``."""
        ...

    def toolbar_color_scheme(self, scheme: str = 'dark', bars: str = 'navigation_bar') -> Self:
        """Set toolbar color scheme (iOS 16+)."""
        ...

    def navigation_destination(self, is_presented: bool = False, content: Optional["View"] = None,
                                on_dismiss: Optional[Callable] = None,
                                isPresented: Optional[bool] = None,
                                onDismiss: Optional[Callable] = None) -> Self:
        """Programmatic navigation destination."""
        ...
    def safe_area_bar(self, edge: str = 'bottom', content: Optional["View"] = None,
                      alignment: str = 'center', spacing: Optional[float] = None,
                      safeAreaEdge: Optional[str] = None) -> Self:
        """Attach iOS 26 safe-area bar content to ``'top'``, ``'bottom'``, ``'leading'``, or ``'trailing'``."""
        ...
    def tab_view_bottom_accessory(self, content: Optional["View"] = None,
                                  enabled: bool = True,
                                  is_enabled: Optional[bool] = None,
                                  isEnabled: Optional[bool] = None) -> Self:
        """Attach iOS 26 TabView bottom accessory content."""
        ...
    def tab_bar_minimize_behavior(self, behavior: str = 'automatic') -> Self:
        """Set iOS 26 tab bar minimize behavior: ``'automatic'``, ``'never'``, ``'on_scroll_down'``, ``'on_scroll_up'``."""
        ...
    def tab_view_search_activation(self, activation: str = 'search_tab_selection') -> Self:
        """Configure iOS 26 search-tab activation: ``'automatic'`` or ``'search_tab_selection'``."""
        ...

    # ── Styles ──

    def button_style(self, style: str) -> Self:
        """Button style: ``'automatic'``, ``'bordered'``, ``'bordered_prominent'``, ``'borderless'``, ``'plain'``."""
        ...
    def list_style(self, style: str) -> Self:
        """List style: ``'automatic'``, ``'inset'``, ``'inset_grouped'``, ``'grouped'``, ``'plain'``, ``'sidebar'``."""
        ...
    def text_field_style(self, style: str) -> Self:
        """TextField style: ``'automatic'``, ``'plain'``, ``'rounded_border'``."""
        ...
    def toggle_style(self, style: str) -> Self:
        """Toggle style: ``'automatic'``, ``'switch'``, ``'button'``."""
        ...
    def tab_view_style(self, style: str) -> Self:
        """TabView style: ``'automatic'``, ``'page'``."""
        ...
    def picker_style(self, style: str) -> Self:
        """Picker style: ``'automatic'``, ``'wheel'``, ``'segmented'``, ``'menu'``, ``'inline'``."""
        ...
    def gauge_style(self, style: str) -> Self:
        """Gauge style: ``'automatic'``, ``'linear'``, ``'circular'``,
        ``'accessory_circular'``, ``'accessory_linear'``,
        ``'linear_capacity'``, ``'accessory_circular_capacity'``,
        ``'accessory_linear_capacity'``."""
        ...
    def progress_view_style(self, style: str) -> Self:
        """ProgressView style: ``'automatic'``, ``'linear'``, ``'circular'``."""
        ...
    def date_picker_style(self, style: str) -> Self:
        """DatePicker style: ``'automatic'``, ``'compact'``, ``'wheel'``, ``'graphical'``."""
        ...

    # ── Interaction ──

    def on_tap(self, action: Callable) -> Self:
        """Called when the view is tapped."""
        ...
    def on_appear(self, action: Callable) -> Self:
        """Called when the view appears on screen."""
        ...
    def on_disappear(self, action: Callable) -> Self:
        """Called when the view disappears."""
        ...
    def on_long_press(self, action: Optional[Callable] = None, min_duration: float = 0.5,
                      minDuration: Optional[float] = None,
                      on_pressing: Optional[Callable] = None,
                      onPressing: Optional[Callable] = None) -> Self:
        """Called on long press. ``on_pressing`` fires while pressed (bool arg)."""
        ...
    def on_drag(self, on_changed: Optional[Callable] = None,
                on_ended: Optional[Callable] = None,
                onChanged: Optional[Callable] = None,
                onEnded: Optional[Callable] = None) -> Self:
        """Pan/drag gesture callbacks."""
        ...
    def on_magnification(self, on_changed: Optional[Callable] = None,
                         on_ended: Optional[Callable] = None,
                         onChanged: Optional[Callable] = None,
                         onEnded: Optional[Callable] = None) -> Self:
        """Pinch-to-zoom gesture callbacks."""
        ...
    def on_rotation(self, on_changed: Optional[Callable] = None,
                    on_ended: Optional[Callable] = None,
                    onChanged: Optional[Callable] = None,
                    onEnded: Optional[Callable] = None) -> Self:
        """Two-finger rotation gesture callbacks."""
        ...
    def on_drop(self, action: Callable) -> Self:
        """Called when content is dropped onto this view."""
        ...
    def on_geometry(self, action: Callable) -> Self:
        """Called with geometry info ``{'width': float, 'height': float}``."""
        ...
    def task(self, action: Callable) -> Self:
        """Run an async-like task when the view appears."""
        ...
    def disabled(self, value: bool = True) -> Self:
        """Disable user interaction."""
        ...
    def hidden(self) -> Self:
        """Hide the view while preserving its layout space."""
        ...
    def simultaneous_gesture(self, gesture: str = 'tap', callback: Optional[Callable] = None,
                              on_changed: Optional[Callable] = None,
                              min_duration: float = 0.5) -> Self:
        """Attach a gesture alongside the view's own. Gesture: ``'tap'``, ``'long_press'``, ``'magnification'``."""
        ...
    def high_priority_gesture(self, gesture: str = 'tap', callback: Optional[Callable] = None,
                               min_duration: float = 0.5) -> Self:
        """Attach a gesture that overrides child gestures."""
        ...

    # ── Presentation ──

    def alert(self, title: str, message: str = '', is_presented: bool = False,
              on_dismiss: Optional[Callable] = None, actions: Optional[List["View"]] = None,
              isPresented: Optional[bool] = None,
              onDismiss: Optional[Callable] = None) -> Self:
        """Present an alert dialog."""
        ...
    def sheet(self, is_presented: bool = False, content: Optional[Union["View", Callable[[], "View"]]] = None,
              on_dismiss: Optional[Callable] = None,
              detents: Optional[str] = None,
              drag_indicator: Optional[str] = None,
              interactive_dismiss_disabled: bool = False,
              isPresented: Optional[bool] = None,
              onDismiss: Optional[Callable] = None,
              dragIndicator: Optional[str] = None,
              interactiveDismissDisabled: Optional[bool] = None) -> Self:
        """Present a modal sheet.

        Args:
            detents: Sheet heights — ``'medium'``, ``'large'``, ``'medium_large'``.
            drag_indicator: ``'visible'`` or ``'hidden'``.
            interactive_dismiss_disabled: Prevent swipe-to-dismiss.
        """
        ...
    def full_screen_cover(self, is_presented: bool = False, content: Optional[Union["View", Callable[[], "View"]]] = None,
                          on_dismiss: Optional[Callable] = None,
                          isPresented: Optional[bool] = None,
                          onDismiss: Optional[Callable] = None) -> Self:
        """Present a full-screen modal."""
        ...
    def confirmation_dialog(self, title: str, is_presented: bool = False,
                            actions: Optional[List["View"]] = None, message: str = '',
                            on_dismiss: Optional[Callable] = None,
                            isPresented: Optional[bool] = None,
                            onDismiss: Optional[Callable] = None) -> Self:
        """Present a confirmation dialog with action buttons."""
        ...
    def context_menu(self, content: Optional[List["View"]] = None) -> Self:
        """Attach a context menu (long-press/right-click)."""
        ...
    def searchable(self, text: str = '', on_change: Optional[Callable] = None,
                   onChange: Optional[Callable] = None,
                   placement: str = 'automatic',
                   prompt: Optional[str] = None) -> Self:
        """Add a search bar."""
        ...
    def search_toolbar_behavior(self, behavior: str = 'minimize') -> Self:
        """Configure iOS 26 search toolbar behavior: ``'automatic'`` or ``'minimize'``."""
        ...
    def swipe_actions(self, edge: str = 'trailing', content: Optional[List["View"]] = None,
                      actions: Optional[List["View"]] = None) -> Self:
        """Attach swipe actions to a list row. Edge: ``'leading'`` or ``'trailing'``."""
        ...
    def refreshable(self, action: Optional[Callable] = None) -> Self:
        """Enable pull-to-refresh."""
        ...
    def badge(self, count: Any) -> Self:
        """Show a numeric or text badge."""
        ...
    def popover(self, is_presented: bool = False, content: Optional[Union["View", Callable[[], "View"]]] = None,
                on_dismiss: Optional[Callable] = None,
                isPresented: Optional[bool] = None,
                onDismiss: Optional[Callable] = None) -> Self:
        """Present a popover (iPad) or sheet (iPhone)."""
        ...
    def inspector(self, is_presented: bool = False, content: Optional[Union["View", Callable[[], "View"]]] = None,
                  on_dismiss: Optional[Callable] = None) -> Self:
        """Show an inspector sidebar (iOS 17+, iPad)."""
        ...

    # ── Animation & Transform ──

    def animation(self, type: str = 'default', value: Optional[Any] = None) -> Self:
        """Apply implicit animation. Types: ``'default'``, ``'linear'``, ``'easeIn'``,
        ``'easeOut'``, ``'easeInOut'``, ``'spring'``, ``'interpolatingSpring'``."""
        ...
    def transition(self, type: str = 'opacity') -> Self:
        """Apply insertion/removal transition. Types: ``'opacity'``, ``'slide'``, ``'scale'``,
        ``'move'``, ``'push'``, ``'identity'``."""
        ...
    def scale_effect(self, scale: float) -> Self:
        """Scale the view uniformly."""
        ...
    def rotation_effect(self, degrees: float) -> Self:
        """Rotate the view in 2D."""
        ...
    def rotation_3d_effect(self, degrees: float, x: float = 0, y: float = 0, z: float = 0) -> Self:
        """Rotate the view in 3D around the given axis."""
        ...
    def matched_geometry_effect(self, ns_id: Optional[str] = None, namespace: Optional[str] = None,
                                is_source: bool = True,
                                nsId: Optional[str] = None,
                                isSource: Optional[bool] = None) -> Self:
        """Shared geometry animation between views with the same ``ns_id``."""
        ...
    def glass_effect_id(self, id: Any) -> Self:
        """Assign an iOS 26 Liquid Glass matched-effect identity."""
        ...
    def glass_effect_transition(self, transition: str = 'matched_geometry') -> Self:
        """Set iOS 26 Liquid Glass transition: ``'matched_geometry'``, ``'materialize'``, or ``'identity'``."""
        ...
    def glass_effect_union(self, id: Any) -> Self:
        """Group iOS 26 Liquid Glass effects into the same union namespace."""
        ...
    def content_transition(self, type: str = 'opacity') -> Self:
        """Animate content changes. Types: ``'opacity'``, ``'interpolate'``, ``'numeric_text'``, ``'identity'``."""
        ...
    def phase_animator(self, phases: Optional[List[float]] = None,
                       effect: str = 'scale_opacity', scale_range: float = 0.1,
                       opacity_range: float = 0.2, duration: float = 0.6,
                       animation: str = 'easeInOut') -> Self:
        """Looping phase animation (iOS 17+). Default phases: ``[0, 0.5, 1, 0.5, 0]``.

        Args:
            effect: ``'scale_opacity'``, ``'scale'``, ``'opacity'``, ``'rotation'``, ``'offset_y'``.
            scale_range: Scale delta per unit phase (default 0.1).
            opacity_range: Opacity delta per unit phase (default 0.2).
            duration: Seconds per phase transition (default 0.6).
            animation: ``'easeInOut'``, ``'linear'``, ``'easeIn'``, ``'easeOut'``, ``'spring'``.
        """
        ...

    # ── Visual Effects ──

    def blur(self, radius: float) -> Self:
        """Gaussian blur."""
        ...
    def brightness(self, amount: float) -> Self:
        """Adjust brightness (-1.0 to 1.0)."""
        ...
    def contrast(self, amount: float) -> Self:
        """Adjust contrast (0.0 = gray, 1.0 = original)."""
        ...
    def saturation(self, amount: float) -> Self:
        """Adjust saturation (0.0 = desaturated, 1.0 = original)."""
        ...
    def grayscale(self, amount: float) -> Self:
        """Apply grayscale (0.0 = full color, 1.0 = full gray)."""
        ...

    # ── Focus & Keyboard ──

    def focused(self, field_id: Union[bool, str, None] = None, equals: Optional[str] = None,
                fieldId: Union[bool, str, None] = None,
                key: Optional[str] = None) -> Self:
        """Control keyboard focus (iOS 15+).

        Bool usage: ``TextField(...).focused(state.is_focused)``
        Key usage: ``TextField(...).focused(key='name', equals=state.active_field)``
        """
        ...
    def submit_label(self, label: str) -> Self:
        """Return key label: ``'done'``, ``'go'``, ``'send'``, ``'search'``, ``'next'``, ``'continue'``, ``'return'``."""
        ...
    def on_submit(self, action: Callable) -> Self:
        """Called when user presses the return key."""
        ...
    def keyboard_dismiss(self, mode: str = 'interactive') -> Self:
        """Keyboard dismissal on scroll: ``'interactive'`` or ``'immediately'``."""
        ...

    # ── List Row ──

    def list_row_background(self, color: ColorLike) -> Self:
        """Background color for a List row."""
        ...
    def list_row_separator(self, visibility: str = 'hidden') -> Self:
        """Row separator: ``'visible'``, ``'hidden'``, ``'automatic'``."""
        ...
    def list_row_insets(self, top: float = 0, leading: float = 0,
                        bottom: float = 0, trailing: float = 0) -> Self:
        """Custom insets for a List row."""
        ...

    # ── Text Styling ──

    def line_limit(self, limit: Optional[int]) -> Self:
        """Maximum number of lines (``None`` = unlimited)."""
        ...
    def multiline_text_alignment(self, alignment: str) -> Self:
        """Multiline text alignment: ``'leading'``, ``'center'``, ``'trailing'``."""
        ...
    def truncation_mode(self, mode: str) -> Self:
        """Truncation: ``'head'``, ``'middle'``, ``'tail'``."""
        ...
    def minimum_scale_factor(self, factor: float) -> Self:
        """Minimum text scale factor before truncation (0.0–1.0)."""
        ...
    def strikethrough(self, active: bool = True, color: Optional[ColorLike] = None) -> Self:
        """Apply strikethrough."""
        ...
    def underline(self, active: bool = True, color: Optional[ColorLike] = None) -> Self:
        """Apply underline."""
        ...

    # ── Accessibility ──

    def accessibility_label(self, label: str) -> Self:
        """VoiceOver label for this view."""
        ...
    def accessibility_hidden(self, value: bool = True) -> Self:
        """Hide from the accessibility tree."""
        ...

    # ── Scroll ──

    def scroll_content_background(self, visibility: str = 'hidden') -> Self:
        """List/Form background: ``'visible'`` or ``'hidden'`` (iOS 16+)."""
        ...
    def scroll_position(self, id: Optional[str] = None) -> Self:
        """Bind scroll position to an anchor ID (iOS 17+)."""
        ...
    def scroll_target_layout(self, enabled: bool = True) -> Self:
        """Mark children as scroll-snap targets (iOS 17+)."""
        ...
    def scroll_target_behavior(self, mode: str = 'view_aligned') -> Self:
        """Scroll snap behavior: ``'view_aligned'`` or ``'paging'`` (iOS 17+)."""
        ...
    def default_scroll_anchor(self, anchor: str = 'top') -> Self:
        """Set the default scroll anchor (iOS 17+). Anchor: ``'top'``, ``'center'``, ``'bottom'``, ``'leading'``, ``'trailing'``."""
        ...
    def scroll_clip_disabled(self, disabled: bool = True) -> Self:
        """Allow scroll content to extend beyond bounds (iOS 17+)."""
        ...
    def content_margins(self, edges: str = 'all', length: Optional[float] = None,
                        **kwargs: Any) -> Self:
        """Set content margins for scrollable containers (iOS 17+).

        Args:
            edges: ``'all'``, ``'horizontal'``, ``'vertical'``, ``'top'``,
                   ``'bottom'``, ``'leading'``, ``'trailing'``.
            length: Margin size in points.
        """
        ...
    def symbol_effect(self, effect: str = 'bounce', is_active: bool = True,
                      value: Optional[Any] = None) -> Self:
        """Apply a symbol animation to SF Symbols (iOS 17+).

        Args:
            effect: ``'bounce'``, ``'pulse'``, ``'variable_color'``, ``'scale'``,
                    ``'appear'``, ``'disappear'``, ``'replace'``.
            is_active: Whether the effect is active.
            value: Trigger value — effect replays when this changes.
        """
        ...
    def scroll_transition(self, axis: str = 'vertical', transition: str = 'identity') -> Self:
        """Apply a visual transition as content scrolls in/out of view (iOS 17+).

        Args:
            axis: ``'vertical'`` or ``'horizontal'``.
            transition: ``'identity'``, ``'opacity'``, ``'scale'``, ``'slide'``.
        """
        ...
    def scroll_edge_effect_style(self, style: str = 'automatic', edges: str = 'all') -> Self:
        """Set iOS 26 scroll edge effect style: ``'automatic'``, ``'hard'``, ``'soft'``, or ``'none'``."""
        ...
    def scroll_edge_effect_hidden(self, hidden: bool = True, edges: str = 'all') -> Self:
        """Hide/show iOS 26 scroll edge effects for an edge set."""
        ...

    # ── Environment & Feedback ──

    def sensory_feedback(self, style: str = 'impact', trigger: Optional[str] = None) -> Self:
        """Haptic feedback on trigger change. Style: ``'impact'``, ``'success'``, ``'warning'``, ``'error'``, ``'selection'``."""
        ...
    def preferred_color_scheme(self, scheme: str) -> Self:
        """Force color scheme: ``'light'`` or ``'dark'``."""
        ...
    def environment_value(self, key: str, value: Any) -> Self:
        """Set an environment value."""
        ...

    # ── Misc ──

    def z_index(self, value: float) -> Self:
        """Z-axis drawing order relative to siblings."""
        ...
    def content_shape(self, shape: str = 'rect') -> Self:
        """Define the hit-testing shape: ``'rect'``, ``'circle'``, ``'capsule'``."""
        ...

    # ── CamelCase Aliases ──
    # These are identical to their snake_case counterparts.

    foregroundColor = foreground_color
    foregroundStyle = foreground_style
    backgroundColor = background
    cornerRadius = corner_radius
    clipShape = clip_shape
    lineLimit = line_limit
    navigationTitle = navigation_title
    navigationBarTitleDisplayMode = navigation_bar_title_display_mode
    navigationBarBackButtonHidden = navigation_bar_back_button_hidden
    buttonStyle = button_style
    listStyle = list_style
    textFieldStyle = text_field_style
    toggleStyle = toggle_style
    tabViewStyle = tab_view_style
    pickerStyle = picker_style
    gaugeStyle = gauge_style
    progressViewStyle = progress_view_style
    datePickerStyle = date_picker_style
    onTap = on_tap
    onAppear = on_appear
    onDisappear = on_disappear
    onLongPress = on_long_press
    onDrag = on_drag
    onMagnification = on_magnification
    onRotation = on_rotation
    onDrop = on_drop
    onGeometry = on_geometry
    onSubmit = on_submit
    fullScreenCover = full_screen_cover
    confirmationDialog = confirmation_dialog
    contextMenu = context_menu
    swipeActions = swipe_actions
    submitLabel = submit_label
    keyboardDismiss = keyboard_dismiss
    ignoreSafeArea = ignore_safe_area
    fixedSize = fixed_size
    layoutPriority = layout_priority
    scaleEffect = scale_effect
    rotationEffect = rotation_effect
    rotation3dEffect = rotation_3d_effect
    matchedGeometryEffect = matched_geometry_effect
    contentTransition = content_transition
    phaseAnimator = phase_animator
    minimumScaleFactor = minimum_scale_factor
    multilineTextAlignment = multiline_text_alignment
    truncationMode = truncation_mode
    accessibilityLabel = accessibility_label
    accessibilityHidden = accessibility_hidden
    listRowBackground = list_row_background
    listRowSeparator = list_row_separator
    listRowInsets = list_row_insets
    scrollContentBackground = scroll_content_background
    scrollPosition = scroll_position
    scrollTargetLayout = scroll_target_layout
    scrollTargetBehavior = scroll_target_behavior
    defaultScrollAnchor = default_scroll_anchor
    scrollClipDisabled = scroll_clip_disabled
    contentMargins = content_margins
    symbolEffect = symbol_effect
    scrollTransition = scroll_transition
    containerRelativeFrame = container_relative_frame
    simultaneousGesture = simultaneous_gesture
    highPriorityGesture = high_priority_gesture
    sensoryFeedback = sensory_feedback
    preferredColorScheme = preferred_color_scheme
    environmentValue = environment_value
    contentShape = content_shape
    safeAreaInset = safe_area_inset
    toolbarBackground = toolbar_background
    toolbarColorScheme = toolbar_color_scheme
    navigationDestination = navigation_destination
    safeAreaBar = safe_area_bar
    tabViewBottomAccessory = tab_view_bottom_accessory
    tabBarMinimizeBehavior = tab_bar_minimize_behavior
    tabViewSearchActivation = tab_view_search_activation
    searchToolbarBehavior = search_toolbar_behavior
    zIndex = z_index
    drawingGroup = drawing_group
    glassEffect = glass_effect
    backgroundExtensionEffect = background_extension_effect
    glassEffectID = glass_effect_id
    glassEffectTransition = glass_effect_transition
    glassEffectUnion = glass_effect_union
    scrollEdgeEffectStyle = scroll_edge_effect_style
    scrollEdgeEffectHidden = scroll_edge_effect_hidden


# ═══════════════════════════════════════════════════════════
#  Text & Labels
# ═══════════════════════════════════════════════════════════

class Text(View):
    """Display static or dynamic text.

    Example::

        appui.Text("Hello World").font("title").bold().foreground_color("systemBlue")
    """
    content: str
    def __init__(self, content: str = '') -> None: ...
    def aurora_set_content(self, content: str) -> None:
        """Update text content via Aurora binary fast-path."""
        ...

class Label(View):
    """Title + icon combination (SF Symbol or custom image).

    Example::

        appui.Label("Settings", system_image="gear")
    """
    title: str
    def __init__(self, title: str = '', system_image: Optional[str] = None,
                 image: Optional[str] = None, systemImage: Optional[str] = None) -> None: ...
    def aurora_set_title(self, title: str) -> None:
        """Update label title text via Aurora binary fast-path."""
        ...

class AttributedText(View):
    """Rich text with per-span styling.

    Example::

        appui.AttributedText(spans=[
            {"text": "Bold ", "bold": True},
            {"text": "Red", "color": "systemRed"},
        ])
    """
    def __init__(self, spans: Optional[List[Dict[str, Any]]] = None) -> None: ...


# ═══════════════════════════════════════════════════════════
#  Images
# ═══════════════════════════════════════════════════════════

class Image(View):
    """Display an SF Symbol or named image asset.

    Example::

        appui.Image(system_name="star.fill").resizable().aspect_ratio(content_mode="fit").frame(width=40, height=40)
    """
    def __init__(self, name: Optional[str] = None, system_name: Optional[str] = None,
                 systemName: Optional[str] = None) -> None: ...
    def aurora_set_system_name(self, system_name: Optional[str]) -> None:
        """Update a system-symbol image via Aurora binary fast-path."""
        ...
    def resizable(self) -> Self:
        """Make the image resizable."""
        ...
    def aspect_ratio(self, ratio: Optional[float] = None, content_mode: str = 'fit',
                     **kwargs: Any) -> Self:
        """Set aspect ratio. content_mode: ``'fit'`` or ``'fill'``."""
        ...
    def symbol_rendering_mode(self, mode: str) -> Self:
        """SF Symbol rendering: ``'hierarchical'``, ``'palette'``, ``'multicolor'``, ``'monochrome'``."""
        ...
    def image_scale(self, scale: str) -> Self:
        """Image scale: ``'small'``, ``'medium'``, ``'large'``."""
        ...
    # CamelCase aliases
    aspectRatio = aspect_ratio
    imageScale = image_scale
    symbolRenderingMode = symbol_rendering_mode

class AsyncImage(View):
    """Load an image from a URL asynchronously.

    Example::

        appui.AsyncImage(url="https://example.com/photo.jpg")
            .aspect_ratio(5 / 7, content_mode="fill")
    """
    def __init__(self, url: str = '', placeholder: Optional[View] = None,
                 error_view: Optional[View] = None, content_mode: str = 'fit',
                 on_success: Optional[Callable] = None,
                 on_failure: Optional[Callable] = None) -> None: ...


# ═══════════════════════════════════════════════════════════
#  Input Controls
# ═══════════════════════════════════════════════════════════

class Button(View):
    """A standard button.

    Example::

        appui.Button("Save", action=save_data, role="destructive")
        appui.Button(appui.Image(system_name="trash"), action=delete_item)
        appui.Button(role="close", content=appui.Label("", system_image="xmark"))
        appui.Button(action=do_thing, content=appui.Label("Go", system_image="arrow.right"))
    """
    def __init__(self, title: Optional[Union[str, View]] = None, action: Optional[Callable] = None,
                 role: Optional[str] = None, content: Optional[ViewChild] = None) -> None: ...

class CloseButton(View):
    """A semantic MiniApp close button.

    Use inside a toolbar when you want to provide your own close control. In
    ``fullscreen_with_close`` this prevents the host from injecting a duplicate
    close button for the containing NavigationStack.
    """
    def __init__(self, title: str = '', system_image: str = 'xmark',
                 systemImage: Optional[str] = None) -> None: ...

class TextField(View):
    """Single-line text input.

    Example::

        def set_name(value):
            state.name = value

        appui.TextField("Enter name", text=state.name, on_change=set_name)
    """
    text: str
    def __init__(self, placeholder: str = '', text: str = '', on_change: Optional[Callable] = None,
                 on_submit: Optional[Callable] = None, keyboard_type: Optional[str] = None,
                 autocapitalization: Optional[str] = None, autocorrection_disabled: bool = False,
                 submit_label: Optional[str] = None,
                 onChange: Optional[Callable] = None,
                 onSubmit: Optional[Callable] = None,
                 keyboardType: Optional[str] = None,
                 autoCapitalization: Optional[str] = None,
                 autocorrectionDisabled: Optional[bool] = None,
                 submitLabel: Optional[str] = None,
                 value: Optional[str] = None,
                 **kwargs: Any) -> None: ...
    def aurora_set_text(self, text: str) -> None:
        """Update text field content via Aurora binary fast-path."""
        ...

class SecureField(View):
    """Password input field."""
    def __init__(self, placeholder: str = '', text: str = '', on_change: Optional[Callable] = None,
                 on_submit: Optional[Callable] = None,
                 onChange: Optional[Callable] = None,
                 onSubmit: Optional[Callable] = None) -> None: ...

class TextEditor(View):
    """Multi-line text editing area."""
    def __init__(self, text: str = '', on_change: Optional[Callable] = None,
                 onChange: Optional[Callable] = None) -> None: ...

class TextFieldLink(View):
    """Text field that triggers a submission action."""
    def __init__(self, title: str = '', prompt: str = '', on_submit: Optional[Callable] = None,
                 onSubmit: Optional[Callable] = None) -> None: ...

class SearchField(View):
    """Standalone search field."""
    def __init__(self, text: str = '', placeholder: str = 'Search',
                 on_change: Optional[Callable] = None,
                 onChange: Optional[Callable] = None,
                 on_submit: Optional[Callable] = None,
                 onSubmit: Optional[Callable] = None) -> None: ...

class Toggle(View):
    """On/off switch.

    Example::

        def set_dark(value):
            state.dark = value

        appui.Toggle("Dark Mode", is_on=state.dark, on_change=set_dark)
    """
    is_on: bool
    def __init__(self, label: str = '', is_on: bool = False, on_change: Optional[Callable] = None,
                 isOn: Optional[bool] = None, onChange: Optional[Callable] = None,
                 value: Optional[bool] = None) -> None: ...
    def aurora_set_is_on(self, value: bool) -> None:
        """Update toggle state via Aurora binary fast-path."""
        ...

class Slider(View):
    """Continuous value slider.

    Example::

        def set_volume(value):
            state.vol = value

        appui.Slider(value=state.vol, minimum=0, maximum=100, on_change=set_volume)
    """
    value: float
    def __init__(self, value: float = 0.0, minimum: float = 0.0, maximum: float = 1.0,
                 step: Optional[float] = None, label: str = '',
                 on_change: Optional[Callable] = None,
                 onChange: Optional[Callable] = None,
                 min_value: Optional[float] = None,
                 max_value: Optional[float] = None,
                 minValue: Optional[float] = None,
                 maxValue: Optional[float] = None) -> None: ...
    def aurora_set_value(self, value: float) -> None:
        """Update slider value via Aurora binary fast-path."""
        ...

class Stepper(View):
    """Increment/decrement control."""
    value: int
    def __init__(self, label: str = '', value: int = 0, minimum: int = 0, maximum: int = 100,
                 step: int = 1, on_change: Optional[Callable] = None,
                 onChange: Optional[Callable] = None) -> None: ...
    def aurora_set_value(self, value: int) -> None:
        """Update stepper value via Aurora binary fast-path."""
        ...

class Picker(View):
    """Selection picker (dropdown/wheel/menu).

    Style controlled by ``.picker_style()``."""
    def __init__(self, label: str = '', selection: Optional[str] = None,
                 options: Optional[List[str]] = None, on_change: Optional[Callable] = None,
                 onChange: Optional[Callable] = None) -> None: ...

class SegmentedControl(View):
    """Horizontal segmented picker."""
    def __init__(self, options: Optional[List[str]] = None, selection: Optional[str] = None,
                 on_change: Optional[Callable] = None,
                 onChange: Optional[Callable] = None) -> None: ...

class InlinePickerStyle(View):
    """Inline picker displayed directly in the layout."""
    def __init__(self, options: Optional[List[str]] = None, selection: Optional[str] = None,
                 on_change: Optional[Callable] = None,
                 onChange: Optional[Callable] = None) -> None: ...

class WheelPicker(View):
    """Scrolling wheel picker."""
    def __init__(self, options: Optional[List[str]] = None, selection: Optional[str] = None,
                 on_change: Optional[Callable] = None,
                 onChange: Optional[Callable] = None) -> None: ...

class DatePicker(View):
    """Date and/or time picker.

    Args:
        components: ``'date'``, ``'hourAndMinute'``, or both joined."""
    def __init__(self, label: str = '', selection: Optional[str] = None, components: str = 'date',
                 on_change: Optional[Callable] = None,
                 onChange: Optional[Callable] = None) -> None: ...

class MultiDatePicker(View):
    """Multi-date selection (iOS 16+)."""
    def __init__(self, title: str = '', on_change: Optional[Callable] = None,
                 onChange: Optional[Callable] = None) -> None: ...

class ColorPicker(View):
    """Native color picker."""
    def __init__(self, label: str = '', selection: Optional[str] = None,
                 on_change: Optional[Callable] = None,
                 onChange: Optional[Callable] = None) -> None: ...

class Menu(View):
    """Dropdown menu.

    Example::

        appui.Menu("Actions", content=[
            appui.Button("Copy", action=copy),
            appui.Button("Delete", action=delete, role="destructive"),
        ])
    """
    def __init__(self, title: str = '', content: Optional[List[View]] = None,
                 children: Optional[List[View]] = None) -> None: ...

class PasteButton(View):
    """System paste button (iOS 16+)."""
    def __init__(self, on_paste: Optional[Callable] = None,
                 onPaste: Optional[Callable] = None) -> None: ...

class RenameButton(View):
    """System rename button."""
    def __init__(self, action: Optional[Callable] = None) -> None: ...

class EditButton(View):
    """System edit-mode toggle button."""
    pass

class SignInWithAppleButton(View):
    """Apple Sign-In button.

    Args:
        type: ``'signIn'``, ``'continue'``, ``'signUp'``."""
    def __init__(self, type: str = 'signIn', on_complete: Optional[Callable] = None,
                 onComplete: Optional[Callable] = None) -> None: ...

class PhotoPicker(View):
    """Photo library picker.

    Args:
        filter: ``'images'``, ``'videos'``, or ``'all'``."""
    def __init__(self, selection_limit: int = 1, filter: str = 'images',
                 on_picked: Optional[Callable] = None, label: Optional[View] = None,
                 selectionLimit: Optional[int] = None,
                 onPicked: Optional[Callable] = None,
                 **kwargs: Any) -> None: ...

class CameraPicker(View):
    """Camera capture view.

    Args:
        source: ``'camera'`` or ``'front'``.
        media_type: ``'photo'`` or ``'video'``."""
    def __init__(self, source: str = 'camera', media_type: str = 'photo',
                 on_captured: Optional[Callable] = None, label: Optional[View] = None,
                 mediaType: Optional[str] = None,
                 onCaptured: Optional[Callable] = None,
                 **kwargs: Any) -> None: ...


class FileImporter(View):
    """System document picker for importing files.

    Args:
        allowed_types: type names, filename extensions, or MIME types.
        allows_multiple: allow selecting more than one file.
        copy: copy selected files into the app sandbox before returning paths.
        on_picked: callback receiving a list of file-path strings."""
    def __init__(self,
                 allowed_types: Optional[Union[str, Sequence[str]]] = None,
                 allows_multiple: bool = False,
                 copy: bool = True,
                 on_picked: Optional[Callable] = None,
                 label: Optional[View] = None,
                 allowedTypes: Optional[Union[str, Sequence[str]]] = None,
                 allowsMultiple: Optional[bool] = None,
                 onPicked: Optional[Callable] = None,
                 **kwargs: Any) -> None: ...


# ═══════════════════════════════════════════════════════════
#  Layout Containers
# ═══════════════════════════════════════════════════════════

class _ContainerView(View):
    """Base for container views that support ``with`` context-manager syntax."""
    def __enter__(self) -> Self: ...
    def __exit__(self, *exc: Any) -> bool: ...

class VStack(_ContainerView):
    """Vertical stack layout.

    Example::

        appui.VStack([appui.Text("A"), appui.Text("B")], spacing=8, alignment="leading")
    """
    def __init__(self, content: Optional[List[View]] = None, alignment: str = 'center',
                 spacing: Optional[float] = None) -> None: ...

class HStack(_ContainerView):
    """Horizontal stack layout."""
    def __init__(self, content: Optional[List[View]] = None, alignment: str = 'center',
                 spacing: Optional[float] = None) -> None: ...

class ZStack(_ContainerView):
    """Overlay stack — children layered on top of each other."""
    def __init__(self, content: Optional[List[View]] = None, alignment: str = 'center') -> None: ...

class LazyVStack(View):
    """Lazy vertical stack — renders children on demand."""
    def __init__(self, content: Optional[List[View]] = None, alignment: str = 'center',
                 spacing: Optional[float] = None) -> None: ...

class LazyHStack(View):
    """Lazy horizontal stack."""
    def __init__(self, content: Optional[List[View]] = None, alignment: str = 'center',
                 spacing: Optional[float] = None) -> None: ...

class ScrollView(_ContainerView):
    """Scrollable container.

    Args:
        axes: ``'vertical'``, ``'horizontal'``, ``'both'``."""
    def __init__(self, content: Optional[ViewChild] = None, axes: str = 'vertical',
                 shows_indicators: bool = True,
                 showsIndicators: Optional[bool] = None) -> None: ...

class ScrollViewReader(View):
    """ScrollView with programmatic scroll-to support.

    Example::

        appui.ScrollViewReader([...], scroll_to="item_5", anchor="center")
    """
    def __init__(self, content: Optional[ViewChild] = None, axes: str = 'vertical',
                 shows_indicators: bool = True, scroll_to: Optional[str] = None,
                 anchor: str = 'top', showsIndicators: Optional[bool] = None,
                 scrollTo: Optional[str] = None,
                 children: Optional[ViewChild] = None) -> None: ...

class Spacer(View):
    """Flexible space that expands to fill available room."""
    def __init__(self, min_length: Optional[float] = None,
                 minLength: Optional[float] = None) -> None: ...

class Divider(View):
    """Thin horizontal line separator."""
    pass

class LazyVGrid(View):
    """Lazy vertical grid.

    Example::

        appui.LazyVGrid(columns=[appui.flexible(), appui.flexible()], content=[...])
    """
    def __init__(self, columns: Optional[List[dict]] = None, content: Optional[List[View]] = None,
                 spacing: Optional[float] = None, children: Optional[List[View]] = None) -> None: ...

class LazyHGrid(View):
    """Lazy horizontal grid."""
    def __init__(self, rows: Optional[List[dict]] = None, content: Optional[List[View]] = None,
                 spacing: Optional[float] = None, children: Optional[List[View]] = None) -> None: ...

class Grid(View):
    """Precise grid layout (like HTML ``<table>``). Use with ``GridRow``."""
    def __init__(self, content: Optional[List[View]] = None, alignment: str = 'center',
                 horizontal_spacing: Optional[float] = None,
                 vertical_spacing: Optional[float] = None,
                 horizontalSpacing: Optional[float] = None,
                 verticalSpacing: Optional[float] = None) -> None: ...

class GridRow(View):
    """A single row inside a ``Grid``."""
    def __init__(self, content: Optional[List[View]] = None,
                 alignment: Optional[str] = None) -> None: ...

class GeometryReader(View):
    """Read the parent's size and position.

    The ``on_change`` callback receives ``{'width': float, 'height': float}``."""
    def __init__(self, content: Optional[ViewChild] = None, on_change: Optional[Callable] = None,
                 onChange: Optional[Callable] = None,
                 children: Optional[ViewChild] = None,
                 on_geometry: Optional[Callable] = None,
                 onGeometry: Optional[Callable] = None) -> None: ...

class ViewThatFits(View):
    """Picks the first child that fits the available space."""
    def __init__(self, content: Optional[List[View]] = None) -> None: ...

class Group(View):
    """Logical grouping — does not add any visual element or layout."""
    def __init__(self, content: Optional[List[View]] = None) -> None: ...

class Overlay(View):
    """Layer an overlay view on top of content."""
    def __init__(self, content: Optional[View] = None, overlay: Optional[View] = None,
                 alignment: str = 'center') -> None: ...

class SafeAreaInset(View):
    """Pin content to a safe-area edge."""
    def __init__(self, edge: str = 'bottom', content: Optional[View] = None) -> None: ...


# ═══════════════════════════════════════════════════════════
#  Navigation
# ═══════════════════════════════════════════════════════════

class NavigationStack(View):
    """Container for push-based navigation.

    Example::

        appui.NavigationStack(
            appui.List([
                appui.NavigationLink("Detail", destination=detail_view())
            ]).navigation_title("Home")
        )
    """
    def __init__(self, content: Optional[View] = None, path: Optional[NavigationPath] = None,
                 destinations: Optional[Dict[str, Callable]] = None) -> None: ...

NavigationView = NavigationStack
"""Alias: ``NavigationView`` is the same as ``NavigationStack``."""

class NavigationLink(View):
    """Push a destination view onto the navigation stack."""
    def __init__(self, title: Optional[str] = None, destination: Optional[View] = None,
                 label: Optional[View] = None) -> None: ...

class NavigationSplitView(View):
    """Two- or three-column layout (iPad).

    Args:
        column_visibility: ``'all'``, ``'double'``, ``'detail'``."""
    def __init__(self, sidebar: Optional[View] = None, detail: Optional[View] = None,
                 supplementary: Optional[View] = None, column_visibility: str = 'all') -> None: ...

class TabView(View):
    """Tab-based navigation.

    Example::

        appui.TabView(tabs=[
            appui.Tab("Home", system_image="house", content=home_view()),
            appui.Tab("Settings", system_image="gear", content=settings_view()),
        ])
    """
    def __init__(self, tabs: Optional[List["Tab"]] = None, selection: Optional[int] = None,
                 on_change: Optional[Callable] = None,
                 onChange: Optional[Callable] = None) -> None: ...

class Tab(View):
    """A single tab for ``TabView``.

    ``role`` supports ``'search'`` on iOS 18+ for the trailing search tab affordance.
    """
    def __init__(self, title: str = '', system_image: Optional[str] = None,
                 image: Optional[str] = None, content: Optional[View] = None,
                 badge: Optional[int] = None, tag: Optional[int] = None,
                 systemImage: Optional[str] = None, role: Optional[str] = None) -> None: ...
    def badge(self, count: Any) -> Self:
        """Show a badge on this tab."""
        ...


# ═══════════════════════════════════════════════════════════
#  Data Display
# ═══════════════════════════════════════════════════════════

class List(_ContainerView):
    """Scrollable list of rows. Style with ``.list_style()``."""
    def __init__(self, content: Optional[List[View]] = None) -> None: ...

class ForEach(View):
    """Dynamic list of views from data.

    Example::

        def row_view(item):
            return appui.Text(item.name)

        def item_key(item):
            return item.id

        appui.ForEach(items, row_builder=row_view, key=item_key)
    """
    def __init__(self, data: Any, row_builder: Optional[Callable] = None,
                 key: Optional[Callable] = None,
                 rowBuilder: Optional[Callable] = None,
                 content: Optional[Callable] = None) -> None: ...

class Form(_ContainerView):
    """Grouped settings form. Use with ``Section``."""
    def __init__(self, content: Optional[List[View]] = None) -> None: ...

class Section(_ContainerView):
    """Section inside a ``List`` or ``Form`` with optional header/footer."""
    @overload
    def __init__(self, header: Union[str, View], content: Optional[ViewChild] = None,
                 footer: Optional[Union[str, View]] = None) -> None: ...
    @overload
    def __init__(self, content: Optional[ViewChild] = None, *, header: Optional[Union[str, View]] = None,
                 footer: Optional[Union[str, View]] = None, children: Optional[ViewChild] = None) -> None: ...

class GroupBox(View):
    """Titled content group box."""
    def __init__(self, label: Optional[str] = None, content: Optional[ViewChild] = None,
                 children: Optional[List[View]] = None) -> None: ...

class DisclosureGroup(View):
    """Expandable/collapsible content group."""
    def __init__(self, label: str = '', is_expanded: Optional[bool] = None,
                 content: Optional[ViewChild] = None,
                 isExpanded: Optional[bool] = None,
                 children: Optional[ViewChild] = None) -> None: ...

class LabeledContent(View):
    """Label-value pair for settings rows."""
    def __init__(self, label: str = '', value: Optional[str] = None,
                 content: Optional[View] = None) -> None: ...

class Table(View):
    """Multi-column table (iPad, iOS 17.4+). Falls back to ``List`` on iPhone."""
    def __init__(self, data: Optional[List[Dict[str, Any]]] = None,
                 columns: Optional[List[Dict[str, str]]] = None,
                 on_select: Optional[Callable] = None,
                 onSelect: Optional[Callable] = None) -> None: ...

class ControlGroup(View):
    """Group related controls together."""
    def __init__(self, label: str = '', content: Optional[List[View]] = None,
                 children: Optional[List[View]] = None) -> None: ...

class ContentUnavailableView(View):
    """Empty state placeholder view."""
    def __init__(self, title: str = '', system_image: Optional[str] = None,
                 description: Optional[str] = None,
                 systemImage: Optional[str] = None) -> None: ...

class ProgressView(View):
    """Determinate or indeterminate progress indicator.

    Omit ``value`` for an indeterminate spinner."""
    value: Optional[float]
    def __init__(self, label: Optional[str] = None, value: Optional[float] = None,
                 total: float = 1.0) -> None: ...
    def aurora_set_value(self, value: Optional[float]) -> None:
        """Update progress value via Aurora binary fast-path."""
        ...

class Link(View):
    """Tappable hyperlink that opens a URL."""
    def __init__(self, title: str = '', url: str = '') -> None: ...

class Gauge(View):
    """Value gauge indicator."""
    def __init__(self, value: float = 0.0, min_value: float = 0.0, max_value: float = 1.0,
                 label: str = '', minValue: Optional[float] = None,
                 maxValue: Optional[float] = None) -> None: ...

class ShareLink(View):
    """Share button that presents a system share sheet."""
    def __init__(self, item: str = '', subject: Optional[str] = None,
                 message: Optional[str] = None) -> None: ...

class Badge(View):
    """Numeric or text badge overlay."""
    def __init__(self, count: Optional[int] = None, text: Optional[str] = None) -> None: ...

class TimelineView(View):
    """Periodically updating view (e.g., clocks)."""
    def __init__(self, interval: float = 1.0, content: Optional[View] = None) -> None: ...


# ═══════════════════════════════════════════════════════════
#  Presentation Views
# ═══════════════════════════════════════════════════════════

class Alert(View):
    """Alert dialog as a standalone view."""
    def __init__(self, title: str = '', message: Optional[str] = None,
                 is_presented: bool = False, actions: Optional[List[View]] = None,
                 isPresented: Optional[bool] = None) -> None: ...

class ConfirmationDialog(View):
    """Confirmation action sheet as a standalone view."""
    def __init__(self, title: str = '', message: Optional[str] = None,
                 is_presented: bool = False, actions: Optional[List[View]] = None,
                 isPresented: Optional[bool] = None) -> None: ...

class Popover(View):
    """Popover container (iPad shows popover, iPhone shows sheet)."""
    def __init__(self, is_presented: bool = False, content: Optional[View] = None,
                 trigger: Optional[View] = None,
                 isPresented: Optional[bool] = None) -> None: ...

class Refreshable(View):
    """Pull-to-refresh container."""
    def __init__(self, on_refresh: Optional[Callable] = None,
                 onRefresh: Optional[Callable] = None,
                 content: Optional[ViewChild] = None) -> None: ...

class SwipeActions(View):
    """Swipe-action container for list rows."""
    def __init__(self, content: Optional[View] = None, leading: Optional[List[View]] = None,
                 trailing: Optional[List[View]] = None) -> None: ...


# ═══════════════════════════════════════════════════════════
#  Media & Maps
# ═══════════════════════════════════════════════════════════

class MapView(View):
    """Native Apple Maps view.

    Example::

        appui.MapView(latitude=31.23, longitude=121.47, span=0.05, markers=[
            {"latitude": 31.23, "longitude": 121.47, "title": "Shanghai"},
        ])
    """
    def __init__(self, latitude: float = 37.7749, longitude: float = -122.4194,
                 span: float = 0.05, markers: Optional[List[Dict[str, Any]]] = None,
                 map_style: str = 'automatic',
                 mapStyle: Optional[str] = None) -> None: ...
    def aurora_set_center(self, latitude: float, longitude: float) -> None:
        """Update map center via Aurora binary fast-path."""
        ...
    def aurora_set_span(self, span: float) -> None:
        """Update map span via Aurora binary fast-path."""
        ...

class WebView(View):
    """Embedded web view (WKWebView). Provide ``url`` or ``html``."""
    def __init__(self, url: Optional[str] = None, html: Optional[str] = None) -> None: ...

class PlayerController:
    """Primary AppUI video controller for ``VideoPlayer(player=...)``.

    Use this in AppUI media MiniApps that need seek, progress persistence,
    playback rate, completion, error, status, or PiP callbacks. Pure playback
    scripts can use the lower-level ``avplayer`` module instead.
    """
    id: str
    url: str
    autoplay: bool
    loop: bool
    rate: float
    volume: float
    allows_pip: bool
    allows_airplay: bool
    video_gravity: str
    pause_on_disappear: bool
    current_time: float
    duration: float
    is_playing: bool
    def __init__(self, id: str = 'main', url: str = '', autoplay: bool = False,
                 loop: bool = False, rate: float = 1.0, volume: float = 1.0,
                 allows_pip: bool = True, allows_airplay: bool = True,
                 video_gravity: str = 'resizeAspect',
                 pause_on_disappear: bool = True) -> None: ...
    def load(self, url: str, autoplay: Optional[bool] = None) -> bool: ...
    def play(self, rate: Optional[float] = None) -> 'PlayerController': ...
    def pause(self) -> 'PlayerController': ...
    def stop(self) -> 'PlayerController': ...
    def seek(self, seconds: float) -> 'PlayerController': ...
    def set_rate(self, rate: float) -> 'PlayerController': ...
    def set_volume(self, volume: float) -> 'PlayerController': ...
    def on_progress(self, action: Optional[Callable[[float], Any]] = None,
                    interval: float = 1.0) -> Any: ...
    def on_finished(self, action: Optional[Callable[[], Any]] = None) -> Any: ...
    def on_error(self, action: Optional[Callable[[str], Any]] = None) -> Any: ...
    def on_status_change(self, action: Optional[Callable[[str], Any]] = None) -> Any: ...
    def on_pip_change(self, action: Optional[Callable[[bool], Any]] = None) -> Any: ...
    def cleanup(self) -> None: ...

class VideoPlayer(View):
    """Video player (AVKit).

    Example::

        appui.VideoPlayer(url="https://example.com/video.mp4", autoplay=True, loop=True)
        player = appui.PlayerController("main", url="https://example.com/video.m3u8")
        appui.VideoPlayer(player=player)
    """
    def __init__(self, url: str = '', autoplay: bool = False, loop: bool = False,
                 show_controls: bool = True, presentation: str = 'inline',
                 allows_fullscreen: bool = True, allows_pip: bool = True,
                 allows_airplay: bool = True, video_gravity: str = 'resizeAspect',
                 enters_fullscreen_when_playback_begins: bool = False,
                 exits_fullscreen_when_playback_ends: bool = True,
                 showControls: Optional[bool] = None,
                 allowsFullscreen: Optional[bool] = None,
                 allowsPiP: Optional[bool] = None,
                 allowsPictureInPicture: Optional[bool] = None,
                 allowsAirPlay: Optional[bool] = None,
                 videoGravity: Optional[str] = None,
                 entersFullscreenWhenPlaybackBegins: Optional[bool] = None,
                 exitsFullscreenWhenPlaybackEnds: Optional[bool] = None,
                 allows_picture_in_picture: Optional[bool] = None,
                 player: Optional[PlayerController] = None,
                 player_id: Optional[str] = None,
                 pause_on_disappear: Optional[bool] = None) -> None: ...


# ═══════════════════════════════════════════════════════════
#  Charts (iOS 16+)
# ═══════════════════════════════════════════════════════════

class Chart(View):
    """Swift Charts view. Types: ``'bar'``, ``'line'``, ``'area'``, ``'point'``, ``'rule'``.

    Example::

        appui.Chart(data=[{"x": "Jan", "y": 100}, {"x": "Feb", "y": 200}],
                    x="x", y="y", type="bar", color="systemBlue")
    """
    def __init__(self, data: Optional[List[Dict[str, Any]]] = None, x: str = 'x', y: str = 'y',
                 type: str = 'bar', color: Optional[ColorLike] = None,
                 series: Optional[str] = None) -> None: ...
    def aurora_set_data(self, data: List[Dict[str, Any]]) -> None:
        """Update chart data via Aurora binary fast-path (avoids full rebuild)."""
        ...


# ═══════════════════════════════════════════════════════════
#  Canvas & Drawing
# ═══════════════════════════════════════════════════════════

class DrawingContext:
    """Canvas drawing command builder — chain calls then pass to ``Canvas``.

    Example::

        ctx = appui.DrawingContext()
        ctx.fill_rect(10, 10, 100, 50, color="systemBlue")
        ctx.fill_circle(80, 80, 30, color="systemRed")
        ctx.fill_text("Hello", 10, 120, font_size=20)
        appui.Canvas(width=200, height=200, context=ctx)
    """
    commands: List[Dict[str, Any]]
    def __init__(self) -> None: ...
    def fill_rect(self, x: float, y: float, width: float, height: float,
                  color: ColorLike = 'black') -> Self: ...
    def stroke_rect(self, x: float, y: float, width: float, height: float,
                    color: ColorLike = 'black', line_width: float = 1,
                    **kwargs: Any) -> Self: ...
    def fill_circle(self, cx: float, cy: float, radius: float,
                    color: ColorLike = 'black') -> Self: ...
    def stroke_circle(self, cx: float, cy: float, radius: float,
                      color: ColorLike = 'black', line_width: float = 1,
                      **kwargs: Any) -> Self: ...
    def fill_ellipse(self, x: float, y: float, width: float, height: float,
                     color: ColorLike = 'black') -> Self: ...
    def stroke_ellipse(self, x: float, y: float, width: float, height: float,
                       color: ColorLike = 'black', line_width: float = 1,
                       **kwargs: Any) -> Self: ...
    def line(self, x1: float, y1: float, x2: float, y2: float,
             color: ColorLike = 'black', line_width: float = 1,
             **kwargs: Any) -> Self: ...
    def fill_text(self, text: str, x: float, y: float, color: ColorLike = 'black',
                  font_size: float = 16, **kwargs: Any) -> Self: ...
    def fill_path(self, points: List[Tuple[float, float]], color: ColorLike = 'black',
                  close: bool = True) -> Self: ...
    def stroke_path(self, points: List[Tuple[float, float]], color: ColorLike = 'black',
                    line_width: float = 1, close: bool = False,
                    **kwargs: Any) -> Self: ...
    def arc(self, cx: float, cy: float, radius: float, start_angle: float = 0,
            end_angle: float = 360, color: ColorLike = 'black', line_width: float = 1,
            fill: bool = False, **kwargs: Any) -> Self: ...
    def rounded_rect(self, x: float, y: float, width: float, height: float,
                     corner_radius: float = 8, color: ColorLike = 'black',
                     line_width: float = 1, fill: bool = True,
                     **kwargs: Any) -> Self: ...
    def gradient_rect(self, x: float, y: float, width: float, height: float,
                      colors: Optional[List[ColorLike]] = None,
                      vertical: bool = True) -> Self: ...

class Canvas(View):
    """2D drawing canvas. Fill with ``DrawingContext`` commands."""
    def __init__(self, width: float = 300, height: float = 300,
                 commands: Optional[List[Dict[str, Any]]] = None,
                 context: Optional[DrawingContext] = None) -> None: ...
    def aurora_set_commands(self, commands: Optional[List[Dict[str, Any]]] = None,
                            context: Optional[DrawingContext] = None) -> None:
        """Update canvas draw commands via Aurora binary fast-path."""
        ...

class Path(View):
    """Vector path view.

    Commands: ``{'move': [x, y]}``, ``{'line': [x, y]}``,
    ``{'curve': [cx1, cy1, cx2, cy2, x, y]}``,
    ``{'arc': [cx, cy, r, startDeg, endDeg]}``, ``{'close': True}``."""
    def __init__(self, commands: Optional[List[Dict[str, Any]]] = None,
                 fill: Optional[ColorLike] = None, stroke: Optional[ColorLike] = None,
                 line_width: Optional[float] = None) -> None: ...
    def aurora_set_commands(self, commands: List[Dict[str, Any]]) -> None:
        """Update path commands via Aurora binary fast-path."""
        ...


# ═══════════════════════════════════════════════════════════
#  Shapes
# ═══════════════════════════════════════════════════════════

class _Shape(View):
    """Base for shape views. Use ``.fill()`` and ``.stroke()``."""
    def fill(self, color: ColorLike) -> Self:
        """Fill the shape with a color."""
        ...
    def stroke(self, color: ColorLike, line_width: float = 1, **kwargs: Any) -> Self:
        """Stroke the shape outline."""
        ...

class Rectangle(_Shape):
    """A rectangle shape."""
    def __init__(self) -> None: ...

class RoundedRectangle(_Shape):
    """A rounded rectangle shape."""
    def __init__(self, corner_radius: float = 10,
                 cornerRadius: Optional[float] = None) -> None: ...

class Circle(_Shape):
    """A circle shape."""
    def __init__(self) -> None: ...

class Capsule(_Shape):
    """A capsule (stadium) shape."""
    def __init__(self) -> None: ...

class Ellipse(_Shape):
    """An ellipse shape."""
    def __init__(self) -> None: ...

class Color(View):
    """A solid color view or color value.

    Example::

        appui.Color("systemBlue")
        appui.Color(red=0.2, green=0.5, blue=0.8, opacity=0.9)
    """
    def __init__(self, value: Optional[ColorLike] = None, red: Optional[float] = None,
                 green: Optional[float] = None, blue: Optional[float] = None,
                 opacity: float = 1.0) -> None: ...

class ToolbarItem(View):
    """An item placed in a toolbar.

    Args:
        placement: ``'automatic'``, ``'navigation_bar_leading'``,
                   ``'navigation_bar_trailing'``, ``'bottom_bar'``,
                   ``'principal'``, ``'keyboard'``.
        role: optional semantic role. Use ``'close'`` for a custom close item;
              fullscreen_with_close will then not inject a duplicate close button
              for that NavigationStack."""
    def __init__(self, placement: str = 'automatic', content: Optional[View] = None,
                 role: Optional[str] = None) -> None: ...


class ToolbarSpacer(View):
    """An iOS 26 SwiftUI ``ToolbarSpacer`` item for separating toolbar groups."""
    def __init__(self, sizing: str = 'fixed', placement: str = 'automatic') -> None: ...


# ═══════════════════════════════════════════════════════════
#  Module-Level Functions
# ═══════════════════════════════════════════════════════════

def run(body_func: Optional[Union[Callable[[], View], Callable[[Union[State, ReactiveState, None]], View]]] = None,
        state: Optional[Union[State, ReactiveState]] = None,
        hot_reload: bool = False, presentation: str = 'sheet',
        body: Optional[Union[Callable[[], View], Callable[[Union[State, ReactiveState, None]], View]]] = None) -> None:
    """Start the UI event loop.

    Args:
        body_func: A function that returns the root ``View`` tree. It may be
            declared as ``body()`` or ``body(state)``.
        state: Optional ``State`` or ``ReactiveState`` for automatic rebuild on change.
        hot_reload: Watch the source file and auto-reload on save.
        presentation: ``'sheet'``, ``'fullscreen'``, ``'fullscreen_with_close'``.
    """
    ...

def dismiss() -> None:
    """Dismiss the current appui presentation."""
    ...

def animate(action: Callable[[], None], type: str = 'default') -> None:
    """Wrap state changes in an animation.

    Example::

        def show_view():
            state.batch_update(show=True)

        appui.animate(show_view, type="spring")

    Types: ``'default'``, ``'linear'``, ``'easeIn'``, ``'easeOut'``, ``'easeInOut'``, ``'spring'``.
    """
    ...

def auto_refresh(interval: float = 1.0) -> None:
    """Force periodic UI rebuilds for live-updating content (clocks, dashboards)."""
    ...

def preload() -> None:
    """Pre-initialize the native bridge to reduce first-run latency."""
    ...

def set_custom_prop(view_or_handle: Any, prop_name: str, value: Any) -> None:
    """Push an arbitrary property via Aurora binary UPDATE_PROPS.

    Falls back to full JSON rebuild if Aurora is inactive."""
    ...

def call_native(function_name: str, **kwargs: Any) -> None:
    """Invoke a native iOS function via the Aurora command buffer.

    Example::

        appui.call_native("haptic", style="impact")
    """
    ...

def get_native_lib() -> Optional[ctypes.CDLL]:
    """Return the ctypes handle to the Aurora native library, or ``None``.

    Useful for advanced users who need direct access to the C bridge.
    """
    ...


# ═══════════════════════════════════════════════════════════
#  Grid Helpers
# ═══════════════════════════════════════════════════════════

def grid_item(type: str = 'flexible', minimum: Optional[float] = None,
              maximum: Optional[float] = None, count: Optional[int] = None) -> Dict[str, Any]:
    """Create a grid column/row specification."""
    ...

def flexible(minimum: float = 10, maximum: Optional[float] = None) -> Dict[str, Any]:
    """Flexible grid column that grows to fill space.

    Example::

        appui.LazyVGrid(columns=[appui.flexible(), appui.flexible()])
    """
    ...

def fixed(size: float) -> Dict[str, Any]:
    """Fixed-width grid column."""
    ...

def adaptive(minimum: float = 50, maximum: Optional[float] = None) -> Dict[str, Any]:
    """Adaptive grid column that fits as many items as possible above ``minimum``."""
    ...

def custom_font(name: str, size: float = 17) -> str:
    """Reference a custom font by PostScript name.

    Example::

        appui.Text("Hello").font(appui.custom_font("Avenir-Heavy", 24))
    """
    ...
