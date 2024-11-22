import csv
from pythondaq.views.console_styling import console

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
            return int(console.input(message))
        except ValueError:
            console.print("[misc][error]Error[/error]:Input must be an integer.[/misc]")

# Clamp an integer input to a certain range and notify the user about it.
def clamp_input(min, max, value, name):
    """Clamp a value to a given min and max value and inform the user if the value has been altered.

    Args:
        min (int/float): Minimum value
        max (int/float): Maximum value
        value (int/float): Value to clamp

    Returns:
        int: Clamped value
    """
    if value < min:
        console.print(f"[misc][warn]Warning[/warn]: [misc_var]{name}[/misc_var] has been clamped to {min}.[/misc]")
        return min
    elif value > max:
        console.print(f"[misc][warn]Warning[/warn]: [misc_var]{name}[/misc_var] has been clamped to {max}.[/misc]")
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
        console.print(f"[misc][error]Error[/error]: CSV file [misc_var]\"{filename}.csv\"[/misc_var] can't be created: The amount of headers does not match the amount of colums.[/misc]")
        return

    # Creata a CSV file and write the voltages and currents from the LED to it.
    with open(f"{filename}.csv", "w", newline = "") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        
        # Zip the colums tuple and iterate through with a tuple named data
        for data in zip(*columns):
            # writer.writerow accepts tuples
            writer.writerow(data)