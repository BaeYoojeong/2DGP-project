from pico2d import *

# 속도
PIXEL_PER_METER = (10.0 / 0.3)   # 10 pixel = 30 cm
RUN_SPEED_KMPH = 10.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)  # 초당 픽셀 이동 속도

# 애니메이션
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 4


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

    def update(self, frame_time):
        # 이동 거리 계산
        distance = RUN_SPEED_PPS * frame_time
        # 애니메이션 프레임 업데이트
        self.frame = (self.frame +
                      FRAMES_PER_ACTION * ACTION_PER_TIME * frame_time) % FRAMES_PER_ACTION

        if self.dir != 0 or self.updown != 0:
            self.x += self.dir * distance
            self.y += self.updown * distance
            self.last_dir = self.dir
            self.last_updown = self.updown

    def draw(self):
        f = int(self.frame)

        if self.updown == 1:
            self.image.clip_draw(f * 16, 32, 16, 32, self.x, self.y, self.character_x, self.character_y)
        elif self.updown == -1:
            self.image.clip_draw(f * 16, 96, 16, 32, self.x, self.y, self.character_x, self.character_y)
        elif self.dir == 1:
            self.image.clip_draw(f * 16, 64, 16, 32, self.x, self.y, self.character_x, self.character_y)
        elif self.dir == -1:
            self.image.clip_draw(f * 16, 0, 16, 32, self.x, self.y, self.character_x, self.character_y)
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
