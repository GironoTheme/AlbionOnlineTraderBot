from navigation_in_city import NavigationForCity
from time import sleep


class BridgeWatch(NavigationForCity):
    @staticmethod
    def name_of_city():
        return "BridgeWatch"

    def _go_to_market_from_travel(self):
        sleep(2)
        self.move_down_left_diagonal(2)
        self.move_up_left_diagonal(4.5)

    def _go_to_auction_from_enter(self):
        sleep(4.5)
        self.move_down_right_diagonal(3.6)
        self.move_up_right_diagonal(1.2)

    def _exit_market_from_auction(self):
        sleep(2)
        self.move_down_left_diagonal(2.2)
        self.move_up_left_diagonal(7)
        sleep(4.5)

    def _go_to_travel_from_market_enter(self):
        self.move_down_right_diagonal(4)
        self.move_up_right_diagonal(2)

    def _open_an_travel_planer(self):
        self.move_and_click(950, 440)

    def go_to_travel_from_auction(self):
        self._exit_market_from_auction()
        self._go_to_travel_from_market_enter()

        self._open_an_travel_planer()

    def go_to_auction_from_travel(self):
        self._go_to_market_from_travel()
        self._go_to_auction_from_enter()


bridge_watch = BridgeWatch()
from vision_controll_package import Windows
windows = Windows()
def a(hwnd):
    #bridge_watch.go_to_auction_from_travel()
    print(bridge_watch.name_of_city())
    #bridge_watch.go_to_travel_from_auction()
    #thetford.go_to_auction_from_travel_planner()
windows.switch_windows(a)