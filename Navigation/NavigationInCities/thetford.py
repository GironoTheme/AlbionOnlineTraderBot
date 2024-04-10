from navigation_in_city import NavigationForCity, TravelBetweenCities
from Navigation.navigation_in_auction import navigation_in_auction
from time import sleep


class Thetford(NavigationForCity, TravelBetweenCities):
    @staticmethod
    def name_of_city():
        return "Thetford"

    def _exit_market_from_auction(self):
        sleep(2)
        self.move_down_left_diagonal(2.2)
        self.move_up_left_diagonal(7)
        sleep(4.5)

    def _go_to_auction_from_enter(self):
        sleep(4.5)
        self.move_down_right_diagonal(3.6)
        self.move_up_right_diagonal(1.2)

    def _open_an_travel_planner(self):
        self.move_and_click(975, 460)

    def _go_to_travel_planner(self):
        self.move_down_right_diagonal(3)
        self.move_up_right_diagonal(2.5)
        self._open_an_travel_planner()

    def go_to_travel_planner_from_auction(self):
        self._exit_market_from_auction()
        self._go_to_travel_planner()

        self.travel()

    def _go_to_market_from_travel_planner(self):
        self.move_down_left_diagonal(2.5)
        self.move_up_left_diagonal(3.2)

    def go_to_auction_from_travel_planner(self):
        sleep(2)
        self._go_to_market_from_travel_planner()
        self._go_to_auction_from_enter()



thetford = Thetford()
from vision_controll_package import Windows
windows = Windows()
def a(hwnd):
    thetford.go_to_travel_planner_from_auction()
    #thetford.go_to_auction_from_travel_planner()
windows.switch_windows(a)