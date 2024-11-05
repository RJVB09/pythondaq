import pyvisa
import numpy as np

# Retrieve list of available ports
def list_resources():
    # Retrieve the resource manager
    rm = pyvisa.ResourceManager("@py")

    # Retrieve and return all ports
    return rm.list_resources()


class ArduinoVISADevice:
    def __init__(self, port):
        self.raw2voltage = (3.3 / 1023.0)
        self.voltage2raw = (1023.0 / 3.3)

        # Retrieve the resource manager
        rm = pyvisa.ResourceManager("@py")

        # Get the device
        self.device = rm.open_resource(port, read_termination="\r\n", write_termination="\n")

    # Get the identification string of the device
    def get_identification(self):
        return self.device.query("*IDN?")

    def set_output_value(self, value):
        self.device.query(f"OUT:CH0 {value}")

    def get_output_value(self):
        return int(self.device.query(f"OUT:CH0?"))
    
    def get_input_value(self, channel):
        return int(self.device.query(f"MEAS:CH{channel}?"))

    # Return channel voltage in volt
    def get_input_voltage(self, channel):
        return self.raw2voltage * float(self.device.query(f"MEAS:CH{channel}?"))

    # Set channel value in volt
    def set_output_voltage(self, voltage):
        self.device.query(f"OUT:CH0 {int(self.voltage2raw * np.clip(0, 3.3, voltage))}")

