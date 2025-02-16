import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget

from SimState import SimState


class MainMenu(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        layout = QVBoxLayout()

        new_sim_button = QPushButton("New Sim")
        new_sim_button.clicked.connect(self.show_new_sim)
        layout.addWidget(new_sim_button)

        load_button = QPushButton("Load")
        load_button.clicked.connect(self.load)
        layout.addWidget(load_button)

        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.exit_app)
        layout.addWidget(exit_button)

        self.setLayout(layout)

    def load(self):
        self.parent.stacked_widget.setCurrentWidget(self.parent.sim_view)
        self.parent.sim_view.world = SimState(None).load("save")
        self.parent.sim_view.create_sim(False)

    def show_new_sim(self):
        self.parent.stacked_widget.setCurrentWidget(self.parent.new_sim_view)

    def exit_app(self):
        QApplication.quit()