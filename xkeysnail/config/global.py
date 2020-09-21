import re
from xkeysnail.transform import *
from "../context.py" import Context

define_keymap(None,{
    # Basic App hotkey functions
    K("RC-Q"): K("Alt-F4"),
    K("RC-H"): K("Alt-F9"),
    # Cmd Tab - App Switching Default
    K("RC-Tab"): K("RC-F13"),                     # Default not-xfce4
    K("RC-Shift-Tab"): K("RC-Shift-F13"),         # Default not-xfce4
    K("RC-Grave"): K("M-F6"),                     # Default not-xfce4
    K("RC-Shift-Grave"): K("M-Shift-F6"),         # Default not-xfce4
    # K("RC-Tab"): K("RC-backslash"),               # xfce4
    # K("RC-Shift-Tab"): K("RC-Shift-backslash"),   # xfce4
    # K("RC-Grave"): K("RC-Shift-backslash"),       # xfce4
    # In-App Tab switching
    # K("M-Tab"): K("C-Tab"),                       # Chromebook - In-App Tab switching
    # K("M-Shift-Tab"): K("C-Shift-Tab"),           # Chromebook - In-App Tab switching
    # K("M-Grave") : K("C-Shift-Tab"),              # Chromebook - In-App Tab switching
    K("Super-Tab"): K("LC-Tab"),                  # Default not-chromebook
    K("Super-Shift-Tab"): K("LC-Shift-Tab"),      # Default not-chromebook

    # Wordwise
    K("RC-Left"): K("Home"),                      # Beginning of Line
    K("Super-a"): K("Home"),                      # Beginning of Line
    K("RC-Shift-Left"): K("Shift-Home"),          # Select all to Beginning of Line
    K("RC-Right"): K("End"),                      # End of Line
    K("Super-e"): K("End"),                       # End of Line
    K("RC-Shift-Right"): K("Shift-End"),          # Select all to End of Line
    # K("RC-Left"): K("C-LEFT_BRACE"),              # Firefox-nw - Back
    # K("RC-Right"): K("C-RIGHT_BRACE"),            # Firefox-nw - Forward
    # K("RC-Left"): K("M-LEFT"),                    # Chrome-nw - Back
    # K("RC-Right"): K("M-RIGHT"),                  # Chrome-nw - Forward
    K("RC-Up"): K("C-Home"),                      # Beginning of File
    K("RC-Shift-Up"): K("C-Shift-Home"),          # Select all to Beginning of File
    K("RC-Down"): K("C-End"),                     # End of File
    K("RC-Shift-Down"): K("C-Shift-End"),         # Select all to End of File
    # K("M-Backspace"): K("Delete"),                # Chromebook - Delete
    K("Super-Backspace"): K("C-Backspace"),       # Default not-chromebook - Delete Left Word of Cursor
    K("Super-Delete"): K("C-Delete"),             # Default not-chromebook - Delete Right Word of Cursor
    K("Alt-Backspace"): K("C-Backspace"),       # Default not-chromebook - Delete Left Word of Cursor
    K("Alt-Delete"): K("C-Delete"),             # Default not-chromebook - Delete Right Word of Cursor
    # K(""): pass_through_key,                      # cancel
    # K(""): K(""),                                 #
})

define_keymap(lambda wm_class: wm_class.casefold() not in Context.vscode,{
    K("Super-Space"): K("C-Space"),         # Basic code completion
    # Wordwise remaining - for Everything but VS Code
    K("M-Left"): K("C-Left"),               # Left of Word
    K("M-Shift-Left"): K("C-Shift-Left"),   # Select Left of Word
    K("M-Right"): K("C-Right"),             # Right of Word
    K("M-Shift-Right"): K("C-Shift-Right"), # Select Right of Word
    K("M-Shift-g"): K("C-Shift-g"),         # View source control
    # ** VS Code fix **
    #   Electron issue precludes normal keybinding fix.
    #   Alt menu auto-focus/toggle gets in the way.
    #
    #   refer to ./xkeysnail-config/vscode_keybindings.json
    # **
    #
    # ** Firefox fix **
    #   User will need to set "ui.key.menuAccessKeyFocuses"
    #   under about:config to false.
    #
    #   https://superuser.com/questions/770301/pentadactyl-how-to-disable-menu-bar-toggle-by-alt
    # **
    #
})