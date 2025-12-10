from pico2d import *
import game_world
import time
import tile
import tree
import bush
import shop_mode
import game_framework

from character import Arang
from inventory import Inventory
from player_data import player_data
from option import OptionMenu


character = None
inventory = None
option_menu = None

snap_x = None
snap_y = None

# tile_mode (1->괭이질, 2->씨앗심기)
tile_mode = 1
def init():
    global character, inventory, option_menu
    option_menu = OptionMenu()
    inventory = Inventory()

    if player_data.inventory is None:
        inventory = Inventory()
        player_data.inventory = inventory
    else:
        inventory = player_data.inventory
    mouse_x, mouse_y =0,0
    tile.load_tile_images()
    tree.load_tree_images()
    bush.load_bush_images()
    bush.create_bushes()

    character = Arang()

    for b in bush.bush_list:
        game_world.add_collision_pair('arang:bush', character, b)


def finish():
    close_canvas()


def handle_events():
    global snap_x, snap_y, tile_mode,inventory
    events = get_events()

    for e in events:
        # 키보드 입력 처리==============
        if e.type == SDL_QUIT:
            import game_framework
            game_framework.quit()
        if e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
            import game_framework
            game_framework.quit()

        # 히트박스
        if e.type == SDL_KEYDOWN and e.key == SDLK_h:
            game_world.hitbox_draw()

        # 타일모드 변경
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_1:
                tile_mode = 1
                print("1 - 괭이 선택")
                continue
            elif e.key == SDLK_2:
                tile_mode = 2
                print("2 - 씨앗 선택")
                continue
            elif e.key == SDLK_3:
                tile_mode = 3
                print("3 - 물뿌리개 선택")
                continue
            elif e.key == SDLK_4:
                tile_mode = 4
                print("4 - 손(수확) 선택")
                continue
            elif e.key == SDLK_i:
                inventory.toggle()
                continue
            elif e.key == SDLK_o:
                option_menu.toggle()
                continue

        # 마우스 입력 처리==============
        # 인벤토리 우클릭 => 판매
        if inventory.is_open and e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_RIGHT:
            mx, my = e.x, get_canvas_height() - e.y
            inventory.sell_item(mx, my)
            continue

        # 마우스 이동 => 스냅 좌표 계산
        if e.type == SDL_MOUSEMOTION:
            mx, my = e.x, get_canvas_height() - e.y
            ty = int((tile.MAP_H * tile.tile - my) // tile.tile)
            tx = int(mx // tile.tile)

            if 0 <= tx < tile.MAP_W and 0 <= ty < tile.MAP_H:
                snap_x = tx
                snap_y = ty
            else:
                snap_x = None
                snap_y = None
            continue

        # 마우스 클릭 =>  타일 변경 처리
        if e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
            # 인벤토리
            if inventory.is_open and e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
                mx, my = e.x, get_canvas_height() - e.y
                inventory.click(mx, my)
                continue

            if option_menu.is_open and e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
                mx, my = e.x, get_canvas_height() - e.y
                option_menu.click(mx, my)
                continue

            if snap_x is not None and snap_y is not None:
                char_tx = int(character.x // tile.tile)
                char_ty = int((tile.MAP_H * tile.tile - character.y) // tile.tile)

                if abs(snap_x - char_tx) <= 1 and abs(snap_y - char_ty) <= 1:

                    if tile_mode == 1:
                        tile.change_tile(snap_x, snap_y)
                    elif tile_mode == 2:
                        tile.plant_seed(snap_x, snap_y)
                    elif tile_mode == 3:
                        tile.water_tile(snap_x, snap_y)
                    elif tile_mode == 4:
                        tile.harvest(snap_x, snap_y)
                else:
                    print("캐릭터 주변 1칸만 변경 가능")
            continue

        character.handle_event(e)


def update():
    global inventory
    # 옵션메뉴 열려있으면 게임 업데이트 중단
    if option_menu.is_open:
        return

    # 인벤토리 열려있으면 게임 업데이트 중단
    if inventory.is_open:
        return

    static_prev = getattr(update, "_prev", None)
    now = time.time()
    if static_prev is None:
        update._prev = now
        frame_time = 0
    else:
        frame_time = now - static_prev
        update._prev = now

    # 타일 씨앗 성장 업데이트
    tile.update_seed_growth(frame_time)

    game_world.handle_collisions()
    character.update(frame_time)


def draw():
    clear_canvas()
    tile.draw_tile_map()
    bush.draw_bush_map()
    character.draw()
    tree.draw_tree_map()

    draw_gold_ui()

    if snap_x is not None and snap_y is not None:
        left = snap_x * tile.tile
        right = left + tile.tile

        top = (tile.MAP_H - snap_y) * tile.tile
        bottom = top - tile.tile

        draw_rectangle(left-5, bottom-15, right-5, top-15)

    if inventory.is_open:
        inventory.draw()
    if option_menu.is_open:
        option_menu.draw()

    update_canvas()

def pause():
    pass


def resume():
    pass

def draw_gold_ui():
    font = load_font('Hakgyoansim_BoardmarkerR.ttf', 20)
    font.draw(30, get_canvas_height() - 40, f"Gold: {player_data.gold}", (255,0,0))