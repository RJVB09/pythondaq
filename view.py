from matplotlib import pyplot as plt
import csv
from diode_experiment import DiodeExperiment
import os

# Try to ask for an integer, ask again if the value given is not an integer.
def try_integer_input(message):
    """Ask the user for an integer with a given message.

    Args:
        message (string): Message to add when asking

    Returns:
        int: Integer given by the user
    """
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Input must be an integer.")

# Clamp an integer input to a certain range and notify the user about it.
def clamp_integer_input(min, max, value):
    """Clamp an integer to a given min and max value and inform the user if the value has been altered.

    Args:
        min (int): Minimum value
        max (int): Maximum value
        value (int): Value to clamp

    Returns:
        int: Clamped value
    """
    if value < min:
        print(f"Value has been set to minimum value of {min}.")
        return min
    elif value > max:
        print(f"Value has been set to maximum value of {max}.")
        return max

    return value

def create_csv(filename, columns, headers):
    """Creates a csv file.

    Args:
        filename (string): name of the csv file
        columns (tuple (list)): Column data lists
        headers (tuple (string)): Headers for each column
    """

    # TODO prevent files from being overwritten.

    if len(headers) != len(columns):
        print(f"CSV file \"{filename}.csv\" can't be created: The amount of headers does not match the amount of colums.")
        return

    # Creata a CSV file and write the voltages and currents from the LED to it.
    with open(f"{filename}.csv", "w", newline = "") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        
        # Zip the colums tuple and iterate through with a tuple named data
        for data in zip(*columns):
            # writer.writerow accepts tuples
            writer.writerow(data)
            

# Compare two LEDs and display the results in a scatterplot
experiment = DiodeExperiment("ASRL9::INSTR")

# Ask for all measurement parameters and inform the user about their input.
iterations = clamp_integer_input(1,50,try_integer_input("Number of experiment iterations: "))
start = clamp_integer_input(0,1024,try_integer_input("Start measurement bound: "))
stop = clamp_integer_input(0,1024,try_integer_input("Stop measurement bound: "))

# Warn the user if the stop value is smaller than the start value
if stop < start:
    print("Warning: stop measurement bound is smaller than start measurement bound, no measurements will be done.")

# Do the measurements
print(input("Place LED 1, and press any key..."))
U_1, I_1, U_1_err, I_1_err = experiment.scan(start = start, stop = stop, iterations = iterations)

print(input("Place LED 2, and press any key..."))
U_2, I_2, U_2_err, I_2_err = experiment.scan(start = start, stop = stop, iterations = iterations)

# Display the results of both LEDs in the same graph
plt.errorbar(x=U_1, y=I_1, yerr=I_1_err, xerr=U_1_err, fmt="ro", markersize=1.5, ecolor="r", elinewidth=0.75, label="LED 1", capsize=1)
plt.errorbar(x=U_2, y=I_2, yerr=I_2_err, xerr=U_2_err, fmt="bo", markersize=1.5, ecolor="b", elinewidth=0.75, label="LED 2", capsize=1)
plt.xlabel("U (V)")
plt.ylabel("I (A)")
plt.legend()

plt.show()

# Generate csv files
create_csv("MetingenLed1", (U_1, I_1, U_1_err, I_1_err), ("U (V)", "I (A)", "U_err (V)", "I_err (A)"))
create_csv("MetingenLed2", (U_2, I_2, U_2_err, I_2_err), ("U (V)", "I (A)", "U_err (V)", "I_err (A)"))

