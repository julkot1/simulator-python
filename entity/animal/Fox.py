import random

from entity.animal.Animal import Animal


class Fox(Animal):
    def __init__(self, position, world):
        super(Fox, self).__init__("Fox", "F", "orange", 3, 7, position, world)

    def new_object(self, position, world):
        return Fox(position, world)

    def action(self):
        neighbours = self.position.get_neighbors(self.world)
        counter = 0
        pos = None
        found = False
        while counter != len(neighbours):
            counter += 1
            pos = random.choice(neighbours)
            e = self.world.get_entity(pos)
            if e is None:
                found = True
                break
            elif e.damage < self.damage or self.entity_type == e.entity_type:
                found = True
                break

        if found:
            entity = self.world.get_entity(pos)

            if entity is not None:
                self.collision(entity)
            else:
                self.position = pos



