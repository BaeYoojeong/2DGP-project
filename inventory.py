from pico2d import *

class Inventory:
    def __init__(self):
        self.is_open = False
        self.image = load_image('inventory.png')
        self.width = 400
        self.height = 400

        # 인벤토리 이미지의 슬롯에 맞춰서 설정
        self.cols = 5
        self.rows = 5
        self.slot_size = 60
        self.margin = 20

        # 슬롯 배열 생성
        self.slots = [[None for _ in range(self.cols)] for _ in range(self.rows)]

        self.selected_slot = None


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

        # 0, 0 번째 슬롯 위치 계산
        start_x = x - (self.width // 2) + 10
        start_y = y + (self.height // 2) - 70

        # 슬롯 그리기
        for r in range(self.rows):
            for c in range(self.cols):

                sx = start_x + c * (self.slot_size + self.margin)
                sy = start_y - r * (self.slot_size + self.margin)

                # 슬롯 박스
                draw_rectangle(sx, sy, sx + self.slot_size, sy + self.slot_size)

                # 선택 표시
                if self.selected_slot == (r, c):
                    draw_rectangle(sx - 3, sy - 3,
                                   sx + self.slot_size + 3,
                                   sy + self.slot_size + 3)

    def click(self, mx, my):
        if not self.is_open:
            return None

        w, h = get_canvas_width(), get_canvas_height()
        cx, cy = w // 2, h // 2

        start_x = cx - (self.width // 2) + 40
        start_y = cy + (self.height // 2) - 100

        for r in range(self.rows):
            for c in range(self.cols):

                sx = start_x + c * (self.slot_size + self.margin)
                sy = start_y - r * (self.slot_size + self.margin)

                if sx <= mx <= sx + self.slot_size and sy <= my <= sy + self.slot_size:
                    self.selected_slot = (r, c)
                    print("슬롯 선택됨:", r, c)
                    return (r, c)

        return None

    def update(self, dt):
        # 인벤토리가 열려있을때 뒤에 게임화면 멈춤
        return self.is_open
