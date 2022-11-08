import pygame.draw
from pygame import Vector2
from pygame.color import Color
from entity import Entity
import game


class MovingCircle(Entity):
    def __init__(self, position: Vector2 = Vector2(0, 0), radius: float = 100, color: Color = (255, 255, 255)):
        self.position = position
        self.radius = radius
        self.color = color

    def begin_play(self):
        ...

    def update(self, delta_time: float):
        self.position.x += 1
        self.position.y += 1

    def render(self):
        pygame.draw.circle(game.Game.surface, self.color, self.position, self.radius)
