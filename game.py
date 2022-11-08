from typing import List, Union
import pygame
from pygame import Surface, Rect
from entity import Entity
from entity_container import EntityContainer
from middlewares.collision_middleware import CollisionMiddleware
from moving_circle import MovingCircle

entity_template = [
    Rect(50, 50, 100, 100),
    Rect(100, 50, 100, 100),
    Rect(150, 50, 100, 100),
    Rect(200, 50, 100, 100),
    Rect(300, 50, 100, 100),
    MovingCircle(velocity=pygame.Vector2(1, 0)),
    MovingCircle(rect=Rect(500, 0, 50, 100), velocity=pygame.Vector2(-1, 0)),
]


class Game:
    entities = EntityContainer()
    surface: Surface = None

    collisions: CollisionMiddleware = None

    @classmethod
    def init(cls, surface: Surface):
        cls.surface = surface
        cls.collisions = CollisionMiddleware(cls)
        cls.__init_entities(entity_template)

    @classmethod
    def main_loop(cls, delta_time: float):
        cls.collisions.process()

        for entity in cls.entities.get_entities():

            if isinstance(entity, Entity):
                entity.update(delta_time)
                entity.render()
            else:
                pygame.draw.rect(cls.surface, (255, 0, 0), entity)

        pygame.display.flip()

    @classmethod
    def __init_entities(cls, entities: List[Union[Entity, Rect]]):
        for entity in entities:
            cls.entities.add_entity(entity)

            if isinstance(entity, Entity):
                entity.begin_play()
