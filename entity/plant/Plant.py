from abc import ABC, abstractmethod
import random

from entity.Entity import Entity


class Plant(Entity, ABC):
    def __init__(self, entity_type, symbol, color, damage, position, world, age=0):
        super(Plant, self).__init__(entity_type, symbol, color, damage, 0, position, world, age)

    def action(self):
        if random.random() < 0.02:
            self.reproduce()

    def reproduce(self):
        neighbours = self.position.get_neighbors(self.world)
        counter = 0
        pos = None
        found = False
        while len(neighbours) != 0:
            counter += 1
            pos = random.choice(neighbours)
            neighbours.remove(pos)
            e = self.world.get_entity(pos)
            if e is None:
                found = True
                break
        if found:
            new_entity = self.new_object(pos, self.world)
            self.world.logger.append(f"[turn {self.world.turn}]: reproduce {self} -> {new_entity}")
            self.world.add_entity(new_entity)

    def collision(self, entity):
        if self.damage > entity.damage:
            self.world.logger.append(f"[turn {self.world.turn}]: kills {self} -> {entity}")
            entity.alive = False
        else:
            self.world.logger.append(f"[turn {self.world.turn}]: kills {entity} -> {self}")
            self.alive = False
            entity.position = self.position

    @abstractmethod
    def new_object(self, position, world):
        pass
