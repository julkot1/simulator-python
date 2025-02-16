from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QLabel


class LogsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Logs")
        self.setGeometry(150, 150, 600, 400)

        self.label = QLabel("", self)
        self.label.setAlignment(Qt.AlignTop)
        self.label.setGeometry(20, 20, 560, 360)

    def update(self, logs):
        text = "\n".join(logs)
        self.label.setText(text)
