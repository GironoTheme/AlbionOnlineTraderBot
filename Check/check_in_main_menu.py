from vision_controll_package import image
from main_shared_variables import path_to_screenshots, path_to_templates
from time import sleep


class CheckInMainMenu:
    @staticmethod
    def checking_for_main_menu():
        sleep(1)
        image.take_screenshot(path_to_screenshots + 'albion_online.png', (750, 100, 1150, 295))
        return image.matching(path_to_templates + 'albion_online.png', path_to_screenshots + 'albion_online.png')

    @staticmethod
    def checking_for_ok():
        sleep(1)
        image.take_screenshot(path_to_screenshots + 'the_server_does_not_allow_players.png', (905, 535, 1015, 555))

        return image.matching(path_to_templates + 'the_server_does_not_allow_players.png',
                              path_to_screenshots + 'the_server_does_not_allow_players.png')

    @staticmethod
    def checking_for_ok_for_failed_to_connect_to_server():
        sleep(1)
        image.take_screenshot(path_to_screenshots+'failed_to_connect_to_server.png', (910, 515, 1010, 535))
        print(22222222222222222222222222222222222)
        return image.matching(path_to_templates + 'failed_to_connect_to_server.png',
                              path_to_screenshots + 'failed_to_connect_to_server.png')
