from vision_controll_package import Mouse, Image
from Check.check_in_main_menu import CheckInMainMenu
from time import sleep


class BackToAuction(Mouse, Image):
    def __init__(self):
        super().__init__()
        self.in_menu = bool

    def back_to_auction(self):
        self.checking_whether_it_is_currently_in_menu()

        return self.in_menu

    def checking_whether_it_is_currently_in_menu(self):
        if CheckInMainMenu.checking_for_main_menu() is True:
            self.enter_to_game()
            self.in_menu = True

        else:
            self.in_menu = False

    def login(self):
        if (CheckInMainMenu.checking_for_ok() is True or
           CheckInMainMenu.checking_for_ok_for_failed_to_connect_to_server() is True):
            self.waiting_for_the_server_to_start()

        else:
            sleep(2)

    def waiting_for_the_server_to_start(self):
        while (CheckInMainMenu.checking_for_ok() is True or
               CheckInMainMenu.checking_for_ok_for_failed_to_connect_to_server() is True):

            self.click_to_ok()
            sleep(3)
            self.move_and_click(960, 770)
            sleep(60)

    def click_to_ok(self):
        self.move_and_click(960, 543)

    def click_to_reconnect(self):
        self.move_and_click(960, 770)
        sleep(14)

        self.waiting_for_the_server_to_start()

    def enter_world(self):
        self.move_and_click(1205, 885)
        sleep(15)

    def remove_ads(self):
        self.move_and_click(1460, 170)
        sleep(2)

    def enter_to_game(self):
        self.login()
        self.click_to_reconnect()
        self.enter_world()
        self.remove_ads()
        self.open_an_auction()

    def open_an_auction(self):
        self.move_and_click(1180, 80)
        sleep(2)


back_to_auction = BackToAuction()

