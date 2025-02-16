from abc import ABC, abstractmethod
import random

from entity.Position import Direction
from view.sim.Tile import Tile





class Entity(ABC):
    def __init__(self, entity_type, symbol, color, damage, priority, position, world, age=0):
        self.entity_type = entity_type
        self.symbol = symbol
        self.color = color
        self.damage = damage
        self.priority = priority
        self.position = position
        self.world = world
        self.age = age
        self.alive = True
        self.tile = None
        self.prev_pos = None

    def create_tile(self, parent):
        self.tile = Tile(self.symbol, self.color, self.position.x, self.position.y, parent)
        self.tile.show()

    def update_tile(self, parent):
        if self.alive and self.tile is None:
            self.create_tile(parent)
        if not self.alive and self.tile is not None:
            self.tile.hide()
            self.tile.deleteLater()
            self.tile = None
        elif self.alive and self.tile is not None:
            self.tile.update_position(self.position)

    def random_direction(self):
        return random.choice(list(Direction))

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self, entity):
        pass

    def __str__(self):
        return f"{self.entity_type}, {self.position}: damage={self.damage}, age={self.age}"

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def compare(entity1, entity2):
        if entity1.priority == entity2.priority:
            return entity2.age - entity1.age
        return entity2.priority - entity1.priority
