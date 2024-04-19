from vision_controll_package import Mouse, Keyboard
from time import sleep


class NavigationInInventory(Mouse, Keyboard):
    def stack_objects_in_inventory(self):
        sleep(0.5)
        self.open_or_close_inventory()

        sleep(0.5)
        self.move_and_click(1720, 940)

        sleep(0.5)
        self.open_or_close_inventory()

    def open_or_close_inventory(self):
        self.press_button('i')


navigation_in_inventory = NavigationInInventory()

