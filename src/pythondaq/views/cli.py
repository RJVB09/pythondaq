from pythondaq.models.diode_experiment import DiodeExperiment, list_resources
import pythondaq.views.view_methods as vm
import matplotlib.pyplot as plt
import click


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
    "-vmx",
    "--maxvalue",
    default = 1023,
    help = "Maximum value in measurement range. Integer between 0-1023.",
    show_default = True,  # show default in help
)
@click.option(
    "-vmn",
    "--minvalue", # arguments have to be all lowercase, no camelcase
    default = 0,
    help = "Minimum value in measurement range. Integer between 0-1023.",
    show_default = True,  # show default in help
)
@click.option(
    "-o",
    "--output", # arguments have to be all lowercase, no camelcase
    default = "",
    help = "Output results into a csv file with a certain name. Usage: --output FILENAME.",
    show_default = True,  # show default in help
)
@click.option(
    "-i",
    "--iterations", # arguments have to be all lowercase, no camelcase
    default = 1,
    help = "How many times should a measurement be repeated. Integer 0-50.",
    show_default = True,  # show default in help
)
@click.option(
    "--graph/--no-graph",
    default = False,
    help = "Whether to show a graph or not show one.",
    show_default = True,  # show default in help
)
def scan(device, maxvalue, minvalue, output, iterations, graph): # Same goes for these arguments
    """Main view code to run
    """
    # Compare two LEDs and display the results in a scatterplot
    experiment = DiodeExperiment(device)

    # Clamp the input values and inform the user when needed.
    iterations = vm.clamp_integer_input(1,50,iterations,"iterations")
    minvalue = vm.clamp_integer_input(0,1024,minvalue,"minvalue")
    maxvalue = vm.clamp_integer_input(0,1024,maxvalue,"maxvalue")

    # Warn the user if the max value is smaller than the min value
    if maxvalue < minvalue:
        print("Warning: The maximum value of the measurement bound is smaller than the minimum value of the measurement bound. No measurements will be done.")

    # Do the measurements
    print(input("Press any key to start the measurement..."))
    U, I, U_err, I_err = experiment.scan(start = minvalue, stop = maxvalue, iterations = iterations)
    
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



