import flet as ft

from controllers import Router, Updater


class Main:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.configure_page()
        self.__init_app__()

    def configure_page(self) -> None:
        self.page.title = "invox"

    def __init_app__(self) -> None:
        Router(self.page)
        Updater(self.page)


ft.app(Main)
