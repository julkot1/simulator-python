from entity.Position import Position, Direction
from entity.animal.Animal import Animal
from entity.plant.Hogweed import Hogweed
from entity.plant.Plant import Plant


class CyberSheep(Animal):
    def __init__(self, position, world):
        super(CyberSheep, self).__init__("CyberSheep", "C", "magenta", 11, 4, position, world)

    def find_hogweed(self):
        pos = Position(-1, -1)
        distance = float("inf")

        for entity in self.world.entities:
            if isinstance(entity, Hogweed):
                new_distance = self.position.distance(entity.position)
                if new_distance < distance:
                    distance = new_distance
                    pos = entity.position
        return pos

    def defend_poison(self):
        return True

    def action(self):
        new_pos = self.find_hogweed()
        if new_pos.x == -1 and new_pos.y == -1:
            super().action()
        else:
            direction = self.get_direction(new_pos)
            self.random_direction()
            new_pos = Position(self.position.x, self.position.y)
            new_pos.translate(direction, self.world)

            entity = self.world.get_entity(new_pos)

            if entity is not None:
                if isinstance(entity, Plant):
                    entity.collision(self)
                else:
                    self.collision(entity)
            else:
                self.position = new_pos

    def attack(self, entity):
        if isinstance(entity, Hogweed):
            self.position = entity.position
            entity.alive = False
            self.world.logger.append(f"[turn {self.world.turn}]: kills {self} -> {entity}")
        else:
            super().attack(entity)

    def new_object(self, position, world):
        return CyberSheep(position, world)

    def get_direction(self, new_pos):
        directions = [Direction.SOUTH, Direction.WEST, Direction.EAST, Direction.NORTH]
        new_direction = None
        dis = float("inf")
        for direction in directions:
            new_distance = self.position.distance(new_pos)
            if (direction == Direction.WEST or direction == Direction.EAST) and new_pos.x == self.position.x:
                continue
            if (direction == Direction.NORTH or direction == Direction.SOUTH) and new_pos.y == self.position.y:
                continue
            if new_distance < dis:
                dis = new_distance
                new_direction = direction
        return new_direction
