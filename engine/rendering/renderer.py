import pygame


class Renderer:
    """
    Handles the rendering of the screen
    """

    def __init__(self, window):
        self.window = window

    
    def clear(self, color=(255, 255, 255)):
        self.window.fill(color)

    
    def draw_sprite(self, transform, sprite):
        rotated = pygame.transform.rotate(sprite.image, -transform.rotation)
        rect = rotated.get_rect(center=transform.position.to_tuple())
        self.window.blit(rotated, rect)
    
    def update(self):
        pygame.display.flip()

