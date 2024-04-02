from math import ceil, floor
from main_shared_variables import purchase_limit


class CalculationForTrading:
    @staticmethod
    def checking_for_possibility_of_purchase(price, balance):
        price = price + 1

        if balance > price + ceil(price / 100 * 2.5):
            if balance > purchase_limit + ceil(purchase_limit / 100 * 2.5):
                return floor(purchase_limit / (price + ceil(price / 100 * 2.5)))

            elif balance < purchase_limit + ceil(purchase_limit / 100 * 2.5):
                return floor(balance / (price + ceil(price / 100 * 2.5)))

            else:
                return False

        else:
            return False

    @staticmethod
    def checking_for_possibility_of_sale(price, amount, balance):
        price = price - 1
        sum_of_sale = price * amount
        tax_calculation = ceil(sum_of_sale / 100 * 10.5)

        if balance > tax_calculation:
            return True, tax_calculation

        else:
            return False


