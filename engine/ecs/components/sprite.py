from engine.managers.asset_manager import AssetManager
from engine.ecs.components.component import Component


class Sprite(Component):
    """
    Handles the visual representation of an entity
    Attributes:
        image_path (str): Stores the image path
        image (pygame.Surface): Pygame surface rendering sprite image
    """
    _exclude = {"image"}


    def __init__(self, image_path: str="game/assets/sprites/scratch-cat.png"):
        self.image_path = image_path
        self.image = AssetManager.instance().load_image(image_path)
    

    # Returns class created from dict properties
    @classmethod
    def from_dict(cls, data, entity=None):
        return cls(**data)