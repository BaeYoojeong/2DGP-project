from pico2d import *
import time
from character import Arang


character = None


def init():
    global character\

    character = Arang()



def finish():
    close_canvas()


def handle_events():
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            import game_framework
            game_framework.quit()
        elif e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
            import game_framework
            game_framework.quit()
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
    character.update(frame_time)


def draw():
    clear_canvas()
    character.draw()
    update_canvas()


def pause():
    pass


def resume():
    pass
