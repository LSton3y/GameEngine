from engine.core.game import Game


def get_current_scene():
    """Returns the current active scene"""
    return Game.instance().scene_manager.current_scene


def get_current_scene_index():
    """Returns the index of the current active scene"""
    return Game.instance().scene_manager.scenes.index(get_current_scene())


def load_scene(index: int):
    """Loads a scene based on index"""
    Game.instance().scene_manager.change_scene_index(index)


def create_scene():
    """Creates a new scene"""
    pass


def remove_scene(index: int):
    """Removes a scene based on index"""
    pass
