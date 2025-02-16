import random
from abc import ABC, abstractmethod

from entity.Entity import Entity
from entity.Position import Direction, Position
from entity.plant.Plant import Plant


class Animal(Entity, ABC):
    def __init__(self, entity_type, symbol, color, damage, priority, position, world, age=0):
        super(Animal, self).__init__(entity_type, symbol, color, damage, priority, position, world, age)

    def action(self):
        self.prev_pos = Position(self.position.x, self.position.y)
        d = self.random_direction()
        new_pos = Position(self.position.x, self.position.y)
        new_pos.translate(d, self.world)

        entity = self.world.get_entity(new_pos)

        if entity is not None:
            if isinstance(entity, Plant):
                entity.collision(self)
            else:
                self.collision(entity)
        else:
            self.position = new_pos

    def defend_poison(self):
        return False

    def attack(self, entity):
        if not entity.alive:
            return
        if isinstance(entity, Animal):
            if entity.defend_attack(self):
                self.world.logger.append(f"[turn {self.world.turn}]: {entity} defend attack {self} ")
                return

        if entity.damage > self.damage:
            self.world.logger.append(f"[turn {self.world.turn}]: kills {entity} -> {self}")
            self.alive = False
        else:
            self.world.logger.append(f"[turn {self.world.turn}]: kills {self} -> {entity}")
            self.position = entity.position
            entity.alive = False

    def defend_attack(self, entity):
        return False

    def reproduce(self, entity):

        neighbours = self.position.get_neighbors(self.world) + entity.position.get_neighbors(self.world)
        counter = 0
        pos = None
        found = False
        while counter != len(neighbours):
            counter += 1
            pos = random.choice(neighbours)
            if self.world.get_entity(pos) is None:
                found = True
                break
        if found:
            new_entity = self.new_object(pos, self.world)
            self.world.logger.append(f"[turn {self.world.turn}]: reproduce {self} and {entity} -> {new_entity}")
            self.world.add_entity(new_entity)

    @abstractmethod
    def new_object(self, position, world):
        pass

    def collision(self, entity):
        if self.entity_type == entity.entity_type:
            self.reproduce(entity)
        else:
            self.attack(entity)
