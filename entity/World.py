from functools import cmp_to_key

from Logger import Logger
from entity.Entity import Entity


class World:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.entities = []
        self.turn = 0
        self.logger = Logger()
        self.human = None

    def add_entity(self, entity):
        self.entities.append(entity)
        self.entities = sorted(self.entities, key=cmp_to_key(Entity.compare))

    def next_turn(self, map):
        self.turn += 1
        for entity in self.entities:
            entity.age += 1
            if entity.alive:
                entity.action()
        for entity in self.entities:
            entity.update_tile(map)
        if self.human is not None:
            if not self.human.alive:
                self.human = None
        self.entities = [x for x in self.entities if x.alive]

    def get_entity(self, position):
        for entity in self.entities:
            if entity.position.x == position.x and entity.position.y == position.y:
                return entity
        return None
