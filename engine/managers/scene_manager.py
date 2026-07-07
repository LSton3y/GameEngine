from engine.core.scene import Scene
from engine.core.singleton import SingletonMeta


class SceneManager(metaclass=SingletonMeta):
    """
    Stores all the scenes

    Controls which scenes are currently active
    """

    def __init__(self):
        # Stores all the scenes
        self._scenes = [Scene()]
        # Stores the current scene
        self._current_scene = self._scenes[0]
    

    def change_scene_index(self, index) -> None:
        # If scene index exists, change active scene
        if index < len(self._scenes):
            self._current_scene = self._scenes[index]
        else:
            return IndexError("Scene index does not exist.")
    

    @property
    def current_scene(self):
        return self._current_scene
