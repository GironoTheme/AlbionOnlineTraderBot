from Actions.back_to_auction import back_to_auction
from Check.check_in_auction import CheckInAuction
from Calculation.difference_calculation import DifferenceCalculation
from Calculation.calculation_for_trading import CalculationForTrading
from Navigation.navigation_in_auction import navigation_in_auction
from Navigation.navigation_in_product_menu import navigation_in_product_menu
from Navigation.navigation_in_inventory import navigation_in_inventory
from Parsing.parse_orders import ParseOrders
from time import sleep


class SaleOfProducts(ParseOrders, DifferenceCalculation):
    def __init__(self):
        DifferenceCalculation.__init__(self)
        ParseOrders.__init__(self)

        self.balance = 0

    def sale(self):
        back_to_auction.back_to_auction()

        self.reset_data_in_the_lists()
        self._fraud_in_completed_transactions_tab()

    def reset_data_in_the_lists(self):
        self.list_of_orders = []
        self.list_of_prices_and_difference = []

    def _fraud_in_completed_transactions_tab(self):
        sleep(0.5)
        if CheckInAuction.checking_completed_transactions_tab() is True:
            navigation_in_auction.click_of_completed_transactions_tab()
            navigation_in_auction.click_on_take_all()
            sleep(0.5)

            if CheckInAuction.checking_for_you_cant_carry_more_weight() is True:

                navigation_in_auction.click_on_ok()

                while CheckInAuction.checking_for_presence_of_button((1394, 402, 1407, 410), [256, 15, 50]) is True:

                    navigation_in_auction.take_items_from_completed_transactions()
                    CheckInAuction.checking_for_presence_of_button((1394, 402, 1407, 410), [256, 15, 50])

                    if CheckInAuction.checking_your_inventory_cannot_hold_this_many_item() is True:
                        navigation_in_auction.click_on_ok()
                        break

                navigation_in_inventory.stack_objects_in_inventory()
                navigation_in_auction.click_on_sales_tab()

                self._sales_cycle()

            else:
                navigation_in_auction.click_on_sales_tab()

                navigation_in_inventory.stack_objects_in_inventory()
                self._sales_cycle()

        else:
            navigation_in_auction.click_on_sales_tab()

            self._sales_cycle()

    def _sales_cycle(self):
        self._search_for_products_for_sale()

        while CheckInAuction.checking_permissible_weight() is False:
            self._search_for_products_for_sale()

    def _func_for_parsing_of_products(self, name, level):
        self.list_of_prices_and_difference = []

        self.body_of_parser(name, level, True, self._sale_goods)

    def _sale_goods(self, list_of_product):
        sorted_list = self.calculation([list_of_product], True)
        print(sorted_list)
        if len(sorted_list) > 0:
            try:
                amount = int(CheckInAuction.checking_count_of_product_for_sale())

            except ValueError:
                amount = 1

            price = int(sorted_list[0][2])

            tax_calculation = CalculationForTrading.checking_for_possibility_of_sale(price,
                                                                                     amount,
                                                                                     self.balance)
            price -= 1

            print(sorted_list[0])
            print(amount)
            if tax_calculation is not False:
                self.balance = self.balance - tax_calculation[1] * self._sale(price)

            elif tax_calculation is False:
                self._sale(price, True)

    def _sale(self, price, check=False):
        self._set_price_and_confirm_sale(price)
        if check is True:
            self._resale_after_waiting()
            self._scrolling_goods()
            self._resale(price)
            return 
        self._scrolling_goods()
        self._resale(price)
        return self._resale(price) + 1

    def _resale(self, price):
        count_of_tax = 0
        while CheckInAuction.checking_for_presence_of_button(color_list=[255, 15, 50]) is True:
            navigation_in_auction.click_to_buy_button()
            navigation_in_product_menu.expand_price_menu()
            self._set_price_and_confirm_sale(price)
            self._resale_after_waiting()
            self._scrolling_goods()
            count_of_tax += 1

        return count_of_tax

    def _resale_after_waiting(self):
        while CheckInAuction.check_possible_pay() is True:
            navigation_in_product_menu.resale_after_waiting()

    def _set_price_and_confirm_sale(self, price):
        navigation_in_product_menu.set_product_price(price)
        navigation_in_product_menu.confirm_buy()

    def _scrolling_goods(self):
        navigation_in_product_menu.move(886, 505)
        navigation_in_product_menu.scroll_up(12)

    def _search_for_products_for_sale(self):
        back_to_auction.back_to_auction()
        self.balance = CheckInAuction.check_balance()
        print(self.balance)

        navigation_in_auction.moving_between_resource_categories_and_levels_for_sale(self._func_for_parsing_of_products)


sale_of_products = SaleOfProducts()

