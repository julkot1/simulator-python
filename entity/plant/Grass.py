from entity.plant.Plant import Plant


class Grass(Plant):

    def __init__(self, position, world):
        super().__init__("Grass", "G", "green", 0, position, world)

    def new_object(self, position, world):
        return Grass(position, world)