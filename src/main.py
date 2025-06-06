import flet as ft

from controllers import Router, Updater


class Main:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.__init_confg__()
        self.__init_ctrls__()

    def __init_confg__(self) -> None:
        self.page.title = "invox"

    def __init_ctrls__(self) -> None:
        Router(self.page)
        Updater(self.page)


ft.app(Main)
