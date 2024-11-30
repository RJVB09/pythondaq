import sys
from PySide6 import QtWidgets
from PySide6.QtCore import Slot
import pyqtgraph as pg
from pythondaq.models.fake_diode_experiment import DiodeExperiment, list_resources
from pythondaq.ui.diode_experiment_ui import Ui_MainWindow
import pythondaq.views.view_methods as vm
import pythondaq.views.view_methods as vm
import matplotlib.pyplot as plt
import numpy as np


class UserInterface(QtWidgets.QMainWindow):
    def __init__(self):

        # Call the inherited init.
        super().__init__()

        # Prevent saving nothing
        self.experiment_ran = False
        
        # Use the UI created in the designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Update the combobox with devices
        resources = list_resources()
        self.ui.deviceComboBox.addItems(resources)

        # Set the labels prior to a plot
        self.ui.plot_widget.setLabel("left", "Current (A)")
        self.ui.plot_widget.setLabel("bottom", "Voltage (V)")

        # Connect the buttons to their functions
        self.ui.startButton.clicked.connect(self.measurement)
        self.ui.saveButton.clicked.connect(self.save_results)

    def advance_progress_bar(self, data):
        self.ui.progressBar.setValue(self.ui.progressBar.value() + 1)

    @Slot()
    def save_results(self):
        # The default name of the csv file is DiodeExperimentResults.csv rename if a filename is given.
        name = "DiodeExperimentResults"
        if self.ui.saveLineEdit.text() != "":
            name = self.ui.saveLineEdit.text()

        # Dont save anything when there is no experiment done
        if self.experiment_ran:
            vm.create_csv(name, (self.U, self.I, self.U_err, self.I_err), ("U (V)", "I (A)", "U_err (V)", "I_err (A)"))

    @Slot()
    def measurement(self):
        # Run the experiment
        experiment = DiodeExperiment(self.ui.deviceComboBox.currentText())
    	
        # Validate the user input, and correct if the start is higher than the stop.
        start_value = self.ui.startSpinBox.value()
        stop_value = self.ui.stopSpinBox.value()
        if start_value > stop_value:
            self.ui.stopSpinBox.setValue(start_value)
            self.ui.startSpinBox.setValue(stop_value)

        #self.ui.progressBar.setMaximum(self.ui.stopSpinBox.value()) # Set the progressbar bounds
        #self.ui.progressBar.setMinimum(self.ui.startSpinBox.value())
        self.U, self.I, self.U_err, self.I_err = experiment.scan(start = self.ui.startSpinBox.value(), stop = self.ui.stopSpinBox.value(), iterations = self.ui.iterationsSpinBox.value(), close = True)

        # Convert the measurement data to numpy arrays
        self.U, self.I, self.U_err, self.I_err = np.array(self.U), np.array(self.I), np.array(self.U_err), np.array(self.I_err)
        self.plot()

        # Allow for saving
        self.experiment_ran = True

    @Slot()
    def plot(self):
        # Clear the graph and plot the data
        self.ui.plot_widget.clear()

        self.ui.plot_widget.plot(self.U, self.I, symbol = "o", symbolSize = 3, pen = {"color": "b", "width": 2})
        self.ui.plot_widget.setLabel("left", "Current (A)")
        self.ui.plot_widget.setLabel("bottom", "Voltage (V)")

        # Plot the errorbars
        error_bars = pg.ErrorBarItem(x = self.U, y = self.I, width = 2 * self.U_err, height = 2 * self.I_err)
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