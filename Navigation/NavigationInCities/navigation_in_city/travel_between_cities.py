from vision_controll_package import Mouse, Keyboard
from Jsons.get_json import get_json


class TravelBetweenCities(Mouse, Keyboard):
    def choose_city(self, city):
        self.move_and_click(270, 230)
        self.type(city)

    def travel(self):
        self.choose_city('BridgeWatch')
        self.move_and_click(390, 950)

