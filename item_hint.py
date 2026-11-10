from pico2d import get_canvas_height, load_image


class ItemHint:
    def __init__(self):
        self.image = load_image('item_hint.png')

    def draw(self):
        self.image.draw(10 + self.image.w // 2,
                        get_canvas_height() - 10 - self.image.h // 2)

    def update(self):
        pass
