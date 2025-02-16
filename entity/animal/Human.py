from entity.Position import Direction, Position
from entity.animal.Animal import Animal
from entity.plant.Plant import Plant


class Human(Animal):
    def new_object(self, position, world):
        return Human(position, world)

    def __init__(self, position, world):
        super(Human, self).__init__("Human", "H", "cyan", 5, 4, position, world)
        self.direction = Direction.NORTH
        self.cooldown = 0
        self.is_active = False
        self.active = 5

    def update_ult(self):
        if not self.is_active and self.cooldown < 5:
            self.cooldown += 1
        if self.is_active:
            self.active -= 1
            self.ult()
            if self.active == 0:
                self.is_active = False
                self.cooldown = 0
                self.active = 5

    def ult(self):
        neighbours = self.position.get_neighbors(self.world)
        for neighbour in neighbours:
            entity = self.world.get_entity(neighbour)
            if entity is not None:
                self.world.logger.append(f"[turn {self.world.turn}]: kills {self} -> {entity}")
                entity.alive = False

    def action(self):
        self.update_ult()
        self.prev_pos = Position(self.position.x, self.position.y)
        new_pos = Position(self.position.x, self.position.y)
        new_pos.translate(self.direction, self.world)

        entity = self.world.get_entity(new_pos)

        if entity is not None:
            if isinstance(entity, Plant):
                entity.collision(self)
            else:
                self.collision(entity)
        else:
            self.position = new_pos


