# Sprite class
from engine.rendering.renderer import load_sprite_image


class Sprite:

    def __init__(self, image_path="assets/sprites/scratch-cat.png"):
        self.image = load_sprite_image(image_path)