from vision_controll_package import Image
from Navigation.navigation_in_auction import navigation_in_auction
from main_shared_variables import path_to_screenshots


class ParsingOfGoodsForSale(Image):
    def parsing(self):
        self._body_of_parsing()

    def _body_of_parsing(self):
        navigation_in_auction.click_on_sales_tab()
        for _ in range(4):
            self._get_name_of_product(_)
            self._comparison_with_current_list_of_products(self._get_name_of_product(_))

    def _comparison_with_current_list_of_products(self, name):
        pass

    def _get_name_of_product(self, multiplier):
        self.take_screenshot(path_to_screenshots+f'name_of_product.png',
                             (590, 390 + 112 * multiplier, 800, 425 + 112 * multiplier))
        return self.image_to_string(path_to_screenshots+f'name_of_product.png', False)


parsing_of_goods_for_sale = ParsingOfGoodsForSale()

