import time
from vision_controll_package import Mouse, Keyboard
from Jsons.get_json import get_json


class NavigationInProductMenu(Mouse, Keyboard):
    def click_to_levels(self):
        self.move_and_click(380, 365)

    def click_on_cross_in_expanded_form(self):
        self.move_and_click(930, 250)

    def expand_price_menu(self):
        self.move_and_click(1325, 275)

    def navigation_in_levels(self, func, name):
        self.expand_price_menu()
        for level, c in get_json.get_levels().items():
            self.click_to_levels()
            self.move_and_click(c[0], c[1])
            time.sleep(1.2)
            func(name, level)

        self.click_on_cross_in_expanded_form()

    def navigation_for_parser(self, func, name, level):
        self.expand_price_menu()
        func(name, level)
        self.click_on_cross_in_expanded_form()

    def moving_between_prices_within_chart(self, func):
        for i in range(24):
            self.move(1070 + i * 20, 613)
            time.sleep(0.5)
            func(i)

    def click_on_purchase_order(self):
        self.move_and_click(460, 540)

    def set_product_quantity(self, quantity):
        self.move_and_click(480, 585)
        self.type(quantity)

    def set_product_price(self, price):
        self.move_and_click(550, 660)
        self.type(price)

    def confirm_buy(self):
        self.move_and_click(850, 780)
        self.move_and_click(800, 555)


navigation_in_product_menu = NavigationInProductMenu()

