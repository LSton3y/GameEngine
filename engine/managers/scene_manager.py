import json

from engine.core.scene import Scene
from engine.core.singleton import SingletonMeta


class SceneManager(metaclass=SingletonMeta):
    """
    Stores all the scenes

    Controls which scenes are currently active
    """

    def __init__(self):
        # Stores all the scenes
        self._scenes = []
        # Stores the current scene
        self._current_scene = None

    
    # Saves current scene as a json file
    def save(self, path):
        with open(path, "w") as file:
            json.dump(self._current_scene.to_dict(), file, indent=2)
    
    # Loads current scene from json file
    def load(self, path, registry):
        with open(path) as file:
            data = json.load(file)
        
        self._current_scene = Scene.from_dict(data, registry)
    

    def change_scene_index(self, index) -> None:
        # If scene index exists, change active scene
        if index < len(self._scenes):
            self._current_scene = self._scenes[index]
        else:
            return IndexError("Scene index does not exist.")
    

    @property
    def current_scene(self):
        return self._current_scene

    @property
    def scenes(self):
        return self._scenes
