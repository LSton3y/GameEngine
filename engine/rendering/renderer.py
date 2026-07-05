# Renderer class
# Handles the rendering of the screen and sprites
import pygame


class Renderer:

    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))

    
    def clear(self):
        self.screen.fill((255, 255, 255))

    
    def draw_sprite(self, transform, sprite):
        rotated = pygame.transform.rotate(sprite.image, -transform.rotation)
        rect = rotated.get_rect(center=transform.position.to_tuple())
        self.screen.blit(rotated, rect)
    
    def present(self):
        pygame.display.flip()


def load_sprite_image(image_path):
    return pygame.image.load(image_path).convert_alpha()

