import abc


class Entity(abc.ABC):
    @abc.abstractmethod
    def begin_play(self):
        ...

    @abc.abstractmethod
    def update(self, delta_time: float):
        ...

    @abc.abstractmethod
    def render(self):
        ...
