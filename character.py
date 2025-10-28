from pico2d import load_image


class arang:
    def __init__ (self):
        self.x, self.y = 16, 32
        self.frame = 4
        self.face_dir = 1
        self.image = load_image('arang.png')

        def draw(self):
            if self.face_dir == 1:
                self.image.clip_draw(self.frame * 16, 32, 16, 16, self.x, self.y)