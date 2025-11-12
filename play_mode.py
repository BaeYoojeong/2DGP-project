from pico2d import *
import game_world
import time
import tile
import tree
import bush
from character import Arang


character = None


def init():
    global character

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
    events = get_events()
    for e in events:
        if e.type == SDL_QUIT:
            import game_framework
            game_framework.quit()
        elif e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
            import game_framework
            game_framework.quit()
        elif e.type == SDL_KEYDOWN and e.key == SDLK_h:
            game_world.hitbox_draw()
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
    update_canvas()


def pause():
    pass


def resume():
    pass
