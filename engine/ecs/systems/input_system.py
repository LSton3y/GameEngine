import pygame

from engine.ecs.systems.base_system import BaseSystem
from engine.managers.input_manager import InputManager
from engine.core.singleton import SingletonMeta


class InputSystem(BaseSystem, metaclass=SingletonMeta):
    """
    Handles input actions
    """

    def __init__(self):
        self._action_map = {
            "up": [pygame.K_w, pygame.K_UP],
            "down": [pygame.K_s, pygame.K_DOWN],
            "left": [pygame.K_a, pygame.K_LEFT],
            "right": [pygame.K_d, pygame.K_RIGHT],
            "jump": [pygame.K_SPACE],
        }

    # Checks if action is down
    def is_action_down(self, action: str) -> bool:
        keys = self._action_map.get(action, [])
        input_mgr = InputManager.instance()
        return any(input_mgr.is_key_down(k) for k in keys)

    # Checks if action is pressed
    def is_action_pressed(self, action: str) -> bool:
        keys = self._action_map.get(action, [])
        input_mgr = InputManager.instance()
        return any(input_mgr.is_key_pressed(k) for k in keys)

    # Checks if action is released
    def is_action_released(self, action: str) -> bool:
        keys = self._action_map.get(action, [])
        input_mgr = InputManager.instance()
        return any(input_mgr.is_key_released(k) for k in keys)