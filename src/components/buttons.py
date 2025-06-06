from typing import Callable, Optional

import flet as ft


class _ElevatedButton(ft.ElevatedButton):
    def __init__(
        self,
        text: Optional[str] = None,
        icon: Optional[ft.IconValue] = None,
        autofocus: Optional[bool] = None,
        on_click: Optional[Callable] = None,
    ) -> None:
        super().__init__()
        self.text = text
        self.icon = icon
        self.autofocus = autofocus
        self.on_click = on_click
        self.height = 45
        self.width = 185

    def _set_style(self, color: str, variant: bool) -> None:
        self.style = (
            ft.ButtonStyle(
                color=f"on{color}container",
                bgcolor=f"{color}container",
                overlay_color=f"{color},.1",
            )
            if variant
            else ft.ButtonStyle(
                color=f"on{color}", bgcolor=color, overlay_color=f"{color}container,.1"
            )
        )


class PrimaryButton(_ElevatedButton):
    def __init__(
        self,
        text: Optional[str] = None,
        icon: Optional[ft.IconValue] = None,
        autofocus: Optional[bool] = None,
        on_click: Optional[Callable] = None,
        variant: bool = False,
    ) -> None:
        super().__init__(text, icon, autofocus, on_click)
        self._set_style("primary", variant)


class SecondaryButton(_ElevatedButton):
    def __init__(
        self,
        text: Optional[str] = None,
        icon: Optional[ft.IconValue] = None,
        autofocus: Optional[bool] = None,
        on_click: Optional[Callable] = None,
        variant: bool = False,
    ) -> None:
        super().__init__(text, icon, autofocus, on_click)
        self._set_style("secondary", variant)


class TertiaryButton(_ElevatedButton):
    def __init__(
        self,
        text: Optional[str] = None,
        icon: Optional[ft.IconValue] = None,
        autofocus: Optional[bool] = None,
        on_click: Optional[Callable] = None,
        variant: bool = False,
    ) -> None:
        super().__init__(text, icon, autofocus, on_click)
        self._set_style("tertiary", variant)


class CancelButton(_ElevatedButton):
    def __init__(
        self,
        text: Optional[str] = None,
        icon: Optional[ft.IconValue] = None,
        autofocus: Optional[bool] = None,
        on_click: Optional[Callable] = None,
        variant: bool = False,
    ) -> None:
        super().__init__(text, icon, autofocus, on_click)
        self._set_style("error", variant)
