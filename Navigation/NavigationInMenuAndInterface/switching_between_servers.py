from Navigation.NavigationInMenuAndInterface.navigation_in_game_menu import NavigationInGameMenu
from Navigation.NavigationInMenuAndInterface.navigation_in_main_menu import NavigationInMainMenu


class SwitchingBetweenServers(NavigationInMainMenu, NavigationInGameMenu):
    def switching(self, func):
        for i in range(1):
            self.choose_a_server(i)
            func()
            self.remove_ads()
            self.logout()


switching_between_servers = SwitchingBetweenServers()


