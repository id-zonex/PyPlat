from typing import List, Any, Union
from entity import Entity
from pygame import Rect


class EntityContainer:
    def __init__(self):
        self.entities: List[Union[Entity, Rect]] = list()

    def add_entity(self, entity: Union[Entity, Rect]):
        self.entities.append(entity)

    def get_entities(self) -> List[Union[Entity, Rect]]:
        return self.entities

