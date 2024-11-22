from pythondaq.models.diode_experiment import DiodeExperiment, list_resources
import pythondaq.views.view_methods as vm
import matplotlib.pyplot as plt
import numpy as np
import click
from pythondaq.views.console_styling import console
from rich.progress import Progress

voltage2raw = (1023.0 / 3.3)
raw2voltage = (3.3 / 1023.0)

def logmethod(v_in, U, U_err, I, I_err):
    console.print(f"[misc][misc_var]Input U[/misc_var] = [value]{np.round(v_in * raw2voltage,3)} V[/value] | [voltage]U[/voltage] = [value]{U} V ± {U_err} V[/value] | [current]I[/current] = [value]{I} A ± {I_err} A[/value][/misc]")

@click.group()
def cmd_group():
    pass

@cmd_group.command()
@click.option(
    "-s",
    "--search",
    default = "",
    help = "Search for a device by a search prompt",
    show_default = True,  # show default in help
)
def list(search):
    """Retrieve a list of resource names connected to this computer.
    """

    resource_list = list_resources()
    search_prompt = search.split()

    # List all results when no search promt is given
    if search == "":
        print(resource_list)
    else:
        # Create list
        search_results = []
        for resource in resource_list:
            found = False
            for search_term in search_prompt:
                if search_term in resource:
                    found |= True

            if found:
                search_results.append(resource)


        print(search_results)

@cmd_group.command()
@click.argument("device")
def info(device):
    """Get the full name of a DEVICE

    DEVICE is the resource name of the targeted device.
    """
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
@click.option(
    "-l",
    "--log",
    is_flag = True,
    help = "Whether to print the measurements in the terminal when a graph or csv is created.",
    show_default = True,  # show default in help
)
def scan(device, maxvoltage, minvoltage, output, iterations, graph, log): # Same goes for these arguments
    """Run the diode experiment on a DEVICE.

    DEVICE is the resource name of the device on which to run the experiment.
    """

    # Whether a csv should be created.
    csv = output != ""

    experiment = DiodeExperiment(device)

    # Log results when there is no graph shown and no csv created or when the user asks for logging.
    log_results = (not csv and not graph) or log

    # Clamp the input voltages and inform the user when needed. also convert them to raw values instead of voltages
    iterations = vm.clamp_input(1,50,iterations,"iterations")
    start = int(vm.clamp_input(0,3.3,minvoltage,"minvoltage") * voltage2raw)
    stop = int(vm.clamp_input(0,3.3,maxvoltage,"maxvoltage") * voltage2raw)

    # Warn the user if the max voltage is smaller than the min voltage
    if stop <= start:
        console.print("[misc][warn]Warning[/warn]: The maximum voltage of the measurement bound is smaller than or equal to the minimum voltage of the measurement bound. No measurements will be done.[/misc]")

    # Do the measurements
    console.print(console.input("[notify]Press any key to start the measurement..."))
    with Progress() as progress:
        task = None

        if not log_results and stop - start > 0:
            task = progress.add_task("[yellow]Testing...", total = stop - start)

        U, I, U_err, I_err = experiment.scan(start = start, stop = stop, iterations = iterations, log = log_results, logmethod = logmethod, progress_bar = progress, progress_bar_task = task)
    
    console.print("[success]Done.[/success]")
    # Generate csv files if the user wishes to.
    if csv:
        vm.create_csv(output, (U, I, U_err, I_err), ("U (V)", "I (A)", "U_err (V)", "I_err (A)"))
    
    # Show a graph if the user wishes to
    if graph:
        plt.errorbar(x=U, y=I, yerr=I_err, xerr=U_err, fmt="ro", markersize=1.5, ecolor="r", elinewidth=0.75, label="LED", capsize=1)
        plt.xlabel("U (V)")
        plt.ylabel("I (A)")
        plt.legend()

        plt.show()

if __name__ == "__main__":
    list("")

