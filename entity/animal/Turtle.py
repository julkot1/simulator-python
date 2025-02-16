import random

from entity.animal.Animal import Animal


class Turtle(Animal):
    def __init__(self, position, world):
        super().__init__("Turtle", "T", "darkGreen", 2, 1, position, world)

    def new_object(self, position, world):
        return Turtle(position, world)

    def action(self):
        if random.randint(0, 4) == 0:
            super().action()

    def defend_attack(self, entity):
        if random.randint(0, 2) == 0:
            return False
        if isinstance(entity, Animal):
            if entity.damage < 5:
                return True
