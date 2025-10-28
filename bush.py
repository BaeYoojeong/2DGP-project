from pico2d import *

bush = 32*1.7

# 부쉬 노가다 붙이기
bush_map = [
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0],
    [0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0],
    [0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0],
    [0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0],
    [0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0],
    [0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0],
    [0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0],
    [0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0],
    [0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0],
    [0,0,0,0,0,0,0,0,0,0,0]
]

MAP_H = len(bush_map)
MAP_W = len(bush_map[0])


def load_bush_images():
    global bush_images

    bush_images = {
        0: load_image('bush01.png')
    }

def draw_bush_map():
    for y in range(MAP_H):
        for x in range(MAP_W):
            bush_num = bush_map[y][x]
            if bush_num in bush_images:
                bush_images[bush_num].draw((x * bush)+120, (((MAP_H - y) * bush)-20), bush, bush)