from pico2d import *

tree = 64

# 나무 노가다 붙이기
tree_map = [
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0],
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0],
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0],
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0],
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0],
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0],
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0],
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0],
    [0,0,-1,-1,-1,-1,-1,-1,-1,-1,-1,0,0],
]

MAP_H = len(tree_map)
MAP_W = len(tree_map[0])


def load_tree_images():
    global tree_images

    tree_images = {
        0: load_image('tree01_1.png')
    }

def draw_tree_map():
    for y in range(MAP_H):
        for x in range(MAP_W):
            tree_num = tree_map[y][x]
            if tree_num in tree_images:
                tree_images[tree_num].draw((x * tree)+10, (((MAP_H - y) * tree)-10), tree, tree+10)