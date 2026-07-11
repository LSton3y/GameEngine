from engine.rendering.window import Window
from engine.rendering.renderer import Renderer

from engine.managers.asset_manager import AssetManager
from engine.managers.scene_manager import SceneManager
from engine.managers.system_manager import SystemManager

import game.scripts
from engine.scripting.loader import import_package


class Game:
    """
    Handles the main game loop and processes
    """

    def __init__(self):
        # Singleton initalisation
        self.window = Window(800, 600, "My Game")
        self.asset_manager = AssetManager()

        # Class initialisation
        self.renderer = Renderer()

        self.scene_manager = SceneManager()
        self.system_manager = SystemManager()

    

    def run(self):
        import_package(game.scripts)
        SceneManager.instance().load("game/scenes/scene1.json")
        self.system_manager.start()


        while self.window.is_open:
            # Update functions
            dt = self.window.tick()
            self.input_manager.poll()

            # Checks if window is stil open after input poll
            if not self.window.is_open:
                break

            # Update functions
            self.renderer.clear()
            self.update(dt)
            self.renderer.update()
    


    # Handles main update loop
    def update(self, dt):
        self.system_manager.update(dt)
                