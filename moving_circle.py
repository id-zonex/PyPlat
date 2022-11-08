import pygame.draw
from pygame import Rect, Vector2
from pygame.color import Color
from entity import Entity
import game


class MovingCircle(Entity):
    def __init__(self, rect: Rect = Rect(0, 0, 100, 100), color: Color = (255, 255, 255), velocity: Vector2 = (1, 1)):
        super().__init__()
        self.color = color
        self.root_rect = rect
        self.velocity = velocity

    def begin_play(self):
        ...

    def update(self, delta_time: float):
        self.root_rect.x += self.velocity.x
        self.root_rect.y += self.velocity.y

    def render(self):
        pygame.draw.circle(game.Game.surface, self.color, self.root_rect.center, self.root_rect.width/2)

    def on_collide_entity(self, entity):
        print(entity)
