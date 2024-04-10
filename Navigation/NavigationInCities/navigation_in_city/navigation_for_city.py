from vision_controll_package import Mouse, Keyboard


class NavigationForCity(Mouse, Keyboard):
    def move_down_left_diagonal(self, delay):
        self.move(860, 550)
        self.hold_down_right_mouse_button(delay)

    def move_down_right_diagonal(self, delay):
        self.move(1060, 550)
        self.hold_down_right_mouse_button(delay)

    def move_up_left_diagonal(self, delay):
        self.move(860, 350)
        self.hold_down_right_mouse_button(delay)

    def move_up_right_diagonal(self, delay):
        self.move(1060, 350)
        self.hold_down_right_mouse_button(delay)


