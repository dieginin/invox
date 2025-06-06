import flet as ft

from components import Title
from controllers import Updater
from version import VERSION


def main(page: ft.Page) -> None:
    page.title = "invox"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.add(Title(f"invox version {VERSION}"))

    Updater(page)


ft.app(main)
