import time
from vision_controll_package import Windows
from Check.check_in_auction import CheckInAuction
from Trading.purchase_of_goods import purchase_of_goods
from Trading.sale_of_goods import sale_of_products
from main_shared_variables import min_balance
from Navigation.NavigationInCities.hiking_between_cities import hiking_between_cities
from Actions.actions_in_game import actions_in_game
windows = Windows()


def purchase():
    if CheckInAuction.check_balance() >= min_balance:
        purchase_of_goods.purchase()

    else:
        while CheckInAuction.check_balance() <= min_balance:
            sale_of_products.sale()
            time.sleep(270)

        purchase_of_goods.purchase()


def purchase_and_sale():
    actions_in_game.open_an_auction()

    purchase()

    time.sleep(270)
    for _ in range(4):
        sale_of_products.sale()

    actions_in_game.close_auction_menu()


def sale_and_purchase():
    actions_in_game.open_an_auction()

    for _ in range(4):
        sale_of_products.sale()

    purchase()

    actions_in_game.close_auction_menu()


def only_sale():
    actions_in_game.open_an_auction()

    sale_of_products.sale()

    actions_in_game.close_auction_menu()


def walker(hwnd):
    hiking_between_cities.start_hiking_in_thetford(purchase_and_sale)


while True:
    try:
        windows.switch_windows(walker)

    except Exception as e:
            print(e)
            break




