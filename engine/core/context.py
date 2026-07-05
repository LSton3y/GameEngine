class Context:
    """
    Central service locator. Holds references to engine-wide singletons
    (managers) so systems/scenes don't need long constructor argument lists.
    """

    def __init__(self, window, renderer, asset_manager, input_manager):
        self.window = window
        self.renderer = renderer
        self.asset_manager = asset_manager
        self.input = input_manager