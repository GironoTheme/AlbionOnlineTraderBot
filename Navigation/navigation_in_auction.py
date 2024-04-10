import time

from vision_controll_package import Mouse, Keyboard
from Jsons.get_json import get_json
from Check.check_in_auction import CheckInAuction
from Navigation.navigation_in_product_menu import navigation_in_product_menu


class NavigationInAuction(Mouse, Keyboard):
    def click_to_goods(self):
        self.move_and_click(735, 200)

    def click_to_levels(self):
        self.move_and_click(980, 200)

    def click_to_buy_button(self):
        self.move_and_click(1340, 405)

    def move_to_resources_categories(self):
        self.move(780, 880)
        self.move(920, 880)

    def moving_between_resource_categories_and_levels_for_sale(self, func):
        self.click_on_sales_tab()
        self._moving_between_resource_categories_and_levels(func, True)

    def moving_between_resource_categories_and_levels_for_purchase(self, func):
        self.click_on_purchases_tab()
        self._moving_between_resource_categories_and_levels(func)

    def _moving_between_resource_categories_and_levels(self, func, for_sale=False):
        """
        Перебор категорий ресурсов с выполнением функции
        """

        for name, cords in get_json.get_resources().items():
            self.click_to_goods()
            self.move_to_resources_categories()
            self.move_and_click(cords[0], cords[1])

            for level, c in get_json.get_levels().items():
                self.click_to_levels()
                self.move_and_click(c[0], c[1])
                time.sleep(1.2)

                if self._check_button(name) is False:
                    continue

                if for_sale is True:
                    while self._check_button(name) is True:
                        self.click_to_buy_button()
                        navigation_in_product_menu.navigation_for_parser(func, name, level)

                else:
                    self.click_to_buy_button()
                    navigation_in_product_menu.navigation_for_parser(func, name, level)

            if CheckInAuction().checking_for_presence_of_button() is False:
                continue

    def find_one_product_in_resources(self, name, level):
        self.click_on_purchases_tab()

        self.click_to_goods()
        self.move_to_resources_categories()

        category_of_goods = get_json.get_resources().get(name)
        level_of_goods = get_json.get_levels().get(level)

        self.move_and_click(category_of_goods[0], category_of_goods[1])

        self.click_to_levels()
        self.move_and_click(level_of_goods[0], level_of_goods[1])

        if self._check_button(name) is True:
            self.click_to_buy_button()

    @staticmethod
    def _check_button(name):
        if name == 'Кожа':
            return CheckInAuction().checking_for_presence_of_button((1397, 420, 1400, 425))
        else:
            return CheckInAuction().checking_for_presence_of_button()

    def click_on_sales_tab(self):
        self.move_and_click(1500, 380)

    def click_on_purchases_tab(self):
        self.move_and_click(1500, 280)

    def click_of_completed_transactions_tab(self):
        self.move_and_click(1500, 800)

    def click_on_take_all(self):
        self.move_and_click(1360, 950)

    def click_on_ok(self):
        self.move_and_click(960, 530)

    def take_items_from_completed_transactions(self):
        time.sleep(1)
        for i in range(4):
            cords = (1394, 402 + 112 * i, 1407, 410 + 112 * i)

            if CheckInAuction.checking_for_presence_of_button(cords, [256, 15, 50]) is True:
                self.move_and_click(cords[0], cords[1])

                self.move_and_click(800, 550)
                self.click_on_submit()
                self.move_and_click(800, 550)

                time.sleep(1.3)
                self.scroll_up(10)

    def click_on_submit(self):
        self.move_and_click(1100, 615)


navigation_in_auction = NavigationInAuction()

