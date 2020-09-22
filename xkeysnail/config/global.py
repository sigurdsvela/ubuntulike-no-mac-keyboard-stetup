import re
from xkeysnail.transform import *
from .context import Context

define_keymap(None,{
    K("Super-Space"): K("Super-Space"),

    # Wordwise
    K("Super-Left"): K("Home"),
    K("Super-Shift-Left"): K("Shift-Home"),
    K("Super-Right"): K("End"),
    K("Super-Shift-Right"): K("Shift-End"),
    K("Super-Up"): K("C-Home"),
    K("Super-Shift-Up"): K("C-Shift-Home"),
    K("Super-Down"): K("C-End"),
    K("Super-Shift-Down"): K("C-Shift-End"),
    K("Super-Backspace"): K("C-Backspace"),
    K("Super-Delete"): K("C-Delete"),
    K("Alt-Backspace"): K("C-Backspace"),
    K("Alt-Delete"): K("C-Delete"),

    # Other Selections
    K("Super-A") : K("Ctrl-A"),

    # History Tree
    K("Super-Z") : K("Ctrl-Z"),
    K("Super-Shift-Z") : K("Ctrl-Shift-Z"),

    # Clip Board
    K("Super-C") : K("Ctrl-C"),
    K("Super-V") : K("Ctrl-V"),
    K("Super-X") : K("Ctrl-X"),

    # Basic Global App Controll
    K("Super-S") : K("C-S"), # Save
    K("Super-Shift-S"): K("C-Shift-S"), # Save as
    K("Super-O"): K("C-O"), # Open
    K("Super-P"): K("C-P"), # Print
})
