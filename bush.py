import game_world
from pico2d import *

bush_size = 32 * 1.7
bush_images = {}
bush_list = []

MAP_H = 11
MAP_W = 11

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


class Bush:
    def __init__(self, x, y):
        self.image = bush_images[0]
        self.x, self.y = x, y

    def draw(self):
        self.image.draw(self.x, self.y, bush_size, bush_size)
        if game_world.hitbox:
            draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

    def handle_collision(self, group, other):
        pass


def load_bush_images():
    global bush_images
    bush_images = {0: load_image('bush01.png')}

def create_bushes():
    global bush_list
    bush_list = []
    for y in range(MAP_H):
        for x in range(MAP_W):
            if bush_map[y][x] == 0:
                bx = (x * bush_size) + 120
                by = ((MAP_H - y) * bush_size) - 20
                bush_list.append(Bush(bx, by))

def draw_bush_map():
    for b in bush_list:
        b.draw()
