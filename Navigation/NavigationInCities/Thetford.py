from vision_controll_package import Mouse, Keyboard
from Navigation.navigation_in_auction import navigation_in_auction
from time import sleep


class Thetford(Mouse, Keyboard):
    def __init__(self):
        super().__init__()
        self.x_cords_of_arrow = 960
        self.y_cords_of_arrow = 450

    def exit_market(self):
        sleep(2)
        self.move(860, 550)
        self.hold_down_right_mouse_button(1.5)


thetford = Thetford()
from vision_controll_package import Windows
windows = Windows()
def a(hwnd):
    thetford.exit_market()
windows.switch_windows(a)