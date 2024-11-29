import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
import pyqtgraph as pg
from pythondaq.models.diode_experiment import DiodeExperiment, list_resources
from pythondaq.ui.diode_experiment_ui import Ui_MainWindow
import pythondaq.views.view_methods as vm
import matplotlib.pyplot as plt
import numpy as np


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):

        # Call the inherited init.
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        resources = list_resources()
        self.ui.deviceComboBox.addItems(resources)

        self.ui.start_button.clicked.connect(self.measurement)

    def advance_progress_bar(self, data):
        self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)

    @Slot()
    def measurement(self):
        # Run the experiment
        experiment = DiodeExperiment(self.ui.deviceComboBox.currentText())
    	
        # Validate the user input, and correct if the start is higher than the stop.
        start_value = self.ui.startSpinBox.value()
        stop_value = self.ui.stopSpinBox.value()
        if (start_value > stop_value):
            self.ui.stopSpinBox.setValue(start_value)
            self.ui.startSpinBox.setValue(stop_value)

        #self.ui.progressBar.setMaximum(self.ui.stopSpinBox.value()) # Set the progressbar bounds
        #self.ui.progressBar.setMinimum(self.ui.startSpinBox.value())
        self.U, self.I, self.U_err, self.I_err = experiment.scan(start = self.ui.startSpinBox.value(), stop = self.ui.stopSpinBox.value(), iterations = self.ui.iterationsSpinBox.value())

        # Convert the measurement data to numpy arrays
        self.U, self.I, self.U_err, self.I_err = np.array(self.U), np.array(self.I), np.array(self.U_err), np.array(self.I_err)
        self.plot()

    @Slot()
    def plot(self):
        # Maak eerst een scatterplot
        self.ui.plot_widget.plot(self.U, self.I, symbol = "o", symbolSize = 3, pen = {"color": "b", "width": 2})
        self.ui.plot_widget.setLabel("left", "Current (A)")
        self.ui.plot_widget.setLabel("bottom", "Voltage (V)")

        # nu de foutvlaggen, met 'breedte' en 'hoogte' in plaats van x errors en y
        # errors.
        error_bars = pg.ErrorBarItem(x = self.U, y = self.I, width = 2 * self.U_err, height = 2 * self.I_err)
        # we moeten de error_bars expliciet toevoegen aan de plot
        self.ui.plot_widget.addItem(error_bars)


def main():
    pg.setConfigOption("background", "w")
    pg.setConfigOption("foreground", "k")
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()  