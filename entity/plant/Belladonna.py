from entity.plant.Plant import Plant


class Belladonna(Plant):
    def __init__(self, position, world):
        super().__init__("Belladonna", "B", "darkMagenta", 99, position, world)

    def new_object(self, position, world):
        return Belladonna(position, world)

    def collision(self, entity):
        entity.alive = False
        self.alive = False
        self.world.logger.append(f"[turn {self.world.turn}]: kills {self} -> {entity}")
