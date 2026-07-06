import pygame
from engine.core.singleton import SingletonMeta


class Window(metaclass=SingletonMeta):
    """
    Handles the attributes of the window
    """

    def __init__(self, width=800, height=600, title="My Engine", fullscreen=False, vsync=True, target_fps=60):
        # Pygame initialisation
        pygame.init()
        pygame.display.set_caption(title)

        # Window attributes
        self.width = width
        self.height = height
        self.title = title
        self.fullscreen = fullscreen
        self.target_fps = target_fps

        # Window flags
        flags = pygame.RESIZABLE
        if fullscreen:
            flags |= pygame.FULLSCREEN
        
        # Pygame classes
        self.surface = pygame.display.set_mode((width, height), flags, vsync=vsync)
        self.clock = pygame.time.Clock()
        self._running = True
    

    @classmethod


    @property
    def size(self):
        return (self.width, self.height)
    
    @property
    def is_open(self):
        return self._running
    

    # Sets window icon
    def set_icon(self, icon_path: str, context):
        icon = context.assets.load_image(icon_path)
        pygame.display.set_icon(icon)
    
    # Sets window title
    def set_title(self, title: str):
        self.title = title
        pygame.display.set_caption(title)

    
    # Toggles fullscreen
    def toggle_fullscreen(self):
        self.fullscreen = not self.fullscreen
        flags = pygame.RESIZABLE | (pygame.FULLSCREEN if self.fullscreen else 0)
        self.surface = pygame.display.set_mode((self.width, self.height), flags)
    

    # Resizes window
    def resize(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode((width, height), pygame.RESIZABLE)


    # Advances the clock and returns delta time
    def tick(self) -> float:
        return self.clock.tick(self.target_fps) / 1000.0

    # Returns fps
    def get_fps(self) -> float:
        return self.clock.get_fps()
    

    # Closes the window
    def close(self):
        self._running = False
        pygame.quit()