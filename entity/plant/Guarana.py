from entity.plant.Plant import Plant


class Guarana(Plant):
    def __init__(self, position, world):
        super().__init__("Guarana", "G", "darkRed", 0, position, world)

    def collision(self, entity):
        entity.damage += 3
        entity.position = self.position
        self.alive = False
        self.world.logger.append(f"[turn {self.world.turn}]: {self} adds +3 damage to {entity}")

    def new_object(self, position, world):
        return Guarana(position, world)
