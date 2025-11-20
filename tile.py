from pico2d import *

tile = 32*1.5   # 타일 크기

# 타일 노가다 붙이기
tile_map = [
    [0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0,  1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

MAP_H = len(tile_map)
MAP_W = len(tile_map[0])

tile_images = {}

def load_tile_images():
    global tile_images
    tile_images = {
        0: load_image('a_grass.png'),
        1: load_image('a_grass_rock.png'),
        2: load_image('brown.png')
    }

def draw_tile_map():
    for y in range(MAP_H):
        for x in range(MAP_W):
            tile_num = tile_map[y][x]
            if tile_num in tile_images:
                tile_images[tile_num].draw((x * tile)+20, (((MAP_H - y) * tile)-40), tile, tile)

# 타일 변경 함수 (기존 바닥->밭)
def change_tile(tx, ty):
    if 0 <= tx < MAP_W and 0 <= ty < MAP_H:
        tile_map[ty][tx] = 2
