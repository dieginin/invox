from typing import Callable, List, Optional

import flet as ft


class _AlertDialog(ft.AlertDialog):
    def __init__(
        self,
        page: ft.Page,
        title: str,
        content: ft.Control,
    ) -> None:
        super().__init__(
            modal=True,
            title=ft.Text(title),
            content=content,
        )
        self.page: ft.Page = page

    def show(self) -> None:
        self.page.open(self)

    def close(self) -> None:
        self.page.close(self)


def _show_dialog(
    page: ft.Page, title: str, content: ft.Control, actions: List[ft.Control]
) -> _AlertDialog:
    dialog = _AlertDialog(page, title, content)
    dialog.actions = actions
    dialog.show()
    return dialog


def accept_dialog(
    page: ft.Page,
    title: str,
    content: ft.Control,
    on_accept: Callable,
    accept_txt: str = "Accept",
) -> _AlertDialog:
    dialog = _show_dialog(
        page,
        title,
        content,
        [ft.TextButton(accept_txt, on_click=lambda _: (dialog.close(), on_accept()))],
    )
    return dialog


def confirmation_dialog(
    page: ft.Page,
    title: str,
    content: ft.Control,
    on_confirm: Callable,
    on_cancel: Optional[Callable] = None,
    confirm_txt: str = "Confirm",
) -> _AlertDialog:
    dialog = _show_dialog(
        page,
        title,
        content,
        [
            ft.TextButton(
                confirm_txt, on_click=lambda _: (dialog.close(), on_confirm())
            ),
            ft.TextButton(
                "Cancel",
                on_click=lambda _: (dialog.close(), on_cancel() if on_cancel else None),
            ),
        ],
    )
    return dialog


def info_dialog(
    page: ft.Page,
    title: str,
    content: ft.Control,
    on_close: Optional[Callable] = None,
) -> _AlertDialog:
    dialog = _show_dialog(
        page,
        title,
        content,
        [
            ft.TextButton(
                "Close",
                on_click=lambda _: (dialog.close(), on_close() if on_close else None),
            )
        ],
    )
    return dialog
