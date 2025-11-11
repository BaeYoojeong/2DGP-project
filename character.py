from pico2d import *

open_canvas()
character = load_image('arang.png')
frame = 0
running = True
x = 400
y=120
dir = 0
updown = 0
def handle_events():
    global running, dir, updown
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_UP:
                updown += 1
            elif event.key == SDLK_DOWN:
                updown -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                    dir -= 1
            elif event.key == SDLK_LEFT:
                    dir += 1
            elif event.key == SDLK_UP:
                updown -= 1
            elif event.key == SDLK_DOWN:
                updown += 1


while running:
    clear_canvas()
    handle_events()
    if updown == 1:
        character.clip_draw(frame * 16, 32, 16, 32, x, y, 100, 200)
    elif updown == -1:
        character.clip_draw(frame * 16, 96, 16, 32, x, y, 100, 200)
    elif dir == 1:
        character.clip_draw(frame * 16, 64, 16, 32, x, y, 100, 200)
    elif dir == -1:  ㅋ
        character.clip_draw(frame * 16, 0, 16, 32, x, y, 100, 200)
    else:
        if updown == 1:
            character.clip_draw(0, 32, 16, 32, x, y, 100, 200)
        elif updown == -1:
            character.clip_draw(0, 96, 16, 32, x, y, 100, 200)
        elif dir == 1:
            character.clip_draw(0, 64, 16, 32, x, y, 100, 200)
        elif dir == -1:
            character.clip_draw(0, 0, 16, 32, x, y, 100, 200)
        else:
            character.clip_draw(0, 96, 16, 32, x, y, 100, 200)
    update_canvas()
    frame = (frame + 1) % 4
    x += dir * 10
    y += updown *10
    delay(0.1)

close_canvas()