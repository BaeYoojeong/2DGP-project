from pico2d import *

class OptionMenu:
    def __init__(self):
        self.is_open = False
        self.image = load_image('option_select.png')
        self.width = 800
        self.height = 600

        self.cols = 3
        self.rows = 1
        self.slot_width = 250
        self.slot_height = 600
        self.margin = 0

        self.selected_slot = None


    def toggle(self):
        self.is_open = not self.is_open
        print("옵션 메뉴:", "열림" if self.is_open else "닫힘")


    def draw(self):
        if not self.is_open:
            return

        w, h = get_canvas_width(), get_canvas_height()
        cx, cy = w // 2, h // 2

        self.image.draw(cx, cy, self.width, self.height)

        start_x = cx - (self.slot_width * 1.5) - self.margin
        start_y = cy -300

        for c in range(self.cols):

            sx = start_x + c * (self.slot_width + self.margin)
            sy = start_y

            if self.selected_slot == (0, c):
                draw_rectangle(sx - 3, sy - 3,
                               sx + self.slot_width + 3,
                               sy + self.slot_height + 3)


    def click(self, mx, my):
        if not self.is_open:
            return None

        w, h = get_canvas_width(), get_canvas_height()
        cx, cy = w // 2, h // 2

        start_x = cx - (self.slot_width * 1.5) - self.margin
        start_y = cy - 300

        for c in range(self.cols):

            sx = start_x + c * (self.slot_width + self.margin)
            sy = start_y

            if sx <= mx <= sx + self.slot_width and sy <= my <= sy + self.slot_height:
                self.selected_slot = (0, c)
                if c == 0:
                    print("저잣거리로 이동합니다.")
                    import game_framework
                    import shop_mode
                    game_framework.push_mode(shop_mode)
                elif c == 1:
                    print("요괴퇴치")
                elif c == 2:
                    print("마을정화")

                return (0, c)

        return None
