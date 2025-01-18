from random import randint

class Move:
    def __init__(self, name, damage=50, type='normal', accuracy=100, category='physical'|'special'|'status'):
        self._name = name
        self._damage = damage  # eventually pull data from Poke API
        self._type = type       # eventually pull data from Poke API
        self._accuracy = accuracy   # eventually pull data from Poke API
        self._category = category   # eventually pull data from Poke API

    def _has_hit(self):
        return True if randint(1, 100) <= self._accuracy else False

    