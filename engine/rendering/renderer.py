# Renderer class
# Handles the rendering of the screen and sprites
import pygame


class Renderer:

    def __init__(self, screen):
        self.screen = screen

    
    def clear(self, color=(255, 255, 255)):
        self.screen.fill(color)

    
    def draw_sprite(self, transform, sprite):
        rotated = pygame.transform.rotate(sprite.image, -transform.rotation)
        rect = rotated.get_rect(center=transform.position.to_tuple())
        self.screen.blit(rotated, rect)
    
    def update(self):
        pygame.display.flip()

