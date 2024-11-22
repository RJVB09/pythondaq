from rich.console import Console
from rich.theme import Theme

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