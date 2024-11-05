import pyvisa
import numpy as np
import time as t

from arduino_device import ArduinoVISADevice, list_resources

class DiodeExperiment:
    def __init__(self, port):
        self.device = ArduinoVISADevice(port=port)

    def scan(self, start, stop):
        LED_voltages = []
        LED_currents = []

        print("Testing...")

        for v in range(start, stop):
            self.device.set_output_value(v)

            # Get voltage on port A1 and A2
            voltage_A1 = self.device.get_input_voltage(channel=1)
            voltage_A2 = self.device.get_input_voltage(channel=2)

            # Calculate the voltage over the LED and the current over the LED using the resistor of 220 Ohm
            LED_voltage = voltage_A1 - voltage_A2
            LED_current = voltage_A2 / 220.0 #Ohm

            LED_voltages.append(LED_voltage)
            LED_currents.append(LED_current)

        print("Done.")
    
        return LED_voltages, LED_currents

        
