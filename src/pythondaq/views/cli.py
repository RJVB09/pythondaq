from pythondaq.models.diode_experiment import DiodeExperiment
import click

@click.group()
def cmd_group():
    pass

@cmd_group.command()
def list():
    pass

@cmd_group.command()
@click.option(
    "-vmx",
    "--maxValue",
    default=1023,
    help="Maximum value in voltage range. Integer between 0-1023",
    show_default=True,  # show default in help
)
@click.option(
    "-vmn",
    "--minValue",
    default=0,
    help="Maximum value in voltage range. Integer between 0-1023",
    show_default=True,  # show default in help
)
def scan():
    pass



