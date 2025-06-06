import flet as ft

from components import (
    PrimaryButton,
    RegularText,
    SecondaryButton,
    TertiaryButton,
    Title,
)


class HomeView(ft.View):
    def __init__(self) -> None:
        super().__init__()
        self.page: ft.Page

        self.__init__config()
        self.__init_components__()

    def __init__config(self) -> None:
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def __init_components__(self) -> None:
        self.controls = [
            ft.Image(src="logo.png", width=250, height=250),
            Title("Welcome to invox!"),
            RegularText("What would you like to do today?"),
            ft.Row(
                controls=[
                    PrimaryButton(
                        "Create Invoice",
                        icon="add",
                        on_click=lambda _: self.page.go("/create"),
                    ),
                    SecondaryButton(
                        "View Invoices",
                        icon="list",
                        on_click=lambda _: self.page.go("/invoices"),
                    ),
                    TertiaryButton(
                        "Settings",
                        icon="settings",
                        on_click=lambda _: self.page.go("/settings"),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
        ]
