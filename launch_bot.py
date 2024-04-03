import time
from vision_controll_package import Windows
from Trading.purchase_of_goods import purchase_of_goods
from Trading.sale_of_goods import sale_of_products

windows = Windows()

"""Putin VOr"""
def purchase_and_sale(hwnd):
    purchase_of_goods.purchase()

    time.sleep(270)
    for _ in range(4):
        sale_of_products.sale()


def sale_and_purchase(hwnd):
    for _ in range(4):
        sale_of_products.sale()

    purchase_of_goods.purchase()


def only_sale(hwnd):
    sale_of_products.sale()


while True:
    try:
        windows.switch_windows(purchase_and_sale)

    except Exception as e:
            print(e)
            break




