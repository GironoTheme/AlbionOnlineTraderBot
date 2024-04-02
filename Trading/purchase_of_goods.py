from Navigation.navigation_in_auction import navigation_in_auction
from Navigation.navigation_in_product_menu import navigation_in_product_menu
from Check.check_in_auction import CheckInAuction
from Calculation.calculation_for_trading import CalculationForTrading


class PurchaseOfGoods:
    def __init__(self):
        self.list_of_purchased_items = []

    def purchase(self, list_of_goods):
        self._product_search(list_of_goods)

        print('------------------------------------')
        print('Список купленных товаров')
        print(self.list_of_purchased_items)
        print('------------------------------------')

        return self.list_of_purchased_items

    def _product_search(self, list_of_goods):
        for el in list_of_goods:
            balance = CheckInAuction.check_balance()
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

