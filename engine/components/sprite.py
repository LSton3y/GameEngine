class Sprite:
    """
    Handles the visual representation of an entity
    Attributes:
        image (pygame.Surface): Pygame surface rendering sprite image
    """

    def __init__(self, image_path: str="assets/sprites/scratch-cat.png"):
        self.image_path = image_path
        self.image = None # Resolved by render system