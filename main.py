from pico2d import *
import time
import tile
import tree
import bush
from character import Arang


def main():
    open_canvas(800, 600)

    tile.load_tile_images()
    tree.load_tree_images()
    bush.load_bush_images()

    character = Arang()

    running = True
    current_time = time.time()

    while running:
        new_time = time.time()
        frame_time = new_time - current_time
        current_time = new_time

        events = get_events()
        for e in events:
            if e.type == SDL_QUIT:
                running = False
            elif e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
                running = False
            else:
                character.handle_event(e)

        character.update(frame_time)

        clear_canvas()
        tile.draw_tile_map()
        bush.draw_bush_map()
        character.draw()
        tree.draw_tree_map()
        update_canvas()


    close_canvas()


if __name__ == '__main__':
    main()
