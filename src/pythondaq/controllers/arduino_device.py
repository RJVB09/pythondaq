import pyvisa
import numpy as np
import random as r

def list_resources():
    """Retrieve and show a list of available ports.

    Returns:
        list (string): List of available ports.
    """
    # Retrieve the resource manager
    rm = pyvisa.ResourceManager("@py")

    # Retrieve and return all ports
    return rm.list_resources()


class ArduinoVISADevice:
    def __init__(self, port):
        """Initialize the VISA device.

        Args:
            port (string): String representing the port
        """
        # Conversion constants
        self.raw2voltage = (3.3 / 1023.0)
        self.voltage2raw = (1023.0 / 3.3)

        # Retrieve the resource manager
        rm = pyvisa.ResourceManager("@py")

        # Close any open ports
        open_ports = rm.list_opened_resources()
        for resource in open_ports:
            resource.close()

        # Get the device
        self.device = rm.open_resource(port, read_termination="\r\n", write_termination="\n")
    
    def get_identification(self):
        """Get identification of the current device.

        Returns:
            string: String identifying the device
        """
        return self.device.query("*IDN?")

    def set_output_value(self, value):
        """Set output value on port A0.

        Args:
            value (int): Value from 0 to 1023
        """
        self.device.query(f"OUT:CH0 {value}")

    def get_output_value(self):
        """Get output value on port A0.

        Returns:
            int: Value from 0 to 1023
        """
        return int(self.device.query(f"OUT:CH0?"))
    
    def get_input_value(self, channel):
        """Measure value on a channel.

        Args:
            channel (int): Channel integer on the arduino

        Returns:
            int: Value from 0 to 1023
        """
        return int(self.device.query(f"MEAS:CH{channel}?"))
    
    def get_input_voltage(self, channel):
        """Measure voltage on a channel.

        Args:
            channel (int): Channel integer on the arduino

        Returns:
            float: Voltage from 0 to 3.3
        """
        return self.raw2voltage * float(self.device.query(f"MEAS:CH{channel}?"))
    
    def set_output_voltage(self, voltage):
        """Set output voltage on port A0.

        Args:
            voltage (float): Voltage from 0 to 3.3
        """
        self.device.query(f"OUT:CH0 {int(self.voltage2raw * np.clip(0, 3.3, voltage))}")

    def close(self):
        """Closes communication with the arduino
        """
        self.device.close()

