from Actions.actions_in_game import actions_in_game
from Navigation.NavigationInCities.Cities.bridge_watch import bridge_watch
from Navigation.NavigationInCities.Cities.thetford import thetford
from Navigation.NavigationInCities.Cities.fort_sterling import fort_sterling
from Navigation.NavigationInCities.Cities.lymhurst import lymhurst
from Navigation.NavigationInCities.Cities.caerleon import caerleon
from Navigation.NavigationInCities.Cities.martlock import martlock
from Actions.back_to_auction import back_to_auction

from vision_controll_package import mouse, keyboard
from time import sleep


class HikingBetweenCities:
    def __init__(self):
        self.cities = [bridge_watch, caerleon, lymhurst, martlock]

    def start_hiking_in_thetford(self, func):
        sleep(1)

        func()
        thetford.go_to_travel_planner_from_auction()

        for city in range(len(self.cities)):
            back_to_auction.back_to_auction()

            self._choose_city(self.cities[city].name_of_city())
            sleep(12.5)

            self.cities[city].back_and_forth_with_execution_of_function(func)

        # mouse.move_and_click(270, 230)
        mouse.move_and_click(242, 565)
        mouse.move_and_click(410, 950)

        sleep(15)
        actions_in_game.close_ad()

        thetford.go_to_auction_from_travel_planner()

    def _choose_city(self, city):
        # mouse.move_and_click(270, 230)
        # keyboard.type(city)

        if city == "BridgeWatch":
            mouse.move_and_click(257, 643)
        if city == "Caerleon":
            mouse.move_and_click(263, 607)
        if city == "Lymhurst":
            mouse.move_and_click(303, 618)
        if city == "Martlock":
            mouse.move_and_click(227, 604)

        # keyboard.press_button('enter')

        # mouse.move_and_click(410, 950)
        # sleep(0.8)
        mouse.move_and_click(410, 950)


hiking_between_cities = HikingBetweenCities()




