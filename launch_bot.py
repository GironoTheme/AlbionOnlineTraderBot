import time
from vision_controll_package import Windows
from Check.check_in_auction import CheckInAuction
from Trading.purchase_of_goods import purchase_of_goods
from Trading.sale_of_goods import sale_of_products
from main_shared_variables import min_balance

windows = Windows()


def purchase():
    if CheckInAuction.check_balance() >= min_balance:
        purchase_of_goods.purchase()

    else:
        while CheckInAuction.check_balance() <= min_balance:
            sale_of_products.sale()
            time.sleep(270)

        purchase_of_goods.purchase()


def purchase_and_sale(hwnd):
    purchase()

    time.sleep(270)
    for _ in range(4):
        sale_of_products.sale()


def sale_and_purchase(hwnd):
    for _ in range(4):
        sale_of_products.sale()

    purchase()


def only_sale(hwnd):
    sale_of_products.sale()


while True:
    try:
        windows.switch_windows(purchase_and_sale)

    except Exception as e:
            print(e)
            break




