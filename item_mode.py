from pico2d import *
import game_framework
import game_world
import play_mode
from ball import Ball, BigBall

ITEMS = {SDLK_0: None, SDLK_1: Ball, SDLK_2: BigBall}

image = None

def init():
    global image

    image = load_image('item_select.png')

def finish():
    global image
    del(image)

def update():
    pass

def render():
    clear_canvas()
    game_world.render()
    image.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.pop_mode()
            return
        elif event.type == SDL_KEYDOWN and event.key in ITEMS:
            play_mode.boy.item = ITEMS[event.key]
            game_framework.pop_mode()
            return

def pause():
    pass

def resume():
    pass
