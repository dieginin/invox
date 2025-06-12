import calendar
from datetime import datetime
from typing import Callable, Optional

import flet as ft

from utils import button_style

from .dialogs import info_dialog


class MonthSelector(ft.Row):
    def __init__(
        self,
        initial_date: Optional[datetime] = None,
        on_change: Optional[Callable] = None,
        month_selectable: bool = True,
        show_year: bool = False,
    ) -> None:
        super().__init__()
        self.date = initial_date or datetime.today()
        self.on_change = on_change
        self.alignment = ft.MainAxisAlignment.CENTER

        self._show_year = show_year
        self.month_button = ft.TextButton(
            self.date.strftime("%B %Y") if show_year else self.date.strftime("%B"),
            style=button_style(
                "primary",
                variant=True,
                shape=ft.RoundedRectangleBorder(),
            ),
            height=45,
            width=150 if show_year else 95,
            disabled=not month_selectable,
            on_click=self.open_month_dialog,
        )

        self.controls = [
            ft.IconButton(
                icon=ft.Icons.ARROW_BACK,
                style=button_style(
                    "primary",
                    variant=True,
                    shape=ft.RoundedRectangleBorder(ft.border_radius.horizontal(25, 0)),
                ),
                height=45,
                width=45,
                on_click=self.prev_month,
            ),
            self.month_button,
            ft.IconButton(
                icon=ft.Icons.ARROW_FORWARD,
                style=button_style(
                    "primary",
                    variant=True,
                    shape=ft.RoundedRectangleBorder(ft.border_radius.horizontal(0, 25)),
                ),
                height=45,
                width=45,
                on_click=self.next_month,
            ),
        ]
        self.spacing = 0

    def open_month_dialog(self, e: ft.ControlEvent) -> None:
        def select_month(month: int) -> None:
            self.date = self.date.replace(month=month)
            e.page.close(dialog)
            self.update_month_display()

        buttons = []
        for i in range(1, 13):
            month_name = datetime(2000, i, 1).strftime("%B")
            is_current = i == self.date.month

            btn = ft.TextButton(
                month_name,
                on_click=(None if is_current else lambda _, m=i: select_month(m)),
                style=button_style("primary", variant=not is_current),
                width=95,
                disabled=is_current,
            )
            buttons.append(btn)

        dialog = info_dialog(
            e.page,
            "Select a month",
            ft.Column(
                [
                    ft.Row(
                        buttons[i : i + 3],
                        alignment=ft.MainAxisAlignment.CENTER,
                        spacing=10,
                    )
                    for i in range(0, 12, 3)
                ],
                spacing=10,
                tight=True,
            ),
        )

    def prev_month(self, _) -> None:
        month = self.date.month - 1 or 12
        year = self.date.year - (1 if self.date.month == 1 else 0)
        self.date = self.date.replace(year=year, month=month)
        self.update_month_display()

    def next_month(self, _) -> None:
        month = self.date.month + 1 if self.date.month < 12 else 1
        year = self.date.year + (1 if self.date.month == 12 else 0)
        self.date = self.date.replace(year=year, month=month)
        self.update_month_display()

    def update_month_display(self) -> None:
        self.month_button.text = (
            self.date.strftime("%B %Y") if self._show_year else self.date.strftime("%B")
        )
        self.update()
