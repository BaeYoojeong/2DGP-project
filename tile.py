from pico2d import *

tile = 32 * 1.5   # 타일 크기

# 타일 맵
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
seed_image = None
# 씨앗 맵 (0: 씨앗 없음, 1: 씨앗 있음)
seed_map = [[0 for _ in range(MAP_W)] for _ in range(MAP_H)]
# 물 준 상태 맵 (0: 안줌, 1: 물줌)
water_map = [[0 for _ in range(MAP_W)] for _ in range(MAP_H)]

def load_tile_images():
    global tile_images, seed_image
    tile_images = {
        0: load_image('a_grass.png'),
        1: load_image('a_grass_rock.png'),
        2: load_image('brown.png'),   # 갈아놓은 밭
        3: load_image('water_ground.png')   # 물 뿌린 밭
    }

    seed_image = load_image('seed.png')


def draw_tile_map():
    for y in range(MAP_H):
        for x in range(MAP_W):
            tile_num = tile_map[y][x]

            if tile_num in tile_images:
                tile_images[tile_num].draw((x * tile) + 20,
                                           ((MAP_H - y) * tile) - 40,
                                           tile, tile)

            # 씨앗이 있는 경우 씨앗 이미지 그리기
            if seed_map[y][x] == 1:
                seed_image.draw((x * tile) + 20,
                                ((MAP_H - y) * tile) - 40,
                                20, 20)  # 적당한 크기


# 타일 변경(땅 → 밭 만들기)
def change_tile(tx, ty):
    if 0 <= tx < MAP_W and 0 <= ty < MAP_H:
        tile_map[ty][tx] = 2


# 씨앗 심기 함수
def plant_seed(tx, ty):
    if tile_map[ty][tx] == 2:
        seed_map[ty][tx] = 1
    else:
        print("씨앗은 갈아놓은 밭에만 심을 수 있습니다.")

# 물 뿌리기 함수
def water_tile(tx, ty):
    if tile_map[ty][tx] == 2 or tile_map[ty][tx] == 3:
        water_map[ty][tx] = 1
        tile_map[ty][tx] = 3
    else:
        print("물은 씨앗이 심어진 밭에만 뿌릴 수 있습니다.")