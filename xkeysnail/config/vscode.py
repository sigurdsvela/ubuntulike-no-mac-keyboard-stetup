import re
from xkeysnail.transform import *
from .context import Context

# Keybindings for VS Code
define_keymap(re.compile(str(Context.vscode), re.IGNORECASE),{
    # Wordwise remaining - for VS Code
    # Alt-F19 hack fixes Alt menu activation
    K("M-Left"): [K("M-F19"),K("C-Left")],                  # Left of Word
    K("M-Right"): [K("M-F19"),K("C-Right")],                # Right of Word
    K("M-Shift-Left"): [K("M-F19"),K("C-Shift-Left")],      # Select Left of Word
    K("M-Shift-Right"): [K("M-F19"),K("C-Shift-Right")],    # Select Right of Word
    
    # K("C-PAGE_DOWN"): pass_through_key,         # cancel next_view
    # K("C-PAGE_UP"): pass_through_key,           # cancel prev_view
    K("C-M-Left"): K("C-PAGE_UP"),              # next_view
    K("C-M-Right"): K("C-PAGE_DOWN"),           # prev_view

    # VS Code Shortcuts
    K("C-g"): pass_through_key,                 # cancel Go to Line...
    K("Super-g"): K("C-g"),                     # Go to Line...
    K("F3"): pass_through_key,                  # cancel Find next
    K("C-h"): pass_through_key,                 # cancel replace
    K("C-M-f"): K("C-h"),                       # replace
    K("C-Shift-h"): pass_through_key,           # cancel replace_next
    K("C-M-e"): K("C-Shift-h"),                 # replace_next
    K("f3"): pass_through_key,                  # cancel find_next
    K("C-g"): K("f3"),                          # find_next
    K("Shift-f3"): pass_through_key,            # cancel find_prev
    K("C-Shift-g"): K("Shift-f3"),              # find_prev
    K("Super-c"): K("LC-c"),                    # Sigints - interrupt
    # K("Super-C-g"): K("C-f2"),                  # Default - Sublime - find_all_under
    # K("C-M-g"): K("C-f2"),                      # Chromebook - Sublime - find_all_under
    # K("Super-Shift-up"): K("M-Shift-up"),       # multi-cursor up - Sublime
    # K("Super-Shift-down"): K("M-Shift-down"),   # multi-cursor down - Sublime
    # K(""): pass_through_key,                    # cancel
    # K(""): K(""),                               #
}, "Code")
