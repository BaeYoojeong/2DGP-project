from pico2d import *
import game_framework
import play_mode

shop = None  # 전역 이미지 변수

def init():
    global shop
    if shop is None:
        shop = load_image('shop.png')

def finish():
    pass

def handle_events():
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            game_framework.quit()

        if e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
            # ESC → 플레이 모드로 돌아가기
            game_framework.change_mode(play_mode)

def update():
    pass

def draw():
    clear_canvas()
    shop.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    update_canvas()
