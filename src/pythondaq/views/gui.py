import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
import pyqtgraph as pg
from pythondaq.models.diode_experiment import DiodeExperiment, list_resources
import pythondaq.views.view_methods as vm
import matplotlib.pyplot as plt
import numpy as np


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):

        # Call the inherited init.
        super().__init__()

        self.measurement("ASRL9::INSTR")

        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)

        vbox = QtWidgets.QVBoxLayout(central_widget)
        self.plot_widget = pg.PlotWidget()
        vbox.addWidget(self.plot_widget)

    def measurement(self, port):
        # Run the experiment
        experiment = DiodeExperiment(port)
        self.U, self.I, self.U_err, self.I_err = experiment.scan(start = 0, stop = 1023, iterations = 3)

        # Convert the measurement data to numpy arrays
        self.U, self.I, self.U_err, self.I_err = np.array(self.U), np.array(self.I), np.array(self.U_err), np.array(self.I_err)

    @Slot()
    def plot(self):
        # Maak eerst een scatterplot
        self.plot_widget.plot(self.U, self.I, symbol = "o", symbolSize = 3, pen = {"color": "b", "width": 2})
        self.plot_widget.setLabel("left", "y-axis")
        self.plot_widget.setLabel("bottom", "x-axis")

        # nu de foutvlaggen, met 'breedte' en 'hoogte' in plaats van x errors en y
        # errors.
        error_bars = pg.ErrorBarItem(x = self.U, y = self.I, width = 2 * self.U_err, height = 2 * self.I_err)
        # we moeten de error_bars expliciet toevoegen aan de plot
        self.plot_widget.addItem(error_bars)


def main():
    pg.setConfigOption("background", "w")
    pg.setConfigOption("foreground", "k")
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    ui.plot()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()  