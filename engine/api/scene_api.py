from engine.core.game import Game


def current_scene():
    """Returns the current active scene"""
    return Game.instance().scene_manager.current_scene


def current_scene_index():
    """Returns the index of the current active scene"""
    return Game.instance().scene_manager.scenes.index(current_scene())


def save():
    """Saves the current active scene"""
    # TODO: Change save path to variable
    Game.instance().scene_manager.save(f"game/scenes/scene{current_scene_index()}.json")


def load(index: int):
    """Loads a scene based on index"""
    Game.instance().scene_manager.change_scene_index(index)
    Game.instance().load()


def load_current_scene():
    """Loads the current scene"""
    Game.instance().load()


def create(name: str):
    """Creates a new scene and returns it"""
    return Game.instance().scene_manager.add_scene(name)


def remove(index: int):
    """Removes a scene based on index"""
    Game.instance().scene_manager.remove_scene(index)
