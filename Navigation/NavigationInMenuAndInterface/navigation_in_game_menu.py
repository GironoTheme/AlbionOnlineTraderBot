from vision_controll_package import Mouse
from Check.check_in_main_menu import CheckInMainMenu
from time import sleep


class NavigationInGameMenu(Mouse):
    def remove_ads(self):
        if CheckInMainMenu.check_for_ads() is True:
            self.move_and_click(1460, 175)

    def _click_to_settings(self):
        self.move_and_click(1888, 33)

    def _click_to_logout(self):
        self.move_and_click(1740, 173)

    def logout(self):
        self._click_to_settings()
        self._click_to_logout()
        sleep(15)


