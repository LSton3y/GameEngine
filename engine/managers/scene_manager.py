import json

from engine.core.scene import Scene


class SceneManager:
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
    def load(self, path):
        with open(path) as file:
            data = json.load(file)
        
        self._current_scene = Scene.from_dict(data)
    

    def change_scene_index(self, index) -> None:
        # If scene index exists, change active scene
        if index < len(self._scenes):
            self._current_scene = self._scenes[index]
        else:
            return IndexError("Scene index does not exist.")
    

    # Adds scene to scene list
    def add_scene(self, name: str) -> Scene:
        scene = Scene()
        self._scenes.append(scene)
        return scene
    
    # Removes scene from scene list
    def remove_scene(self, index: int):
        self._scenes.pop(index)


    @property
    def current_scene(self):
        return self._current_scene

    @property
    def scenes(self):
        return self._scenes
