from engine.rendering.window import Window
from engine.rendering.renderer import Renderer

from engine.managers.asset_manager import AssetManager
from engine.managers.input_manager import InputManager
from engine.managers.scene_manager import SceneManager
from engine.managers.system_manager import SystemManager


class Game:
    """
    Handles the main game loop and processes
    """

    def __init__(self):
        # Singleton initialisations
        Window(800, 600, "My Game")
        Renderer()

        AssetManager()
        InputManager()
        SceneManager()
        
        self.system_manager = SystemManager()
    

    def run(self):
        window = Window.instance()
        renderer = Renderer.instance()
        input_manager = InputManager.instance()

        SceneManager.instance().load("game/scenes/scene1.json")
        self.system_manager.start()


        while window.is_open:
            # Update functions
            dt = window.tick()
            input_manager.poll()

            # Checks if window is stil open after input poll
            if not window.is_open:
                break

            # Update functions
            renderer.clear()
            self.update(dt)
            renderer.update()
    


    # Handles main update loop
    def update(self, dt):
        self.system_manager.update(dt)
                