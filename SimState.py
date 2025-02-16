from entity.Position import Position
from entity.World import World
from entity.animal.Human import Human

from entity.Position import Position
from entity.animal.Antelope import Antelope
from entity.animal.CyberSheep import CyberSheep
from entity.animal.Fox import Fox
from entity.animal.Sheep import Sheep
from entity.animal.Turtle import Turtle
from entity.animal.Wolf import Wolf
from entity.plant.Belladonna import Belladonna
from entity.plant.Dandelion import Dandelion
from entity.plant.Grass import Grass
from entity.plant.Guarana import Guarana
from entity.plant.Hogweed import Hogweed

class SimState:
    def __init__(self, world):
        self.world = world

    def save(self, file):
        with open(file, 'w') as f:
            f.write(f"{self.world.width}\n")
            f.write(f"{self.world.height}\n")
            f.write(f"{self.world.turn}\n")
            f.write(f"{len(self.world.entities)}\n")
            for entity in self.world.entities:
                f.write(f"{entity.entity_type}\n")
                f.write(f"{entity.age}\n")
                f.write(f"{entity.damage}\n")
                f.write(f"{entity.position.x}\n")
                f.write(f"{entity.position.y}\n")
                if isinstance(entity, Human):
                    f.write(f"{entity.is_active}\n")
                    f.write(f"{entity.cooldown}\n")
                    f.write(f"{entity.active}\n")

    def load(self, file):
        with open(file, 'r') as f:
            lines = [line.strip() for line in f.readlines()]
            print(lines)
            world = World(int(lines[0]), int(lines[1]))
            world.turn = int(lines[2])
            size = int(lines[3])
            idx = 4
            for i in range(size):
                entity_type = lines[idx]
                idx += 1
                age = int(lines[idx])
                idx += 1
                damage = int(lines[idx])
                idx += 1
                pos = Position(int(lines[idx]), int(lines[idx + 1]))
                idx += 2
                entity = None
                if entity_type == "Antelope":
                    entity = Antelope(pos, world)
                elif entity_type == "CyberSheep":
                    entity = CyberSheep(pos, world)
                elif entity_type == "Fox":
                    entity = Fox(pos, world)
                elif entity_type == "Sheep":
                    entity = Sheep(pos, world)
                elif entity_type == "Turtle":
                    entity = Turtle(pos, world)
                elif entity_type == "Wolf":
                    entity = Wolf(pos, world)
                elif entity_type == "Belladonna":
                    entity = Belladonna(pos, world)
                elif entity_type == "Dandelion":
                    entity = Dandelion(pos, world)
                elif entity_type == "Grass":
                    entity = Grass(pos, world)
                elif entity_type == "Guarana":
                    entity = Guarana(pos, world)
                elif entity_type == "Hogweed":
                    entity = Hogweed(pos, world)
                elif entity_type == "Human":
                    entity = Human(pos, world)
                    entity.is_active = bool(lines[idx])
                    idx += 1
                    entity.cooldown = int(lines[idx])
                    idx += 1
                    entity.active = int(lines[idx])
                    idx += 1
                    world.human = entity
                entity.age = age
                entity.damage = damage
                print(entity)
                world.entities.append(entity)
            return world


