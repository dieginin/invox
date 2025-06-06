import flet as ft

from controllers import Router, Updater


class Main:
    def __init__(self, page: ft.Page) -> None:
        self.page = page

        self.__init_confg__()
        self.__init_wndow__()
        self.__init_ctrls__()

    def __init_confg__(self) -> None:
        self.page.title = "invox"
        self.page.theme = ft.Theme(color_scheme_seed="deepPurple")

    def __init_wndow__(self) -> None:
        width, height = 800, 628
        self.page.window.width = width
        self.page.window.height = height
        self.page.window.min_width = width
        self.page.window.min_height = height
        self.page.window.center()

    def __init_ctrls__(self) -> None:
        Router(self.page)
        Updater(self.page)


ft.app(Main)
