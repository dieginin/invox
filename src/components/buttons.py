from typing import Callable, Optional

import flet as ft

from utils import button_style


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
        self.style = button_style("primary", variant)


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
        self.style = button_style("secondary", variant)


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
        self.style = button_style("tertiary", variant)


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
        self.style = button_style("error", variant)
