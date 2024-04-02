from vision_controll_package import Image


class PhotoPreparation(Image):
    def converting_numbers_to_line_from_about_product_menu(self, screenshot):
        self.upscale_image(screenshot, 7)
        self.upscale_contrast(screenshot, 7)

        result = self.image_to_string(screenshot, False)

        if ''.join(filter(str.isdigit, result[result.rfind(' ') + 1:])) == '':
            return 0

        return ''.join(filter(str.isdigit, result[result.rfind(' ') + 1:]))


photo_preparation = PhotoPreparation()
