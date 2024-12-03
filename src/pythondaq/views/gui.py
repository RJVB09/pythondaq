import sys
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Slot
import pyqtgraph as pg
from pythondaq.models.diode_experiment import DiodeExperiment, list_resources
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
        self.measurement_running = False  # Flag to track if measurement is running
        
        # Use the UI created in the designer
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Update the combobox with devices
        resources = list_resources()
        self.ui.deviceComboBox.addItems(resources)

        # Initialize the experiment using the current resource
        self.experiment = DiodeExperiment(self.ui.deviceComboBox.currentText())

        # Set the labels prior to a plot
        self.ui.plot_widget.setLabel("left", "Current (A)")
        self.ui.plot_widget.setLabel("bottom", "Voltage (V)")

        # Connect the buttons to their functions
        self.ui.startButton.clicked.connect(self.measurement)
        self.ui.stopButton.clicked.connect(self.stop_measurement)  # Connect stop button
        self.ui.saveButton.clicked.connect(self.save_results)

        # Create a timer and allow the plot and progress bar to be updated every 100 ms
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.plot)
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(100)

    @Slot()
    def save_results(self):
        """Save the measurement results to a csv file.
        """
        # The default name of the csv file is DiodeExperimentResults.csv rename if a filename is given.
        name = "DiodeExperimentResults"
        if self.ui.saveLineEdit.text() != "":
            name = self.ui.saveLineEdit.text()

        # Dont save anything when there is no experiment done
        if self.experiment_ran:
            vm.create_csv(name, (self.experiment.LED_U_avg, self.experiment.LED_I_avg, self.experiment.LED_U_err, self.experiment.LED_I_err), ("U (V)", "I (A)", "U_err (V)", "I_err (A)"))

    @Slot()
    def measurement(self):
        """Run the measurement on a thread.
        """
        if self.measurement_running:
            return  # Prevent starting a new measurement if one is already running
        
        self.measurement_running = True
        self.ui.startButton.setEnabled(False)  # Disable the start button while measurement is running
        self.ui.stopButton.setEnabled(True)   # Enable the stop button during the measurement

        # Update the experiment to the selected port
        self.experiment = DiodeExperiment(self.ui.deviceComboBox.currentText())
    	
        # Validate the user input, and correct if the start is higher than the stop.
        start_value = self.ui.startSpinBox.value()
        stop_value = self.ui.stopSpinBox.value()
        if start_value > stop_value:
            self.ui.stopSpinBox.setValue(start_value)
            self.ui.startSpinBox.setValue(stop_value)

        # Start a scan on a thread
        self.experiment.start_scan(start = self.ui.startSpinBox.value(), stop = self.ui.stopSpinBox.value(), iterations = self.ui.iterationsSpinBox.value(), close = True, closing_function = self.reset_ui_after_measurement)

        # Allow for saving
        self.experiment_ran = True

    @Slot()
    def stop_measurement(self):
        """Stop the ongoing measurement."""
        if self.measurement_running:
            self.experiment.stop_event.set()  # Signal the scan to stop
            self.measurement_running = False
            self.ui.startButton.setEnabled(True)  # Enable the start button
            self.ui.stopButton.setEnabled(False)  # Disable the stop button

    @Slot()
    def update_progress(self):
        """Updates the progress bar using experiment info.
        """
        self.ui.progressBar.setValue(self.experiment.progress)

    @Slot()
    def plot(self):
        """Plot the measured data.
        """
        # Clear the graph and plot the data
        self.ui.plot_widget.clear()

        self.ui.plot_widget.plot(self.experiment.LED_U_avg, self.experiment.LED_I_avg, symbol = "o", symbolSize = 3, pen = {"color": "b", "width": 2})
        self.ui.plot_widget.setLabel("left", "Current (A)")
        self.ui.plot_widget.setLabel("bottom", "Voltage (V)")
        self.ui.plot_widget.showGrid(x=True, y=True)

        # Plot the errorbars
        error_bars = pg.ErrorBarItem(x = self.experiment.LED_U_avg, y = self.experiment.LED_I_avg, width = 2 * self.experiment.LED_U_err, height = 2 * self.experiment.LED_I_err)
        self.ui.plot_widget.addItem(error_bars)

    def reset_ui_after_measurement(self):
        """Reset UI buttons after the measurement is finished."""
        self.measurement_running = False
        self.ui.startButton.setEnabled(True)
        self.ui.stopButton.setEnabled(False)



def main():
    pg.setConfigOption("background", "#161616")
    pg.setConfigOption("foreground", "w")
    app = QtWidgets.QApplication(sys.argv)
    ui = UserInterface()
    ui.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()  