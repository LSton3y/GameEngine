from engine.rendering.window import Window
from engine.rendering.renderer import Renderer
from engine.managers.asset_manager import AssetManager
from engine.managers.input_manager import InputManager


class Context:
    """
    Central service locator. Holds references to engine-wide singletons
    (managers) so systems/scenes don't need long constructor argument lists.
    Attributes:
        window (Window): Window class
        renderer (Renderer): Renderer class
        assets (AssetManager): AssetManager class
        input (InputManager): InputManager class
    """

    def __init__(self, window, renderer, asset_manager, input_manager):
        self.window: Window = window
        self.renderer: Renderer = renderer
        self.assets: AssetManager = asset_manager
        self.input: InputManager = input_manager