from Navigation.NavigationInCities.navigation_in_city import NavigationForCity
from time import sleep


class Thetford(NavigationForCity):
    @staticmethod
    def name_of_city():
        return "Thetford"

    def _exit_market_from_auction(self):
        sleep(2)
        self.move_down_left_diagonal(2.2)
        self.move_up_left_diagonal(7)
        sleep(5)

    def _go_to_auction_from_enter(self):
        sleep(5)
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

    def _go_to_market_from_travel_planner(self):
        self.move_down_left_diagonal(0.6)
        self.move_up_left_diagonal(2)

    def go_to_auction_from_travel_planner(self):
        sleep(2)
        self._go_to_market_from_travel_planner()
        self._go_to_auction_from_enter()

    def back_and_forth_with_execution_of_function(self, func):
        self.go_to_auction_from_travel_planner()
        func()
        self.go_to_travel_planner_from_auction()


thetford = Thetford()
