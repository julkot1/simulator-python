from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel

from SimState import SimState
from entity.Position import Position, Direction
from entity.World import World
from entity.animal.Animal import Animal
from entity.animal.CyberSheep import CyberSheep
from entity.animal.Fox import Fox
from entity.animal.Human import Human
from entity.animal.Sheep import Sheep
from entity.animal.Turtle import Turtle
from entity.animal.Wolf import Wolf
from entity.plant.Grass import Grass
from entity.plant.Guarana import Guarana
from entity.plant.Hogweed import Hogweed
from view.sim.AddEntity import Dialog
from view.sim.Logs import LogsWindow
from view.sim.Map import Map


class SimView(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.settings = None
        self.world = None

        self.map = Map(self)

        self.next_turn_b = QPushButton("Next Turn", self)
        self.next_turn_b.clicked.connect(self.next_turn)

        self.save_b = QPushButton("Save", self)
        self.save_b.clicked.connect(self.save)

        self.logs = None

        self.turn_counter = QLabel("Turn Counter", self)
        self.human_info = QLabel("Human info", self)

    def human_info_update(self):
        text = f"Human is dead"
        if self.world.human is not None:
            text = f"Human: \nnext move: {self.world.human.direction}\n"
            if self.world.human.is_active:
                text += f"ult: {self.world.human.active}/5"
            else:
                text += f"ult: cooldown {self.world.human.cooldown}/5"
        self.human_info.setText(text)

    def save(self):
        sim_state = SimState(self.world)
        sim_state.save("save")

    def next_turn(self):
        self.world.next_turn(self.map)
        self.turn_counter.setText(f"Turn: {self.world.turn}")
        self.human_info_update()
        self.logs.update(self.world.logger.logs)

    def create_sim(self, new_game):
        self.parent.resize(800, 600)

        if new_game:
            self.world = World(self.settings.width, self.settings.height)
            human = Human(Position(2, 2), self.world)
            self.world.human = human
            self.world.add_entity(human)

            self.world.add_entity(CyberSheep(Position(0, 0), self.world))
            self.world.add_entity(Hogweed(Position(4, 6), self.world))

        self.map.create_map(self.world)

        self.turn_counter.setGeometry(self.map.width() + 100, 5, 100, 20)
        self.human_info.setGeometry(self.map.width() + 100, 30, 150, 50)

        self.next_turn_b.setGeometry(self.map.width() + 100, 90, 100, 30)

        self.save_b.setGeometry(self.map.width() + 100, 110, 100, 30)

        self.turn_counter.setText(f"Turn: {self.world.turn}")
        self.human_info_update()

        self.logs = LogsWindow()
        self.logs.update(self.world.logger.logs)
        self.logs.show()

    def keyPressEvent(self, a0):
        if self.world is None:
            return
        if self.world.human is None:
            return
        key = a0.key()
        if key == Qt.Key_W:
            self.world.human.direction = Direction.NORTH
        elif key == Qt.Key_S:
            self.world.human.direction = Direction.SOUTH
        elif key == Qt.Key_A:
            self.world.human.direction = Direction.WEST
        elif key == Qt.Key_D:
            self.world.human.direction = Direction.EAST
        elif key == Qt.Key_U:
            if self.world.human.cooldown == 5:
                self.world.human.is_active = True

        self.human_info_update()
