from vision_controll_package import mouse


class ActionsInGame:
    def open_an_auction(self):
        mouse.move_and_click(1225, 255)

    def close_auction_menu(self):
        mouse.move_and_click(1450, 90)


actions_in_game = ActionsInGame()


