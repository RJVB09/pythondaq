from pythondaq.models.diode_experiment import DiodeExperiment
import click

@click.group()
def cmd_group():
    pass

@cmd_group.command()
def list():
    print("list stuff")
    pass

@cmd_group.command()
@click.argument("device")
def info(device):
    print(f"print identification string of {device}")
    pass

@cmd_group.command()
@click.option(
    "-vmx",
    "--maxvalue",
    default = 1023,
    help = "Maximum value in voltage range. Integer between 0-1023",
    show_default = True,  # show default in help
)
@click.option(
    "-vmn",
    "--minvalue", # arguments have to be all lowercase, no camelcase
    default = 0,
    help = "Maximum value in voltage range. Integer between 0-1023",
    show_default = True,  # show default in help
)
@click.option(
    "-o",
    "--output", # arguments have to be all lowercase, no camelcase
    default = "",
    help = "Output results into a csv file with a certain name. Usage: --output FILENAME",
    show_default = True,  # show default in help
)
@click.option(
    "-r",
    "--repetitions", # arguments have to be all lowercase, no camelcase
    default = 1,
    help = "How many times should a measurement be repeated. Integer 0-..",
    show_default = True,  # show default in help
)
@click.option(
    "--graph/--no-graph",
    default = False,
    help = "Whether to show a graph or not show one.",
    show_default = True,  # show default in help
)
def scan(maxvalue, minvalue, output, repetitions, graph): # Same goes for these arguments
    print(f"scan {minvalue}-{maxvalue} stuff {repetitions} times.")
    if output != "":
        print(f"output file named {output}.csv")
    
    if graph:
        print(f"Show a graph")
    
    pass



