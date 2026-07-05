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
        self.window = window
        self.renderer = renderer
        self.assets = asset_manager
        self.input = input_manager