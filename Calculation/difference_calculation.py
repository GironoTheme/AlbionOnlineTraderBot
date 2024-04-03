from main_shared_variables import percent_of_difference, limit_for_calculating_best_price


class DifferenceCalculation:
    def __init__(self):
        self.list_of_prices_and_difference = []

    def calculation(self, list_of_orders, for_sale=False):
        self._sort_orders(list_of_orders, for_sale)

        return self._get_sorted_list(for_sale)

    def _get_sorted_list(self, for_sale=False):
        if for_sale is True:
            data = [item for item in self.list_of_prices_and_difference if item != [None, None]]

        else:
            data = [item for item in self.list_of_prices_and_difference if item != [None, None] and
                    item[4] >= percent_of_difference]

            print(sorted(data, key=lambda x: x[4], reverse=True))

        return sorted(data, key=lambda x: x[4], reverse=True)

    def _sort_orders(self, list_of_orders, for_sale):
        for _ in list_of_orders:
            buy_order = self._calculating_the_best_price(self._prepare_list_of_orders(_))
            sell_order = self._calculating_the_best_price(self._prepare_list_of_orders(_), True)

            if buy_order is not None or sell_order is not None:
                diff = self._calculating_difference(buy_order, sell_order)
                if for_sale is False:
                    buy_order.append(diff)
                    self.list_of_prices_and_difference.append(buy_order)

                else:
                    sell_order.append(diff)
                    self.list_of_prices_and_difference.append(sell_order)

    @staticmethod
    def _calculating_difference(buy_order, sell_order):
        # P=(B−A)/A∗100
        # P=(A−B)/B∗100
        difference = (sell_order[2] - buy_order[2]) / buy_order[2] * 100
        return int(difference)

    @staticmethod
    def _prepare_list_of_orders(list_of_orders):

        def is_outlier(value, data, threshold=0.9):
            avg = sum(item[2] for item in data) / len(data)
            return abs((value - avg) / avg) >= threshold

        filtered_data = [item for item in list_of_orders if not is_outlier(item[2], list_of_orders)]

        return filtered_data

    @staticmethod
    def _calculating_the_best_price(orders_of_one_product, sell_orders=False):
        sorted_data = sorted(orders_of_one_product, key=lambda x: x[2], reverse=sell_orders)
        best_price = 0
        for order in sorted_data:
            current_price = order[2] * order[3]
            best_price += current_price

            if best_price >= limit_for_calculating_best_price:
                return order


difference_calculation = DifferenceCalculation()




