from engine.rendering.window import Window
from engine.rendering.renderer import Renderer
from engine.managers.asset_manager import AssetManager
from engine.managers.input_manager import InputManager
from engine.managers.scene_manager import SceneManager

from engine.components.transform import Transform
from engine.components.sprite import Sprite

import math, time


class Game:
    """
    Handles the main game loop and processes
    """

    def __init__(self):
        Window(800, 600, "My Game")
        Renderer(Window.instance().surface)
        AssetManager()
        InputManager()
        SceneManager()
    

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
            sine_pos = math.sin(time.time() * 2) * 5
            entity.get_component(Transform).position.y += sine_pos


    # Handles rendering
    def render(self):
        for entity in self.scene.entities:
            Renderer.instance().draw_sprite(entity.get_component(Transform), entity.get_component(Sprite))