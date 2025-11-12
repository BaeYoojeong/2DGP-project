from pico2d import *

import game_framework
import play_mode
image = None

def init():
    # 타이틀 이미지를 로드
    global image

    image = load_image("title.png")

def update():
    pass

def draw():
    # 타이틀 이미지를 그려줌
    clear_canvas()
    image.draw(400, 300,800,600)
    update_canvas()

def finish():
    global image
    del image

def handle_events():
    event_list = get_events()   # 현재까지 들어온 이벤트들을 받아온다.
    # space키 이벤트 처리
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(play_mode)