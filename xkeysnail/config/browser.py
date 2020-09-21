import re
from xkeysnail.transform import *
from "../context.py" import Context

# Keybindings for Browsers
define_keymap(re.compile(Context.browser, re.IGNORECASE),{
    K("RC-Q"): K("RC-Q"),          # Close all browsers Instances
})
