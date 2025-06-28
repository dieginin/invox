import calendar
from datetime import datetime
from typing import Callable, Optional

import flet as ft

from utils import button_style

from .dialogs import info_dialog

# TODO Add limits


class _YearSelector(ft.Row):
    def __init__(
        self,
        initial_year: Optional[int] = None,
        on_click: Optional[Callable] = None,
    ) -> None:
        super().__init__()
        self._initial_year = initial_year
        self.year = initial_year or datetime.today().year
        self.alignment = ft.MainAxisAlignment.CENTER

        self.year_button = ft.TextButton(
            f"{self.year}",
            style=button_style(
                "primary",
                variant=False,
                shape=ft.RoundedRectangleBorder(),
            ),
            height=45,
            width=55,
            on_click=on_click,
            disabled=True,
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
                on_click=self.prev_year,
            ),
            self.year_button,
            ft.IconButton(
                icon=ft.Icons.ARROW_FORWARD,
                style=button_style(
                    "primary",
                    variant=True,
                    shape=ft.RoundedRectangleBorder(ft.border_radius.horizontal(0, 25)),
                ),
                height=45,
                width=45,
                on_click=self.next_year,
            ),
        ]
        self.spacing = 0

    def prev_year(self, _) -> None:
        self.year -= 1
        self.update_year_display()

    def next_year(self, _) -> None:
        self.year += 1
        self.update_year_display()

    def update_year_display(self) -> None:
        self.year_button.text = f"{self.year}"
        self.year_button.style = button_style(
            "primary",
            variant=not self.year == self._initial_year,
            shape=ft.RoundedRectangleBorder(),
        )
        self.year_button.disabled = self.year == self._initial_year
        self.update()


class MonthSelector(ft.Row):
    def __init__(
        self,
        initial_date: Optional[datetime] = None,
        on_change: Optional[Callable] = None,
        month_selectable: bool = True,
    ) -> None:
        super().__init__()
        self.date = initial_date or datetime.today()
        self.on_change = on_change
        self.alignment = ft.MainAxisAlignment.CENTER

        self.month_button = ft.TextButton(
            self.date.strftime("%B %Y"),
            style=button_style(
                "primary",
                variant=True,
                shape=ft.RoundedRectangleBorder(),
            ),
            height=45,
            width=150,
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
        def select_year(_) -> None:
            self.date = self.date.replace(year_selector.year)
            e.page.close(dialog)
            self.update_month_display()

        def select_month(month: int) -> None:
            self.date = self.date.replace(year_selector.year, month)
            e.page.close(dialog)
            self.update_month_display()

        buttons = []
        for i in range(1, 13):
            month_name = datetime(2000, i, 1).strftime("%B")
            is_current = i == self.date.month

            btn = ft.TextButton(
                month_name,
                on_click=lambda _, m=i: select_month(m),
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
                    year_selector := _YearSelector(
                        self.date.year, on_click=select_year
                    ),
                    ft.Column(
                        [
                            ft.Row(
                                buttons[i : i + 3],
                                alignment=ft.MainAxisAlignment.CENTER,
                                spacing=10,
                            )
                            for i in range(0, 12, 3)
                        ]
                    ),
                ],
                spacing=20,
                tight=True,
            ),
        )

    def prev_month(self, *args) -> None:
        month = self.date.month - 1 or 12
        year = self.date.year - (1 if self.date.month == 1 else 0)
        self.date = self.date.replace(year, month, 1)
        self.update_month_display()
        self.on_change(args) if self.on_change else None

    def next_month(self, *args) -> None:
        month = self.date.month + 1 if self.date.month < 12 else 1
        year = self.date.year + (1 if self.date.month == 12 else 0)
        self.date = self.date.replace(year, month, 1)
        self.update_month_display()
        self.on_change(args) if self.on_change else None

    def update_month_display(self) -> None:
        self.month_button.text = self.date.strftime("%B %Y")
        self.update()


