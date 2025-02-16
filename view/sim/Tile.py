from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QVBoxLayout


class Tile(QWidget):
    def __init__(self, text, color, x, y, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

        self.setGeometry(x*32, y*32, 32, 32)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.label = QLabel(text, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)

    def update_position(self, position):
        self.setGeometry(position.x*32, position.y*32, 32, 32)


