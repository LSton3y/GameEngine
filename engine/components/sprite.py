from engine.rendering.renderer import load_sprite_image


class Sprite:
    """
    Handles the visual representation of an entity
    Attributes:
        image (pygame.Surface): Pygame surface rendering sprite image
    """

    def __init__(self, context, image_path="assets/sprites/scratch-cat.png"):
        self.image = context.assets.load_image(image_path)