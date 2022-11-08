from typing import List, Union
from pygame import Rect
from entity import Entity
from middlewares.game_middleware import GameMiddleware


class CollisionMiddleware(GameMiddleware):
    def process(self):
        self.__detect_collisions(self.owner.entities.get_entities())

    def __detect_collisions(self, entities: List[Union[Entity, Rect]]):
        for entity in entities:
            if isinstance(entity, Entity):

                for other_entity in entities:
                    if isinstance(other_entity, Entity):
                        if entity.root_rect.colliderect(other_entity.root_rect) and entity != other_entity:
                            entity.on_collide_entity(other_entity)
                            other_entity.on_collide_entity(entity)
                    else:
                        if entity.root_rect.colliderect(other_entity):
                            entity.on_collide_rect(other_entity)



