import re
from xkeysnail.transform import *
from .context import Context

# Keybindings for Browsers
define_keymap(re.compile(str(Context.browser), re.IGNORECASE),{
    K("Super-Q"): K("Super-Q"),          # Close all browsers Instances
    K("Super-W"): K("Ctrl-W"),          # Close Tab
    K("Super-T"): K("Ctrl-T"),           # New Tab
    K("Super-Shift-T"): K("Ctrl-Shift-T"),           # Reopen closed tab
    K("Super-F"): K("Ctrl-F"),           # Find in page
}, "browser")
