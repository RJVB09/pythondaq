import pyvisa
import numpy as np
import time as t

# Raw voltage to voltage conversion factor
raw2voltage = (3.3 / 1023.0) # V

# Retrive the resource manager
rm = pyvisa.ResourceManager("@py")

# Retrive all ports
ports = rm.list_resources()

# Get the device
device = rm.open_resource("ASRL9::INSTR", read_termination="\r\n", write_termination="\n")


device.query("OUT:CH0 1023")

print(float(device.query("MEAS:CH1?")) * (3.3 / 1023.0))

# Raw voltages and voltages over their corresponding components
raw_voltages_LED = []
raw_voltages_resistor = []
voltages_LED = []
voltages_resistor = []

# Loop over all values from 0 to 1023
for v in range(1024):
    # Set voltage on port A0 to v
    device.query(f"OUT:CH0 {v}")

    # Measure raw voltage over port A1 and A2
    raw_voltage_A1 = int(device.query("MEAS:CH1?"))
    raw_voltage_A2 = int(device.query("MEAS:CH2?"))

    raw_voltage_LED = raw_voltage_A1 - raw_voltage_A2
    raw_voltage_resistor = raw_voltage_A2

    voltage_LED = raw_voltage_LED * raw2voltage
    voltage_resistor = raw_voltage_resistor * raw2voltage

    voltages_LED.append(voltage_LED)
    voltages_resistor.append(voltage_resistor)

    print(f"{v}) Voltages: ( LED raw: {np.round(raw_voltage_LED,2)}, LED: {np.round(voltage_LED,2)}V, resistor raw: {np.round(raw_voltage_resistor,2)}, resistor: {np.round(voltage_resistor,2)}V  )")
    t.sleep(0.05)
