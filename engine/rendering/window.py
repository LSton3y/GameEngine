import pygame

class Window:

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