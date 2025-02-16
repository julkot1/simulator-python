from entity.animal.Animal import Animal
from entity.plant.Plant import Plant


class Hogweed(Plant):
    def __init__(self, position, world):
        super().__init__("Hogweed", "H", "darkGreen", 10, position, world)

    def new_object(self, position, world):
        return Hogweed(position, world)

    def action(self):
        super().action()
        neighbours = self.position.get_neighbors(self.world)
        for neighbour in neighbours:
            entity = self.world.get_entity(neighbour)
            if entity is not None:
                if isinstance(entity, Animal):
                    if not entity.defend_poison():
                        entity.alive = False
                        self.world.logger.append(f"[turn {self.world.turn}]: kills {self} -> {entity}")

