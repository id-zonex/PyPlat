import abc


class GameMiddleware:
    def __init__(self, owner):
        self.owner = owner

    def process(self):
        ...

