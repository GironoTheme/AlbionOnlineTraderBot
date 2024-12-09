from Check.check_in_main_menu import CheckInMainMenu
from vision_controll_package import mouse


class ActionsInGame:
    def open_an_auction(self):
        mouse.move_and_click(1225, 255)

    def close_auction_menu(self):
        mouse.move_and_click(1450, 90)

    def close_ad(self):
        if CheckInMainMenu.check_ad():
            mouse.move_and_click(1456, 172)


actions_in_game = ActionsInGame()


