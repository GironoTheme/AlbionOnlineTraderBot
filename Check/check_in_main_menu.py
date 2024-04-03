from vision_controll_package import image
from main_shared_variables import path_to_screenshots, path_to_templates
from time import sleep


class CheckInMainMenu:
    @staticmethod
    def checking_for_main_menu():
        sleep(1)
        image.take_screenshot(path_to_screenshots + 'albion_online.png', (790, 70, 1150, 290))

        return image.matching(path_to_templates + 'albion_online.png', path_to_screenshots + 'albion_online.png')

    @staticmethod
    def checking_for_ok():
        sleep(1)
        image.take_screenshot(path_to_screenshots + 'the_server_does_not_allow_players.png', (720, 440, 1200, 490))

        return image.matching(path_to_templates + 'the_server_does_not_allow_players.png',
                              path_to_screenshots + 'the_server_does_not_allow_players.png')

