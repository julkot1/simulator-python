from entity.plant.Plant import Plant


class Dandelion(Plant):
    def __init__(self, position, world):
        super().__init__("Dandelion", "D", "yellow", 0, position, world)

    def new_object(self, position, world):
        return Dandelion(position, world)

    def action(self):
        super().action()
        super().action()
        super().action()

