from Actions.back_to_auction import back_to_auction
from Navigation.navigation_in_auction import navigation_in_auction
from Navigation.navigation_in_product_menu import navigation_in_product_menu
from Parsing.parse_orders import ParseOrders
from Check.check_in_auction import CheckInAuction
from Calculation.difference_calculation import DifferenceCalculation
from Calculation.calculation_for_trading import CalculationForTrading


class PurchaseOfGoods(ParseOrders, DifferenceCalculation):
    def __init__(self):
        DifferenceCalculation.__init__(self)
        ParseOrders.__init__(self)
        self.list_of_purchased_items = []

    def purchase(self):
        back_to_auction.back_to_auction()

        self.reset_data_in_the_lists()
        navigation_in_auction.moving_between_resource_categories_and_levels_for_purchase(self.body_of_parser)

        shopping_list = self.calculation(self.list_of_orders)
        self._product_search(shopping_list)

        print('------------------------------------')
        print('Список купленных товаров')
        print(self.list_of_purchased_items)
        print('------------------------------------')

        return self.list_of_purchased_items

    def reset_data_in_the_lists(self):
        self.list_of_purchased_items = []
        self.list_of_orders = []
        self.list_of_prices_and_difference = []

    def _product_search(self, list_of_goods):

        balance = CheckInAuction.check_balance()
        for el in list_of_goods:
            check = CalculationForTrading.checking_for_possibility_of_purchase(el[2], balance)

            if check is not False:
                navigation_in_auction.find_one_product_in_resources(el[0], el[1])

                self._preparation_for_purchase()
                self._buy_product(el[2], check)

                self.list_of_purchased_items.append([el[0], el[1], el[2], check])

    @staticmethod
    def _buy_product(price, amount):
        navigation_in_product_menu.set_product_quantity(amount)
        navigation_in_product_menu.set_product_price(price+1)
        navigation_in_product_menu.confirm_buy()

    @staticmethod
    def _preparation_for_purchase():
        navigation_in_product_menu.expand_price_menu()
        navigation_in_product_menu.click_on_purchase_order()


purchase_of_goods = PurchaseOfGoods()