class DateSelector(ft.Row):
    def __init__(
        self,
        initial_date: Optional[datetime] = None,
        on_change: Optional[Callable] = None,
        visible: bool = True,
    ) -> None:
        super().__init__()
        self.date = initial_date or datetime.today()
        self.on_change = on_change
        self.alignment = ft.MainAxisAlignment.CENTER
        self.visible = visible

        self.first_date = self.date.replace(day=1)
        self.last_date = self.date.replace(
            day=calendar.monthrange(self.date.year, self.date.month)[1]
        )

        self.first_date_button = ft.TextButton(
            self.first_date.strftime("%d %B %y"),
            style=button_style(
                "primary",
                variant=True,
                shape=ft.RoundedRectangleBorder(25),
            ),
            height=45,
            width=150,
            on_click=self.open_first_date_dialog,
        )
        self.last_date_button = ft.TextButton(
            self.last_date.strftime("%d %B %y"),
            style=button_style(
                "primary",
                variant=True,
                shape=ft.RoundedRectangleBorder(25),
            ),
            height=45,
            width=150,
            on_click=self.open_last_date_dialog,
        )

        self.controls = [self.first_date_button, self.last_date_button]
        self.spacing = 10

    def open_first_date_dialog(self, e: ft.ControlEvent) -> None:
        self.open_date_dialog(
            e, "Select first date", self.first_date, self.set_first_date
        )

    def open_last_date_dialog(self, e: ft.ControlEvent) -> None:
        self.open_date_dialog(
            e,
            "Select last date",
            self.last_date,
            self.set_last_date,
            min_date=self.first_date,
        )

    def open_date_dialog(
        self,
        e: ft.ControlEvent,
        title: str,
        selected_date: datetime,
        date_callback: Callable,
        min_date: Optional[datetime] = None,
    ) -> None:
        day_grid = ft.Column(spacing=5)

        def update_days() -> None:
            last_day = calendar.monthrange(selector.date.year, selector.date.month)[1]
            last_date = selector.date.replace(day=last_day)

            buttons = []
            for d in range(1, last_date.day + 1):
                current_date = selector.date
                is_selected = (
                    d == selected_date.day
                    and selected_date.month == current_date.month
                    and selected_date.year == current_date.year
                )

                current_btn_date = datetime(selector.date.year, selector.date.month, d)
                is_disabled = (
                    min_date
                    and current_btn_date < min_date
                    and current_btn_date.date() != min_date.date()
                )

                btn = ft.TextButton(
                    str(d),
                    style=(
                        button_style("primary", variant=not is_selected)
                        if not is_disabled
                        else button_style("tertiary")
                    ),
                    width=45,
                    disabled=is_selected or is_disabled,
                    on_click=lambda _, day=d: select_date(
                        current_date.year, current_date.month, day
                    ),
                )
                buttons.append(btn)

                if len(buttons) == 8 or d == last_date.day:
                    day_grid.controls.append(
                        ft.Row(
                            buttons, alignment=ft.MainAxisAlignment.CENTER, spacing=5
                        )
                    )
                    buttons = []

        def select_date(year: int, month: int, day: int) -> None:
            date_callback(selected_date.replace(year, month, day))
            e.page.close(dialog)

        def change_month() -> None:
            self.date = selector.date
            day_grid.clean()
            update_days()
            day_grid.update()

        selector = MonthSelector(
            selected_date, month_selectable=False, on_change=lambda _: change_month()
        )
        update_days()
        dialog = info_dialog(
            e.page,
            title,
            ft.Column(
                [
                    selector,
                    day_grid,
                ],
                spacing=10,
                tight=True,
            ),
        )

    def set_first_date(self, new_date: datetime) -> None:
        self.first_date = new_date
        self.update_date_display()

    def set_last_date(self, new_date: datetime) -> None:
        self.last_date = new_date
        self.update_date_display()

    def update_date_display(self) -> None:
        if self.first_date > self.last_date:
            self.last_date = self.first_date

        self.first_date_button.text = self.first_date.strftime("%d %B %y")
        self.last_date_button.text = self.last_date.strftime("%d %B %y")
        self.update()
