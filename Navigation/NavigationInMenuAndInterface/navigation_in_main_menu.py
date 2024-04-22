from vision_controll_package import Mouse
from time import sleep


class NavigationInMainMenu(Mouse):
    def _click_to_server_menu(self):
        self.move_and_click(1540, 35)

    def choose_a_server(self, server):
        self._click_to_server_menu()

        if server == 0:
            self.move_and_click(1540, 70)

        if server == 1:
            self.move_and_click(1540, 135)

        sleep(7)

        self._click_to_enter_world()
        sleep(10)

    def _click_to_enter_world(self):
        self.move_and_click(1200, 880)



