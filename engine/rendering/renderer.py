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
        # Handles rotation and scale of sprite
        image = pygame.transform.scale_by(sprite.image, (transform.scale.x, transform.scale.y))
        image = pygame.transform.rotate(image, -transform.rotation)

        # Handles position of sprite
        rect = image.get_rect(center=transform.position.to_tuple())

        self.window.blit(image, rect)
    

    # Updates display
    def update(self):
        pygame.display.flip()

