from pico2d import *
import tile

def main():
    open_canvas(800, 600)
    tile.load_tile_images()

    running = True
    while running:
        clear_canvas()
        tile.draw_tile_map()
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

