import main_shared_variables

from vision_controll_package import Image
from Navigation.navigation_in_product_menu import navigation_in_product_menu
from main_shared_variables import path_to_screenshots
from PhotoPreparation.photo_preparation import photo_preparation
from collections import Counter


class ParseOrders(Image):
    def __init__(self):
        self.current_product_name = ''
        self.current_product_level = ''

        self.current_list_of_orders = []

        self.list_of_orders = []

    def body_of_parser(self, name, level, need_for_func=False, func=None):
        self.current_product_name = name
        self.current_product_level = level

        navigation_in_product_menu.moving_between_prices_within_chart(self.price_and_quantity_parsing)

        if need_for_func is True:

            func(self.filter_the_list())

        self.list_of_orders.append(self.filter_the_list())
        self.current_list_of_orders = []

    def filter_the_list(self):
        num_lengths = [len(str(num[2])) for num in self.current_list_of_orders]

        most_common_length = Counter(num_lengths).most_common(1)[0][0]

        return [[num[0], num[1], num[2], num[3]] for num in self.current_list_of_orders
                if len(str(num[2])) == most_common_length]

    def price_and_quantity_parsing(self, i):
        path_to_price = path_to_screenshots+f'price{i}.png'
        path_to_amount = path_to_screenshots+f'amount{i}.png'
        # 1070, 650
        self.take_screenshot(path_to_price, (20 * i + 1070 - 78, 561, 20 * i + 1070 - 10, 581))
        self.take_screenshot(path_to_amount, (20 * i + 1070 - 136, 583, 20 * i + 1070 - 10, 602))

        price = photo_preparation.converting_numbers_to_line_from_about_product_menu(path_to_price)
        amount = photo_preparation.converting_numbers_to_line_from_about_product_menu(path_to_amount)

        self.current_list_of_orders.append([self.current_product_name, self.current_product_level, int(price), int(amount)])


parse_orders = ParseOrders()





