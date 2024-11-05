import pyvisa
import numpy as np
import time as t
from matplotlib import pyplot as plt
import csv

# Raw voltage to voltage conversion factor
raw2voltage = (3.3 / 1023.0) # V

# Retrieve the resource manager
rm = pyvisa.ResourceManager("@py")

# Retrieve all ports
ports = rm.list_resources()

# Get the device
device = rm.open_resource("ASRL9::INSTR", read_termination="\r\n", write_termination="\n")

# Raw voltages and voltages over their corresponding components
raw_voltages_LED = []
raw_voltages_resistor = []
voltages_LED = []
voltages_resistor = []

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
    t.sleep(0.01)

# Divide the voltage over the resistor by the resistance to get the current. Resistor is 220Ohm
currents_LED = [voltage / 220 for voltage in voltages_resistor] #Ohm

# Create a plot with the data
plt.plot(voltages_LED, currents_LED, "o", markersize=1)
plt.xlabel("U (V)")
plt.ylabel("I (A)")

plt.show()

# Creata a CSV file and write the voltages and currents from the LED to it.
with open("metingen.csv", "w", newline = "") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["U (V)", "I (A)"])

    for U, I in zip(voltages_LED, currents_LED):
        writer.writerow([U, I])