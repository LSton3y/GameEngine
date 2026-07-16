from engine.ecs.components.script import Script
from engine.math.vector2 import Vector2
from engine.api import *


class PlayerMovement(Script):

    def __init__(self, entity):
        super().__init__(entity)
        self.speed = 300

    
    def update(self, dt):
        if Input.action_down("left"):
            transform.move(self.entity, -self.speed * dt, 0)
            transform.rotate(self.entity, -5)

        if Input.action_down("right"):
            transform.move(self.entity, self.speed * dt, 0)
            transform.rotate(self.entity, 5)

        if Input.action_down("up"):
            transform.move(self.entity, 0, -self.speed * dt)
            
        if Input.action_down("down"):
            transform.move(self.entity, 0, self.speed * dt)

        if Input.action_pressed("reset"):
            scene.load_current_scene()