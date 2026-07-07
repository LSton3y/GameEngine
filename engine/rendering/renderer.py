import pygame
from engine.core.singleton import SingletonMeta


class Renderer(metaclass=SingletonMeta):
    """
    Handles the rendering of the screen
    """
    
    # Fills screen with color
    def clear(self, screen, color=(255, 255, 255)):
        screen.fill(color)

    
    # Draws sprite
    def draw_sprite(self, screen, transform, sprite):
        # Handles rotation and scale of sprite
        image = pygame.transform.scale_by(sprite.image, (transform.scale.x, transform.scale.y))
        image = pygame.transform.rotate(image, -transform.rotation)

        # Handles position of sprite
        rect = image.get_rect(center=transform.position.to_tuple())

        screen.blit(image, rect)
    

    # Updates display
    def update(self):
        pygame.display.flip()

