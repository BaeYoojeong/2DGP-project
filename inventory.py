from pico2d import *

from item_data import get_price
from player_data import player_data

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

        self.item_images = {}
        self.font = load_font('Hakgyoansim_BoardmarkerR.ttf', 16)

    def toggle(self):
        self.is_open = not self.is_open
        print("인벤토리:", "열림" if self.is_open else "닫힘")

    def get_item_image(self, item_name):
        if item_name not in self.item_images:
            self.item_images[item_name] = load_image(item_name)
        return self.item_images[item_name]

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

                slot = self.slots[r][c]
                if slot:
                    # 아이템 이미지 그리기
                    item_img = self.get_item_image(slot["item"])
                    item_img.draw(sx + self.slot_size // 2,
                                  sy + self.slot_size // 2,
                                  70, 70)
                    # 수량 표시
                    self.font.draw(sx + 5, sy + 5, str(slot["count"]), (0, 0, 0))

                # 선택 표시
                if self.selected_slot == (r, c):
                    draw_rectangle(sx - 3, sy - 3,
                                   sx + self.slot_size + 3,
                                   sy + self.slot_size + 3)
    # 인벤토리 클릭
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

    # 인벤토리에 아이템 넣기
    def add_item(self, item_name):
        # 동일 아이템 -> count 증가
        for r in range(self.rows):
            for c in range(self.cols):
                slot = self.slots[r][c]
                if slot and slot["item"] == item_name:
                    slot["count"] += 1
                    print(f"{item_name} 수량 증가  {slot['count']}")
                    return

        # 빈 슬롯 -> 새로 추가
        for r in range(self.rows):
            for c in range(self.cols):
                if self.slots[r][c] is None:
                    self.slots[r][c] = {"item": item_name, "count": 1}
                    print(f"{item_name} 인벤토리에 추가됨 ({r}, {c})")
                    return

        print("인벤토리가 가득 찼습니다!")
    # 물건판매
    def sell_item(self, mx, my):
        if not self.is_open:
            return

        w, h = get_canvas_width(), get_canvas_height()
        cx, cy = w // 2, h // 2

        start_x = cx - (self.width // 2) + 40
        start_y = cy + (self.height // 2) - 100

        for r in range(self.rows):
            for c in range(self.cols):

                sx = start_x + c * (self.slot_size + self.margin)
                sy = start_y - r * (self.slot_size + self.margin)

                if sx <= mx <= sx + self.slot_size and sy <= my <= sy + self.slot_size:

                    slot = self.slots[r][c]
                    if slot is None:
                        return

                    item_name = slot["item"]
                    price = get_price(item_name)

                    if price is None:
                        print(f"'{item_name}' 은(는) 등록되지 않아 판매할 수 없습니다.")
                        return

                    player_data.gold += price
                    print(f"{item_name} 판매! +{price} 골드")

                    slot["count"] -= 1
                    if slot["count"] <= 0:
                        self.slots[r][c] = None

                    return
    # 씨앗 있음?
    def has_item(self, item_name):
        for r in range(self.rows):
            for c in range(self.cols):
                slot = self.slots[r][c]
                if slot and slot["item"] == item_name and slot["count"] > 0:
                    return True
        return False
    # 씨앗 소비
    def consume_item(self, item_name):
        for r in range(self.rows):
            for c in range(self.cols):
                slot = self.slots[r][c]
                if slot and slot["item"] == item_name:
                    slot["count"] -= 1
                    if slot["count"] <= 0:
                        self.slots[r][c] = None
                    return True
        return False
