from random import random

from entity.Position import Position
from entity.animal.Animal import Animal


class Antelope(Animal):
    def __init__(self, position, world):
        super(Antelope, self).__init__("Antelope", "A", "lightGray", 4, 4, position, world)

    def new_object(self, position, world):
        return Antelope(position, world)

    def action(self):
        self.prev_pos = Position(self.position.x, self.position.y)
        d = self.random_direction()
        new_pos = Position(self.position.x, self.position.y)
        new_pos.translate(d, self.world).translate(d, self.world)

        entity = self.world.get_entity(new_pos)

        if entity is not None:
            self.collision(entity)
        else:
            self.position = new_pos

    def attack(self, entity):
        if random.random() < 0.5:
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
                self.position = pos
            else:
                super().attack(entity)
        else:
            super().attack(entity)
