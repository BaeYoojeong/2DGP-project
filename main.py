from pico2d import *
import tile
import tree
import bush

def main():
    open_canvas(800, 600)
    tile.load_tile_images()
    tree.load_tree_images()
    bush.load_bush_images()

    running = True
    while running:
        clear_canvas()
        tile.draw_tile_map()
        bush.draw_bush_map()
        tree.draw_tree_map()

        update_canvas()

        # 이벤트 처리 (ESC로 종료)
        events = get_events()
        for e in events:
            if e.type == SDL_QUIT:
                running = False
            elif e.type == SDL_KEYDOWN and e.key == SDLK_ESCAPE:
                running = False

    close_canvas()

if __name__ == '__main__':
    main()

