from pico2d import *

running = True


WIN_W, WIN_H = 960, 640

tile = 64    # 타일 크기

# 타일 노가다 붙이기
tile_map = [
    [0,1,0,0,1,1,0,0,0,1,1,0,0,1,0],
    [0,0,1,0,0,0,0,0,1,0,0,0,1,0,0],
    [1,0,0,0,0,1,0,0,0,0,1,0,0,1,0],
    [0,0,0,0,1,0,0,0,0,0,0,0,0,0,0],
    [0,0,1,0,0,0,0,1,0,1,0,0,1,1,1],
    [1,0,0,0,1,1,0,0,0,0,1,0,0,1,0],
    [0,0,1,0,0,1,1,0,0,0,1,0,0,0,0],
    [0,0,1,1,0,0,0,1,0,0,0,1,0,1,1],
    [1,0,0,0,1,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,1,0,1,0,0,0,1,0,0,1,1,1]
]


MAP_H = len(tile_map)
MAP_W = len(tile_map[0])

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
                tile_images[tile_num].draw((x+0.5) * tile, (MAP_H -0.5 - y) * tile, 64, 64)




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



