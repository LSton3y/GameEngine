# Renderer class
# Handles the rendering of the screen and sprites
import pygame


class Renderer:

    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))


def load_sprite_image(self, image_path):
    return pygame.image.load(image_path).convert_alpha()
