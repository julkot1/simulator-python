from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget
from view.Menu import MainMenu
from view.NewSim import NewSimView
from view.sim.SimView import SimView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sim Julian Kotłowski s197694")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.main_menu = MainMenu(self)
        self.new_sim_view = NewSimView(self)
        self.sim_view = SimView(self)

        self.stacked_widget.addWidget(self.main_menu)
        self.stacked_widget.addWidget(self.new_sim_view)
        self.stacked_widget.addWidget(self.sim_view)

        self.stacked_widget.setCurrentWidget(self.main_menu)
