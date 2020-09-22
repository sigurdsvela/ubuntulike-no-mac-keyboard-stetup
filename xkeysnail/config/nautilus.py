import re
from xkeysnail.transform import *
from .context import Context

# Keybindings for Nautilus
define_keymap(re.compile(str(Context.nautilus), re.IGNORECASE),{
    K("RC-Up"): K("M-Up"),          # Go Up dir
    K("RC-Down"): K("M-Down"),      # Go Down dir
    K("RC-Left"): K("M-Left"),      # Go Back
    K("RC-Right"): K("M-Right"),    # Go Forward
})
