import time

from vision_controll_package import image
from main_shared_variables import path_to_screenshots, path_to_templates
from vision_controll_package import mouse


class CheckInAuction:
    @staticmethod
    def checking_for_presence_of_button(cords=(1390, 402, 1402, 410), color_list=[135, 15, 40]):
        time.sleep(0.5)
        image.take_screenshot(path_to_screenshots+'buy_button.png', cords)
        main_color_of_zone = image.get_main_color(path_to_screenshots+'buy_button.png')

        if (95 <= main_color_of_zone[0] <= color_list[0] and
           0 <= main_color_of_zone[1] <= color_list[1] and
           5 <= main_color_of_zone[2] <= color_list[2]):

            return True
        return False

    @staticmethod
    def check_balance():
        mouse.move(1210, 125)
        time.sleep(1.4)
        image.take_screenshot(path_to_screenshots+'balance.png', (1090, 96, 1206, 121))

        try:
            return int(image.image_to_string(path_to_screenshots+'balance.png', True).replace(',', ''))

        except:
            return 0

    @staticmethod
    def checking_completed_transactions_tab():
        time.sleep(1.5)
        image.take_screenshot(path_to_screenshots+'completed_transactions_tab.png', (1480, 790, 1508, 815))

        return image.matching(path_to_templates+'completed_transactions_tab.png',
                              path_to_screenshots+'completed_transactions_tab.png')

    @staticmethod
    def checking_for_you_cant_carry_more_weight():
        time.sleep(6)
        image.take_screenshot(path_to_screenshots+'you_cant_carry_more_weight.png', (775, 440, 1140, 550))

        return image.matching(path_to_templates+'you_cant_carry_more_weight.png',
                              path_to_screenshots+'you_cant_carry_more_weight.png')

    @staticmethod
    def checking_count_of_product_for_sale():
        image.take_screenshot(path_to_screenshots+'amount_of_one_product_inside_inventory.png', (775, 570, 860, 600))

        image.delete_all_colors_except_one(path_to_screenshots+'amount_of_one_product_inside_inventory.png',
                                           [140, 110, 40], [240, 190, 70])
        try:
            return image.image_to_string(path_to_screenshots+'amount_of_one_product_inside_inventory.png', True)
        except:
            return 0

    @staticmethod
    def checking_for_main_menu():
        time.sleep(1)
        image.take_screenshot(path_to_screenshots+'albion_online.png', (790, 70, 1150, 290))

        return image.matching(path_to_templates+'albion_online.png', path_to_screenshots+'albion_online.png')



