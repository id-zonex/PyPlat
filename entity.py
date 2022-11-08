from pygame import Rect


class Entity:
    def __init__(self):
        self.root_rect: Rect = Rect(0, 0, 100, 100)

    def begin_play(self):
        ...

    def update(self, delta_time: float):
        ...

    def render(self):
        ...

    def get_collision_rect(self) -> Rect:
        return self.root_rect

    def on_collide_rect(self, rect: Rect):
        ...

    def on_collide_entity(self, entity):
        ...
