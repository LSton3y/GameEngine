import pygame
import engine.core.game as g

from engine.rendering.window import Window


class InputManager:
    """
    Handles user input and window functions (like QUIT, resize, etc.)
    """
    
    def __init__(self):
        self._keys_down = set()
        self._keys_pressed = set()
        self._keys_released = set()

        self._mouse_buttons_down = set()
        self._mouse_buttons_pressed = set()
        self._mouse_buttons_released = set()
     

    def poll(self):
        self._keys_pressed.clear()
        self._keys_released.clear()

        self._mouse_buttons_pressed.clear()
        self._mouse_buttons_released.clear()

        window = g.Game.instance().window


        for event in pygame.event.get():
            # Check if window has been closed
            if event.type == pygame.QUIT:
                window.close()

            # Check if window has been resized
            elif event.type == pygame.VIDEORESIZE:
                window.resize(event.w, event.h) 
            
            # Check if key down
            elif event.type == pygame.KEYDOWN:
                self._keys_down.add(event.key)
                self._keys_pressed.add(event.key)
            
            # Check if key up
            elif event.type == pygame.KEYUP:
                self._keys_down.discard(event.key)
                self._keys_released.add(event.key)
            
            # Check if mouse down
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._mouse_buttons_down.add(event.button)
                self._mouse_buttons_pressed.add(event.button)
            
            elif event.type == pygame.MOUSEBUTTONUP:
                self._mouse_buttons_down.discard(event.button)
                self._mouse_buttons_released.add(event.button)
                
    

    # Checks whether a key is down
    def is_key_down(self, key) -> bool:
        return key in self._keys_down

    # Checks whether a key has been pressed
    def is_key_pressed(self, key) -> bool:
        return key in self._keys_pressed

    # Checks whether a key has been released
    def is_key_released(self, key) -> bool:
        return key in self._keys_released
    
    
    # Checks whether a mouse button is down
    def is_mouse_down(self, mouse_button) -> bool:
        return mouse_button in self._mouse_buttons_down

    # Checks whether a mouse button has been pressed
    def is_mouse_pressed(self, mouse_button) -> bool:
        return mouse_button in self._mouse_buttons_pressed

    # Checks whether a mouse button has been released
    def is_mouse_released(self, mouse_button) -> bool:
        return mouse_button in self.mouse_buttons_released