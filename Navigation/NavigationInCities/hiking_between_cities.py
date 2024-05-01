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

            self.cities[city].back_and_forth_with_execution_of_function(func)

        self._choose_city(thetford.name_of_city())

        thetford.go_to_auction_from_travel_planner()

    def _choose_city(self, city):
        mouse.move_and_click(270, 230)
        keyboard.type(city)

        mouse.move_and_click(410, 950)
        sleep(10)


hiking_between_cities = HikingBetweenCities()




