import time
from vision_controll_package import image, Windows, Mouse

from Parsing.parse_orders import parse_orders
from Parsing.parsing_of_goods_for_sale import parsing_of_goods_for_sale

from Trading.purchase_of_goods import purchase_of_goods
from Trading.sale_of_goods import sale_of_products

from Calculation.difference_calculation import difference_calculation

from Navigation.navigation_in_auction import navigation_in_auction
from Navigation.navigation_in_inventory import navigation_in_inventory

from Check.check_in_auction import CheckInAuction


mouse = Mouse()
windows = Windows()


def abse(hwnd):
    #navigation_in_auction.moving_between_resource_categories_and_levels_for_purchase(parse_orders.body_of_parser)
#
    #shopping_list = difference_calculation.calculation(parse_orders.list_of_orders)
    #purchase_of_goods.purchase(shopping_list)
#
    #time.sleep(270)
    #for _ in range(4):
    sale_of_products.sale()


windows.switch_windows(abse)
while True:
    try:
        abse(2)
    except Exception as e:
        print(e)
        break




