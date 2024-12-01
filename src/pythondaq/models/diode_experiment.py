import numpy as np
import time as t
import threading
from pythondaq.controllers.arduino_device import ArduinoVISADevice, list_resources

raw2voltage = (3.3 / 1023.0)

class DiodeExperiment:
    def __init__(self, port):
        # Initialize all arrays.
        self.LED_U_err = np.array([])
        self.LED_I_err = np.array([])
        self.LED_U_avg = np.array([])
        self.LED_I_avg = np.array([])
        self.device = ArduinoVISADevice(port=port)

        # Record the progress in percentage
        self.progress = 0

        # Event to signal stop
        self.stop_event = threading.Event()
    
    def get_identification(self):
        """Get identification of the current device.

        Returns:
            string: String identifying the device
        """
        return self.device.get_identification()
    
    def start_scan(self, start, stop, iterations, log=None, logmethod=None, progress_bar=None, progress_bar_task=None, close=False, closing_function=None):
        """Start a scan thread

        Args:
            start (int): Start of voltage measurement range. (0-1023)
            stop (int): End of voltage measurement range. (0-1023)
            iterations (int): How many times should the voltage and current be recorded for a given input voltage.

        Returns:
            tuple: Arrays of average voltages, currents, and their errors.
        """
        self.stop_event.clear()  # Make sure the stop event is cleared before starting the scan

        self._scan_thread = threading.Thread(
            target=self.scan, 
            args=(start, stop, iterations, log, logmethod, progress_bar, progress_bar_task, close, closing_function)
        )
        self._scan_thread.start()

    def scan(self, start, stop, iterations, log=None, logmethod=None, progress_bar=None, progress_bar_task=None, close=False, closing_function=None):
        """Execute the experiment for a number of iterations in a given voltage range.

        Args:
            start (int): Start of voltage measurement range. (0-1023)
            stop (int): End of voltage measurement range. (0-1023)
            iterations (int): How many times should the voltage and current be recorded for a given input voltage.

        Returns:
            tuple: Arrays of average voltages, currents, and their errors.
        """
        self.LED_U_err = np.array([])
        self.LED_I_err = np.array([])
        self.LED_U_avg = np.array([])
        self.LED_I_avg = np.array([])

        for v in range(start, stop):
            # Check if the stop event is set, if so, break the loop
            if self.stop_event.is_set():
                break

            # Update the progress as a percentage
            self.progress = int(float(v) / float(stop - start) * 100)

            # Create the result arrays for a single voltage value
            LED_U_iteration = []
            LED_I_iteration = []

            self.device.set_output_value(v)

            for _ in range(iterations):
                # Get voltage on port A1 and A2
                U_A1 = self.device.get_input_voltage(channel=1)
                U_A2 = self.device.get_input_voltage(channel=2)

                # Calculate the voltage over the LED and the current over the LED using the resistor of 220 Ohm
                LED_U = U_A1 - U_A2
                LED_I = U_A2 / 220.0  # Ohm

                LED_U_iteration.append(LED_U)
                LED_I_iteration.append(LED_I)

            # Exit if the stop event is set
            if self.stop_event.is_set():
                break

            # Convert to NumPy arrays for error and average calculations
            LED_U_iteration = np.array(LED_U_iteration)
            LED_I_iteration = np.array(LED_I_iteration)

            # Calculate errors and averages
            LED_U_iteration_err = np.std(LED_U_iteration) / np.sqrt(iterations)
            LED_I_iteration_err = np.std(LED_I_iteration) / np.sqrt(iterations)

            LED_U_iteration_avg = np.mean(LED_U_iteration)
            LED_I_iteration_avg = np.mean(LED_I_iteration)

            # Append to arrays
            self.LED_U_err = np.append(self.LED_U_err, LED_U_iteration_err)
            self.LED_I_err = np.append(self.LED_I_err, LED_I_iteration_err)
            self.LED_U_avg = np.append(self.LED_U_avg, LED_U_iteration_avg)
            self.LED_I_avg = np.append(self.LED_I_avg, LED_I_iteration_avg)

            # Log the results of a single batch of measurements.
            if log:
                logmethod(v, LED_U_iteration_avg, LED_U_iteration_err, LED_I_iteration_avg, LED_I_iteration_err)

            # Update progress bar if given.
            if progress_bar and progress_bar_task:
                progress_bar.update(progress_bar_task, advance=1)

        self.progress = 0
        # Execute the closing function.
        if closing_function != None:
            closing_function()

        # Close communication after the experiment if the user wishes to
        if close:
            self.device.close()
