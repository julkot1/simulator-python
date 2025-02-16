from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel

from entity.Position import Position
from view.sim.AddEntity import Dialog
from view.sim.Tile import Tile


class Map(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.world = None
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("white"))
        self.setPalette(palette)

    def create_map(self, world):
        self.setGeometry(5, 5, world.width*32, world.height*32)
        self.world = world
        for entity in world.entities:
            entity.create_tile(self)

    def update_map(self):
        for entity in self.world.entities:
            entity.update_tile(self)

    def mousePressEvent(self, a0):
        map_x = int(a0.x()/32)
        map_y = int(a0.y()/32)
        if self.world.get_entity(Position(map_x, map_y)) is None:
            dialog = Dialog(map_x, map_y, self.world)
            dialog.exec_()
            self.update_map()


