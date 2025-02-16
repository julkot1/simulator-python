import sys

from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from view.Settings import SimSettings


class NewSimView(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.settings = None
        layout = QVBoxLayout()

        self.width_label = QLabel("Width:")
        self.width_input = QLineEdit()
        self.width_input.setValidator(QIntValidator())
        layout.addWidget(self.width_label)
        layout.addWidget(self.width_input)

        self.height_label = QLabel("Height:")
        self.height_input = QLineEdit()
        self.height_input.setValidator(QIntValidator())
        layout.addWidget(self.height_label)
        layout.addWidget(self.height_input)

        start_sim_button = QPushButton("Start Sim")
        start_sim_button.clicked.connect(self.start_sim)
        layout.addWidget(start_sim_button)

        back_button = QPushButton("Back to Main Menu")
        back_button.clicked.connect(self.show_main_menu)
        layout.addWidget(back_button)

        self.setLayout(layout)

    def start_sim(self):
        self.settings = SimSettings(self.width_input.text(), self.height_input.text())
        self.parent.sim_view.settings = self.settings
        self.parent.stacked_widget.setCurrentWidget(self.parent.sim_view)
        self.parent.sim_view.create_sim(True)

    def show_main_menu(self):
        self.parent.stacked_widget.setCurrentWidget(self.parent.main_menu)
