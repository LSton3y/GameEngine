from engine.rendering.window import Window
from engine.rendering.renderer import Renderer
from engine.managers.asset_manager import AssetManager
from engine.managers.input_manager import InputManager

from engine.core.scene import Scene
from engine.components.transform import Transform
from engine.components.sprite import Sprite


class Game:
    """
    Handles the main game loop and processes
    """

    def __init__(self):
        Window(800, 600, "My Game")
        Renderer(Window.instance().surface)
        AssetManager()
        InputManager()

        self.scene = Scene()
    

    def run(self):
        window = Window.instance()
        renderer = Renderer.instance()
        input = InputManager.instance()


        while window.is_open:
            # Update functions
            dt = window.tick()
            input.poll(window)
            self.update(dt)

            # Checks if window is stil open after input poll
            if not window.is_open:
                break

            # Render functions
            renderer.clear()
            self.render()
            renderer.update()
    

    # Handles main update loop
    def update(self, dt):
        for entity in self.scene.entities:
            entity.get_component(Transform).rotation += 50 * dt


    # Handles rendering
    def render(self):
        for entity in self.scene.entities:
            Renderer.instance().draw_sprite(entity.get_component(Transform), entity.get_component(Sprite))