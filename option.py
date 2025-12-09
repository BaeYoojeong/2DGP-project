from pico2d import *


class OptionMenu:
    def __init__(self):
        self.is_open = False
        self.image = load_image('option_select.png')  # 옵션창 이미지
        self.width = 800
        self.height = 600

    def toggle(self):
        self.is_open = not self.is_open
        print("옵션 메뉴:", "열림" if self.is_open else "닫힘")

    def draw(self):
        if not self.is_open:
            return

        w, h = get_canvas_width(), get_canvas_height()
        cx, cy = w // 2, h // 2
        self.image.draw(cx, cy, self.width, self.height)
    def update(self, dt):
        return self.is_open
