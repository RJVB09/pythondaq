import numpy as np
import time as t

def list_resources():
    """Retrieve and show a list of available ports.

    Returns:
        list (string): List of available ports.
    """

    # Retrieve and return all ports
    return ["Device1","Device2","Device3"]


class ArduinoVISADevice:
    def __init__(self, port):
        """Initialize the VISA device.

        Args:
            port (string): String representing the port
        """
        # Conversion constants
        self.raw2voltage = (3.3 / 1023.0)
        self.voltage2raw = (1023.0 / 3.3)
    
    def get_identification(self):
        """Get identification of the current device.

        Returns:
            string: String identifying the device
        """
        return "Fake device"

    def set_output_value(self, value):
        """Set output value on port A0.

        Args:
            value (int): Value from 0 to 1023
        """

    def get_output_value(self):
        """Get output value on port A0.

        Returns:
            int: Value from 0 to 1023
        """
        t.sleep(0.001)
        return 0
    
    def get_input_value(self, channel):
        """Measure value on a channel.

        Args:
            channel (int): Channel integer on the arduino

        Returns:
            int: Value from 0 to 1023
        """
        return 0
    
    def get_input_voltage(self, channel):
        """Measure voltage on a channel.

        Args:
            channel (int): Channel integer on the arduino

        Returns:
            float: Voltage from 0 to 3.3
        """
        t.sleep(0.001)
        return 0
    
    def set_output_voltage(self, voltage):
        """Set output voltage on port A0.

        Args:
            voltage (float): Voltage from 0 to 3.3
        """

