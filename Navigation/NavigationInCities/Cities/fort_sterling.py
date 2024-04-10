from Navigation.NavigationInCities.navigation_in_city import NavigationForCity
from time import sleep


class FortSterling(NavigationForCity):
    @staticmethod
    def name_of_city():
        return "Fort Sterling"

    def _go_to_market_from_travel(self):
        sleep(2)
        self.move_down_left_diagonal(7.5)
        self.move_up_left_diagonal(2)

    def _go_to_auction_from_enter(self):
        sleep(5)
        self.move_down_right_diagonal(3.35)
        self.move_up_right_diagonal(1.2)

    def _exit_market_from_auction(self):
        sleep(2)
        self.move_down_left_diagonal(2.2)
        self.move_up_left_diagonal(7)
        sleep(5)

    def _go_to_travel_from_market_enter(self):
        self.move_down_right_diagonal(2)
        self.move_up_right_diagonal(7.5)
        self.move_down_right_diagonal(1.5)
        self.move_up_right_diagonal(1.4)
        self.move_down_right_diagonal(1.5)

    def _open_an_travel_planer(self):
        self.move_and_click(1077, 392)

    def go_to_travel_from_auction(self):
        self._exit_market_from_auction()
        self._go_to_travel_from_market_enter()

        self._open_an_travel_planer()

    def go_to_auction_from_travel(self):
        self._go_to_market_from_travel()
        self._go_to_auction_from_enter()

    def back_and_forth_with_execution_of_function(self, func):
        self.go_to_auction_from_travel()
        func()
        self.go_to_travel_from_auction()


fort_sterling = FortSterling()


