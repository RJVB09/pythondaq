import pyvisa
import numpy as np
import time as t

from arduino_device import ArduinoVISADevice, list_resources

class DiodeExperiment:
    def __init__(self, port):
        self.device = ArduinoVISADevice(port=port)

    def scan(self, start, stop, iterations):
        # The average current and voltages after the amount of iterations
        LED_voltages_err = []
        LED_currents_err = []
        LED_voltages_avg = []
        LED_currents_avg = []

        print("Testing...")

        for v in range(start, stop):
            # Create the result lists in which we will store the voltages and currents for output voltage v
            LED_voltages = []
            LED_currents = []

            self.device.set_output_value(v)

            for i in range(iterations):
                # Get voltage on port A1 and A2
                voltage_A1 = self.device.get_input_voltage(channel=1)
                voltage_A2 = self.device.get_input_voltage(channel=2)

                # Calculate the voltage over the LED and the current over the LED using the resistor of 220 Ohm
                LED_voltage = voltage_A1 - voltage_A2
                LED_current = voltage_A2 / 220.0 #Ohm

                LED_voltages.append(LED_voltage)
                LED_currents.append(LED_current)

            # Calculate the error on the average by taking the std of the result lists and dividing this by the square root of the amount of iterations
            LED_voltages_err.append(np.std(LED_voltages) / np.sqrt(iterations))
            LED_currents_err.append(np.std(LED_currents) / np.sqrt(iterations))

            # Calculate the averages themselves
            LED_voltages_avg.append(np.average(LED_voltages))
            LED_currents_avg.append(np.average(LED_currents))

        print("Done.")
    
        return LED_voltages_avg, LED_currents_avg, LED_voltages_err, LED_currents_err

        
