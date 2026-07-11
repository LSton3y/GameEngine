import pygame


class AssetManager:
    """
    Handles the loading of assets
    """
    _instance = None

    def __init__(self):
        self._images = {} # Caches loaded images (path -> Surface)
        self._sounds = {} # Caches loaded sounds (path -> Sound)

        # Handles singleton logic
        if AssetManager._instance is not None:
            raise ValueError("AssetManger instance already exists.")
        else:
            AssetManager._instance = self
    

    # Loads and caches image
    def load_image(self, image_path: str) -> pygame.Surface:
        if image_path not in self._images:
            self._images[image_path] = pygame.image.load(image_path).convert_alpha()
        
        return self._images[image_path]


    # Loads and caches sounds
    def load_sound(self, sound_path: str) -> pygame.mixer.Sound:
        pass # TODO: Make sound logic

    
    @staticmethod
    def get_instance():
        if AssetManager._instance is None:
            AssetManager._instance = AssetManager()
        return AssetManager._instance
