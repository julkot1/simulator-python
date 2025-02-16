import math
from enum import Enum
from abc import ABC, abstractmethod


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def translate(self, direction, world):
        if direction == Direction.NORTH:
            self.y -= 1
        elif direction == Direction.SOUTH:
            self.y += 1
        elif direction == Direction.EAST:
            self.x += 1
        elif direction == Direction.WEST:
            self.x -= 1
        self.normalize(world)
        return self

    def normalize(self, world):
        if self.x >= world.width:
            self.x = 0
        if self.x < 0:
            self.x = world.width - 1
        if self.y >= world.height:
            self.y = 0
        if self.y < 0:
            self.y = world.height - 1
        return self

    def get_neighbors(self, world):
        neighbors = [Position(self.x+1, self.y).normalize(world),
                     Position(self.x+1, self.y).normalize(world),
                     Position(self.x, self.y+1).normalize(world),
                     Position(self.x, self.y-1).normalize(world)]
        return neighbors

    def distance(self, other):
        return math.sqrt(abs(self.x - other.x)**2 + abs(self.y - other.y)**2)

    def __str__(self):
        return f'({self.x}, {self.y})'


class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def __str__(self):
        return self.name
