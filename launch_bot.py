import time
import threading

from Check.check_in_main_menu import CheckInMainMenu
from vision_controll_package import Windows
from Check.check_in_auction import CheckInAuction
from Trading.purchase_of_goods import purchase_of_goods
from Trading.sale_of_goods import sale_of_products
from main_shared_variables import min_balance
from Navigation.NavigationInCities.hiking_between_cities import hiking_between_cities
from Actions.actions_in_game import actions_in_game

windows = Windows()


def purchase():
    actions_in_game.open_an_auction()

    if CheckInAuction.check_balance() >= min_balance:
        purchase_of_goods.purchase()

    else:
        while CheckInAuction.check_balance() <= min_balance:
            sale_of_products.sale()

        purchase_of_goods.purchase()

    actions_in_game.close_auction_menu()


def only_sale():
    actions_in_game.open_an_auction()

    sale_of_products.sale()

    actions_in_game.close_auction_menu()


def schedule_check_ad():
    """Функция, вызывающая check_ad каждые 3.5 секунды."""
    while True:
        time.sleep(3.5)
        actions_in_game.close_ad()


def a():
    print(1 + 1)


def walker():
    """Функция, выполняющая основную логику."""
    hiking_between_cities.start_hiking_in_thetford(purchase)
    hiking_between_cities.start_hiking_in_thetford(only_sale)


def shell(hwnd):
    """Функция для передачи в switch_windows."""
    # Запуск параллельного потока для check_ad
    threading.Thread(target=schedule_check_ad, daemon=True).start()

    # Выполнение основной логики
    walker()


# Основной цикл
while True:
    try:
        windows.switch_windows(shell)
    except Exception as e:
        print(e)
        break




