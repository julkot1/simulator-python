from entity.animal.Animal import Animal


class Sheep(Animal):
    def __init__(self, position, world, age=0):
        super(Sheep, self).__init__("Sheep", "S", "gray", 4, 4, position, world, age)

    def new_object(self, position, world):
        return Sheep(position, world)