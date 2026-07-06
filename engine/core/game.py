from engine.rendering.window import Window
from engine.rendering.renderer import Renderer
from engine.managers.asset_manager import AssetManager
from engine.managers.input_manager import InputManager


class Game:
    """
    Handles the main game loop and processes
    """

    def __init__(self):
        Window(800, 600, "My Game")
        Renderer(Window.instance().surface)
        AssetManager()
        InputManager()
    

    def run(self):
        window = Window.instance()
        renderer = Renderer.instance()
        input = InputManager.instance()


        while self.window.is_open:
            # Update functions
            dt = window.tick()
            input.poll(self.window)
            self.update(dt)

            # Render functions
            renderer.clear()
            self.render()
            renderer.update()
    

    # Handles main update loop
    def update(self):
        pass


    # Handles rendering
    def render(self):
        pass