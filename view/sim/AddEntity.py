from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QListWidget, QPushButton, QMessageBox

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


class Dialog(QDialog):
    def __init__(self, map_x, map_y, world):
        super().__init__()
        self.map_x = map_x
        self.map_y = map_y
        self.world = world

        self.setWindowTitle("Select Entity")

        self.layout = QVBoxLayout()

        self.list_widget = QListWidget()

        self.options = self.get_options()

        self.list_widget.addItems(self.options)

        self.button = QPushButton("Select")
        self.button.clicked.connect(self.show_selection)

        self.layout.addWidget(self.list_widget)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def show_selection(self):
        selected_items = self.list_widget.selectedItems()
        if not selected_items:
            self.close()
        else:
            selected = "".join(item.text() for item in selected_items)
            if selected == "Antelope":
                self.world.add_entity(Antelope(Position(self.map_x, self.map_y), self.world))
            elif selected == "CyberSheep":
                self.world.add_entity(CyberSheep(Position(self.map_x, self.map_y), self.world))
            elif selected == "Fox":
                self.world.add_entity(Fox(Position(self.map_x, self.map_y), self.world))
            elif selected == "Sheep":
                self.world.add_entity(Sheep(Position(self.map_x, self.map_y), self.world))
            elif selected == "Turtle":
                self.world.add_entity(Turtle(Position(self.map_x, self.map_y), self.world))
            elif selected == "Wolf":
                self.world.add_entity(Wolf(Position(self.map_x, self.map_y), self.world))
            elif selected == "Belladonna":
                self.world.add_entity(Belladonna(Position(self.map_x, self.map_y), self.world))
            elif selected == "Dandelion":
                self.world.add_entity(Dandelion(Position(self.map_x, self.map_y), self.world))
            elif selected == "Grass":
                self.world.add_entity(Grass(Position(self.map_x, self.map_y), self.world))
            elif selected == "Guarana":
                self.world.add_entity(Guarana(Position(self.map_x, self.map_y), self.world))
            elif selected == "Hogweed":
                self.world.add_entity(Hogweed(Position(self.map_x, self.map_y), self.world))
        self.close()

    def get_options(self):
        return [
            "Antelope",
            "CyberSheep",
            "Fox",
            "Sheep",
            "Turtle",
            "Wolf",
            "Belladonna",
            "Dandelion",
            "Grass",
            "Guarana",
            "Hogweed",
        ]
