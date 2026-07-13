from engine.ecs.components.script import Script
from engine.math.vector2 import Vector2
from engine.api import *


class PlayerMovement(Script):

    def __init__(self, entity):
        super().__init__(entity)
        self.speed = 300

    
    def update(self, dt):
        movement = Vector2(0, 0)

        if input.action_down("left"):
            movement.x += -1
            self.transform.rotation -= 5
        if input.action_down("right"):
            movement.x += 1
            self.transform.rotation += 5
        if input.action_down("up"):
            movement.y += -1
        if input.action_down("down"):
            movement.y += 1
        if input.action_pressed("reset"):
            scene.load_current_scene()
        
        movement = movement.normalize()

        self.transform.position += movement * self.speed * dt