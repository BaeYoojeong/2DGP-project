from pico2d import *

running = True


WIN_W, WIN_H = 800, 600

tile = 62    # 타일 크기

# 타일 노가다 붙이기
tile_map = [
    [0,0,0,1,0,0,1,0,0,0],
    [0,0,0,1,0,0,1,0,0,0],
    [0,0,0,1,0,0,1,0,0,0]
]


MAP_H = len(tile_map)
MAP_W = len(tile_map[0]) if MAP_H > 0 else 0

open_canvas(WIN_W, WIN_H)

# 타일 정의
tile_images = {
    0: load_image('a_grass.png'),
    1: load_image('a_grass_rock.png')
}

# 맵 그리기
def draw_map():
    for y in range(MAP_H):
        for x in range(MAP_W):
            tile_num = tile_map[y][x]
            if tile_num in tile_images:
                tile_images[tile_num].draw((x+0.5) * tile, (MAP_H + 6.2 - y) * tile, 62, 62) # 0행을 위에서 부터 그리려고 +15함




# 키 입력 처리
def handle_events():
    global running
    events  = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    return True

while running:
    clear_canvas()
    draw_map()
    update_canvas()
    handle_events()
    delay(0.05)



