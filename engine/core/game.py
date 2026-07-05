from engine.rendering.window import Window
from engine.rendering.renderer import Renderer
from engine.managers.asset_manager import AssetManager
from engine.managers.input_manager import InputManager


class Game:

    def __init__(self):
        self.window = Window(800, 600, "My Game")
        self.renderer = Renderer(self.window.surface)
        self.assets = AssetManager()
        self.input = InputManager()

        self.context = self.context(self.window, self.renderer, self.assets, self.input)
    

    def run(self):
        while self.window.is_open:
            # Update functions
            dt = self.window.tick()
            # TODO: Add input managing
            self.update()

            # Render functions
            self.renderer.clear()
            self.render()
            self.renderer.update()
    

    # Handles main update loop
    def update(self):
        pass


    # Handles rendering
    def render(self):
        pass