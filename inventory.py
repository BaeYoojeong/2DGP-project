from pico2d import *

class Inventory:
    def __init__(self):
        self.is_open = False
        self.image = load_image('inventory.png')
        self.width = 400
        self.height = 400

    def toggle(self):
        self.is_open = not self.is_open
        print("인벤토리:", "열림" if self.is_open else "닫힘")

    def draw(self):
        if not self.is_open:
            return


        w, h = get_canvas_width(), get_canvas_height()
        x = w // 2
        y = h // 2

        self.image.draw(x, y, self.width, self.height)

    def update(self, dt):
        # 인벤토리가 열려있을때 뒤에 게임화면 멈춤
        return self.is_open
