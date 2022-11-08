from typing import List, Union
import pygame
from pygame import Surface, Rect
from entity import Entity
from entity_container import EntityContainer
from moving_circle import MovingCircle

entity_template = [
    Rect(50, 50, 100, 100),
    Rect(100, 50, 100, 100),
    Rect(150, 50, 100, 100),
    Rect(200, 50, 100, 100),
    Rect(300, 50, 100, 100),
    MovingCircle(),
    MovingCircle(position=pygame.Vector2(100, 0)),
    MovingCircle(position=pygame.Vector2(200, 0)),
    MovingCircle(position=pygame.Vector2(100, 100)),
    MovingCircle(position=pygame.Vector2(200, 50)),
    MovingCircle(position=pygame.Vector2(100, 100)),
    MovingCircle(position=pygame.Vector2(200, 50)),
]


class Game:
    entities = EntityContainer()
    surface: Surface = None

    @classmethod
    def init(cls, surface: Surface):
        cls.surface = surface
        cls.__init_entities(entity_template)

    @classmethod
    def main_loop(cls, delta_time: float):
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
