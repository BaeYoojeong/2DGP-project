from pico2d import *
import play_mode
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
sprout_image = None
mid_image = None
crop_image = None

# 성장 타이머 (경과 시간 저장)
seed_timer = [[0 for _ in range(MAP_W)] for _ in range(MAP_H)]
# 씨앗 맵
seed_map = [[0 for _ in range(MAP_W)] for _ in range(MAP_H)]
# 물 준 상태 맵 (0: 안줌, 1: 물줌)
water_map = [[0 for _ in range(MAP_W)] for _ in range(MAP_H)]

def load_tile_images():
    global tile_images, seed_image, sprout_image, mid_image, crop_image

    tile_images = {
        0: load_image('a_grass.png'),
        1: load_image('a_grass_rock.png'),
        2: load_image('brown.png'),   # 갈아놓은 밭
        3: load_image('water_ground.png')   # 물 뿌린 밭
    }

    seed_image = load_image('seed.png')  # 1단계
    sprout_image = load_image('farm_cabbage01.png')  # 2단계
    mid_image = load_image('farm_cabbage02.png')  # 3단계 중간풀
    crop_image = load_image('farm_cabbage03.png')  # 4단계 완성작물


# 타일 맵 그리기
def draw_tile_map():
    for y in range(MAP_H):
        for x in range(MAP_W):
            tile_num = tile_map[y][x]
            # 현재 타일 중심 좌표 계산함
            px = (x * tile) + 20
            py = ((MAP_H - y) * tile) - 40
            if tile_num in tile_images:
                tile_images[tile_num].draw((x * tile) + 20,
                                           ((MAP_H - y) * tile) - 40,
                                           tile, tile)

            # 씨앗이 있는 경우 씨앗 이미지 그리기
            if seed_map[y][x] == 1:
                seed_image.draw((x * tile) + 20,
                                ((MAP_H - y) * tile) - 40,
                                20, 20)  # 적당한 크기

            # 씨앗 단계: 0 없음 / 1 씨앗 / 2 새싹 / 3 중간풀 / 4 작물
            stage = seed_map[y][x]

            if stage == 1:
                seed_image.draw(px, py, 20, 20)

            elif stage == 2:
                sprout_image.draw(px, py+10, 60,60)

            elif stage == 3:
                mid_image.draw(px, py+15,80, 80)

            elif stage == 4:
                crop_image.draw(px, py+15, 80, 80)


# 타일 변경(땅 → 밭 만들기)
def change_tile(tx, ty):
    if 0 <= tx < MAP_W and 0 <= ty < MAP_H:
        tile_map[ty][tx] = 2


# 씨앗 심기 함수
def plant_seed(tx, ty):
    if tile_map[ty][tx] == 2:
        seed_map[ty][tx] = 1    # 씨앗
        seed_timer[ty][tx] = 0  # 시간 0부터 시작
        return True
    else:
        print("씨앗은 갈아놓은 밭에만 심을 수 있습니다.")
        return False

# 물 뿌리기 함수
def water_tile(tx, ty):
    if tile_map[ty][tx] == 2 or tile_map[ty][tx] == 3:
        water_map[ty][tx] = 1
        tile_map[ty][tx] = 3
    else:
        print("물은 씨앗이 심어진 밭에만 뿌릴 수 있습니다.")


GROW_TIME_STAGE = {
    1: 5.0,
    2: 7.0,
    3: 10.0
}

def update_seed_growth(dt):
    for y in range(MAP_H):
        for x in range(MAP_W):
            stage = seed_map[y][x]

            # 0 = 아무것도 없음 -> 패스
            if stage == 0:
                continue

            # 4 = 작물 완성 -> 더 성장 안 함
            if stage == 4:
                continue

            if water_map[y][x] == 0:
                continue

            seed_timer[y][x] += dt

            required_time = GROW_TIME_STAGE.get(stage, None)
            if required_time is None:
                continue

            if seed_timer[y][x] >= required_time:
                seed_map[y][x] += 1        # 다음단계
                seed_timer[y][x] = 0       # 타이머 초기화

def harvest(tx, ty):

    if seed_map[ty][tx] == 4:
        print("작물 수확!")

        play_mode.inventory.add_item("farm_cabbage03.png")

        seed_map[ty][tx] = 0       # 작물 제거
        seed_timer[ty][tx] = 0     # 타이머 초기화
        water_map[ty][tx] = 0      # 물 상태 초기화
        tile_map[ty][tx] = 0     # 땅으로 복구
        return True
    return False
