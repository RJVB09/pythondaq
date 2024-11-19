from pythondaq.models.diode_experiment import DiodeExperiment, list_resources
import pythondaq.views.view_methods as vm
import matplotlib.pyplot as plt
import click

voltage2raw = (1023.0 / 3.3)

@click.group()
def cmd_group():
    pass

@cmd_group.command()
def list():
    list_resources()
    pass

@cmd_group.command()
@click.argument("device")
def info(device):
    # Create a new instance of an experiment as to avoid using the controller.
    experiment = DiodeExperiment(device)
    print(experiment.get_identification())

@cmd_group.command()
@click.argument("device")
@click.option(
    "-mxv",
    "--maxvoltage",
    default = 3.3,
    help = "Maximum voltage in measurement range. Float between 0-3.3",
    show_default = True,  # show default in help
)
@click.option(
    "-mnv",
    "--minvoltage", # arguments have to be all lowercase, no camelcase
    default = 0.0,
    help = "Minimum voltage in measurement range. Float between 0-3.3",
    show_default = True,  # show default in help
)
@click.option(
    "-o",
    "--output", # arguments have to be all lowercase, no camelcase
    default = "",
    help = "Output results into a csv file with a given name.",
    show_default = True,  # show default in help
)
@click.option(
    "-i",
    "--iterations", # arguments have to be all lowercase, no camelcase
    default = 1,
    help = "How many times should a measurement be repeated. Integer between 0-50.",
    show_default = True,  # show default in help
)
@click.option(
    "--graph/--no-graph",
    default = False,
    help = "Whether to show a graph or not show one.",
    show_default = True,  # show default in help
)
def scan(device, maxvoltage, minvoltage, output, iterations, graph): # Same goes for these arguments
    """Main view code to run
    """
    # Compare two LEDs and display the results in a scatterplot
    experiment = DiodeExperiment(device)

    # Clamp the input voltages and inform the user when needed. also convert them to raw values instead of voltages
    iterations = vm.clamp_input(1,50,iterations,"iterations")
    start = int(vm.clamp_input(0,3.3,minvoltage,"minvoltage") * voltage2raw)
    stop = int(vm.clamp_input(0,3.3,maxvoltage,"maxvoltage") * voltage2raw)

    # Warn the user if the max voltage is smaller than the min voltage
    if maxvoltage < minvoltage:
        print("Warning: The maximum voltage of the measurement bound is smaller than the minimum voltage of the measurement bound. No measurements will be done.")

    # Do the measurements
    print(input("Press any key to start the measurement..."))
    U, I, U_err, I_err = experiment.scan(start = start, stop = stop, iterations = iterations)
    
    # Generate csv files if the user wishes to.
    if output != "":
        vm.create_csv(output, (U, I, U_err, I_err), ("U (V)", "I (A)", "U_err (V)", "I_err (A)"))
    
    # Show a graph if the user wishes to
    if graph:
        plt.errorbar(x=U, y=I, yerr=I_err, xerr=U_err, fmt="ro", markersize=1.5, ecolor="r", elinewidth=0.75, label="LED", capsize=1)
        plt.xlabel("U (V)")
        plt.ylabel("I (A)")
        plt.legend()

        plt.show()
    
    pass



