from pico2d import *

class Arang:
    def __init__(self):
        self.image = load_image('arang.png')
        self.x, self.y = 400, 120
        self.character_x, self.character_y = 50, 100

        self.frame = 0
        self.dir = 0
        self.updown = 0
        self.last_dir = 0
        self.last_updown = 0

    def handle_event(self, event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                self.dir += 1
            elif event.key == SDLK_LEFT:
                self.dir -= 1
            elif event.key == SDLK_UP:
                self.updown += 1
            elif event.key == SDLK_DOWN:
                self.updown -= 1
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                self.dir -= 1
            elif event.key == SDLK_LEFT:
                self.dir += 1
            elif event.key == SDLK_UP:
                self.updown -= 1
            elif event.key == SDLK_DOWN:
                self.updown += 1

    def update(self):
        if self.dir != 0 or self.updown != 0:
            self.frame = (self.frame + 1) % 4
            self.x += self.dir * 10
            self.y += self.updown * 10
            self.last_dir = self.dir
            self.last_updown = self.updown
        else:
            self.frame = 0

    def draw(self):
        if self.updown == 1:
            self.image.clip_draw(self.frame * 16, 32, 16, 32, self.x, self.y, self.character_x, self.character_y)
        elif self.updown == -1:
            self.image.clip_draw(self.frame * 16, 96, 16, 32, self.x, self.y, self.character_x, self.character_y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 16, 64, 16, 32, self.x, self.y, self.character_x, self.character_y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame * 16, 0, 16, 32, self.x, self.y, self.character_x, self.character_y)
        else:
            if self.last_updown == 1:
                self.image.clip_draw(0, 32, 16, 32, self.x, self.y, self.character_x, self.character_y)
            elif self.last_updown == -1:
                self.image.clip_draw(0, 96, 16, 32, self.x, self.y, self.character_x, self.character_y)
            elif self.last_dir == 1:
                self.image.clip_draw(0, 64, 16, 32, self.x, self.y, self.character_x, self.character_y)
            elif self.last_dir == -1:
                self.image.clip_draw(0, 0, 16, 32, self.x, self.y, self.character_x, self.character_y)
            else:
                self.image.clip_draw(0, 96, 16, 32, self.x, self.y, self.character_x, self.character_y)
