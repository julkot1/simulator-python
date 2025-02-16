from entity.animal.Animal import Animal


class Wolf(Animal):
    def __init__(self, position, world):
        super(Wolf, self).__init__("Wolf", "W", "black", 9, 5, position, world)

    def new_object(self, position, world):
        return Wolf(position, world)