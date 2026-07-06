import pygame
from engine.core.singleton import SingletonMeta


class Renderer(metaclass=SingletonMeta):
    """
    Handles the rendering of the screen
    """

    def __init__(self, window):
        self.window = window

    
    # Fills screen with color
    def clear(self, color=(255, 255, 255)):
        self.window.fill(color)

    
    # Draws sprite
    def draw_sprite(self, transform, sprite):
        rotated = pygame.transform.rotate(sprite.image, -transform.rotation)
        rect = rotated.get_rect(center=transform.position.to_tuple())
        self.window.blit(rotated, rect)
    

    # Updates display
    def update(self):
        pygame.display.flip()

