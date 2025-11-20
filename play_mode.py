from pico2d import *
import game_world
import time
import tile
import tree
import bush
from character import Arang


character = None

snap_x = None
snap_y = None

def init():
    global character
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
    global snap_x, snap_y
    events = get_events()

    for e in events:
        # 키보드 입력 처리==============
        if e.type == SDL_QUIT:
            import game_framework
            game_framework.quit()
        elif e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
            import game_framework
            game_framework.quit()
        elif e.type == SDL_KEYDOWN and e.key == SDLK_h:
            game_world.hitbox_draw()

        # 마우스 입력 처리 ==============
        elif e.type == SDL_MOUSEMOTION:
            mx, my = e.x, get_canvas_height() - e.y

            ty = int((tile.MAP_H * tile.tile - my) // tile.tile)
            tx = int(mx // tile.tile)

            if 0 <= tx < tile.MAP_W and 0 <= ty < tile.MAP_H:
                snap_x = tx
                snap_y = ty
            else:
                snap_x = None
                snap_y = None
        # 캐릭터 주변 1칸 이내 타일 변경
        elif e.type == SDL_MOUSEBUTTONDOWN and e.button == SDL_BUTTON_LEFT:
            if snap_x is not None and snap_y is not None:

                # 캐릭터의 현재 위치 → 타일 인덱스로 변환
                char_tx = int(character.x // tile.tile)
                char_ty = int((tile.MAP_H * tile.tile - character.y) // tile.tile)

                # 캐릭터 주변 8칸(상하좌우/대각선)만 수정 허용
                if abs(snap_x - char_tx) <= 1 and abs(snap_y - char_ty) <= 1:
                    tile.change_tile(snap_x, snap_y)
                else:
                    print("캐릭터 주변 1칸 이내만 변경 가능합니다.")

        else:
            character.handle_event(e)

def update():
    static_prev = getattr(update, "_prev", None)
    now = time.time()
    if static_prev is None:
        update._prev = now
        frame_time = 0
    else:
        frame_time = now - static_prev
        update._prev = now

    game_world.handle_collisions()
    character.update(frame_time)


def draw():
    clear_canvas()
    tile.draw_tile_map()
    bush.draw_bush_map()
    character.draw()
    tree.draw_tree_map()

    if snap_x is not None and snap_y is not None:
        left = snap_x * tile.tile
        right = left + tile.tile

        top = (tile.MAP_H - snap_y) * tile.tile
        bottom = top - tile.tile

        draw_rectangle(left-5, bottom-15, right-5, top-15)



    update_canvas()

def pause():
    pass


def resume():
    pass
