import pygame
from engine.core.singleton import Singleton


class AssetManager(Singleton):
    """
    Handles the loading of assets
    """

    def __init__(self):
        super().__init__(AssetManager)
        self._images = {} # Caches loaded images (path -> Surface)
        self._sounds = {} # Caches loaded sounds (path -> Sound)
    

    # Loads and caches image
    def load_image(self, image_path: str) -> pygame.Surface:
        if image_path not in self._images:
            self._images[image_path] = pygame.image.load(image_path).convert_alpha()
        
        return self._images[image_path]


    # Loads and caches sounds
    def load_sound(self, sound_path: str) -> pygame.mixer.Sound:
        pass # TODO: Make sound logic
