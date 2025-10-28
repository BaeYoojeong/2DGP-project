from pico2d import *

running = True

WIN_W, WIN_H = 960, 640

tile = 64    # 타일 크기
bush = 64    # 부쉬 크기
tree = 64    # 나무 크기
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
# 부쉬 노가다 붙이기
bush_map = [
    [-1,-1,0,0,0,0,0,0,0,0,0,0,0,-1,-1],
    [-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1],
    [-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1],
    [-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1],
    [-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1],
    [-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1],
    [-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1],
    [-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1],
    [-1,-1,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,-1,-1],
    [-1,-1,0,0,0,0,0,0,0,0,0,0,0,-1,-1]
]
# 나무 노가다 붙이기
tree_map = [
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0],
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0],
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0],
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0],
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0],
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0],
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0],
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0],
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0],
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0]
]



MAP_H = len(tile_map)
MAP_W = len(tile_map[0])

open_canvas(WIN_W, WIN_H)

# 타일 정의
tile_images = {
    0: load_image('a_grass.png'),
    1: load_image('a_grass_rock.png')
}

bush_images = {
    0: load_image('bush01.png')
}
tree_images = {
    0: load_image('tree01_1.png')
}

# 맵 그리기
def draw_map():
    for y in range(MAP_H):
        for x in range(MAP_W):
            tile_num = tile_map[y][x]
            if tile_num in tile_images:
                tile_images[tile_num].draw((x+0.5) * tile, (MAP_H -0.5 - y) * tile, tile, tile)

            bush_num = bush_map[y][x]
            if bush_num in bush_images:
                bush_images[bush_num].draw((x+0.5) * bush, (MAP_H -0.5 - y) * bush, bush, bush)

            tree_num = tree_map[y][x]
            if tree_num in tree_images:
                tree_images[tree_num].draw((x* tree)+1, ((MAP_H - y)+1) * tree, tree, tree+ 32)

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



