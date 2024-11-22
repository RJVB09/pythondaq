from rich.console import Console
from rich.theme import Theme
import numpy as np

voltage2raw = (1023.0 / 3.3)
raw2voltage = (3.3 / 1023.0)

resultstheme = Theme({
    "misc" : "grey70",
    "misc_var" : "green",
    "voltage" : "royal_blue1",
    "current" : "deep_pink2",
    "value" : "bright_black bold italic",
    "warn" : "orange1 bold",
    "error" : "red1 bold",
    "success" : "green1 bold",
    "notify" : "bright_white"
})

console = Console(theme = resultstheme)

def logmethod(v_in, U, U_err, I, I_err):
    console.print(f"[misc][misc_var]Input U[/misc_var] = [value]{np.round(v_in * raw2voltage,3)} V[/value] | [voltage]U[/voltage] = [value]{U} V ± {U_err} V[/value] | [current]I[/current] = [value]{I} A ± {I_err} A[/value][/misc]")