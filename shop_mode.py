from pico2d import *
import game_framework
import play_mode
from player_data import player_data

from inventory import Inventory

shop = None  # 전역 이미지 변수

def init():
    global shop
    if shop is None:
        shop = load_image('shop.png')
        if player_data.inventory is None:
            player_data.inventory = Inventory()
    # 상품
    global shop_items
    shop_items = [
        {
            "name": "양배추 씨앗",
            "item_file": "seed_cabbage.png",
            "price": 20,
            "button": (750, 400, 820, 470)  # 엽전 버튼 좌표
        }
    ]

def finish():
    pass

def handle_events():
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()

        if e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
            game_framework.change_mode(play_mode)

        if e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
            mx, my = e.x, get_canvas_height() - e.y
            check_purchase(mx, my)

def update():
    pass

def draw():
    clear_canvas()
    shop.draw(get_canvas_width() // 2, get_canvas_height() // 2)

    for item in shop_items:
        x1, y1, x2, y2 = item["button"]
        cx = (x1 + x2) // 2
        cy = (y1 + y2) // 2
        draw_rectangle(x1, y1, x2, y2)
    update_canvas()



def check_purchase(mx, my):
    for item in shop_items:
        x1, y1, x2, y2 = item["button"]

        if x1 <= mx <= x2 and y1 <= my <= y2:
            price = item["price"]

            if player_data.gold < price:
                print("잔액 부족!")
                return

            # 골드 차감
            player_data.gold -= price

            print(f"{item['name']} 구매 완료! -{price}냥")

            # 인벤토리에 추가
            inv = player_data.inventory
            inv.add_item(item["item_file"])
            return
