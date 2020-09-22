import re
from xkeysnail.transform import *
from .context import Context

define_keymap(re.compile("Sublime_text", re.IGNORECASE),{
    K("Super-Space"): K("C-Space"),             # Basic code completion
    K("C-Super-up"): K("M-o"),                  # Switch file
    K("Super-RC-f"): K("f11"),                  # toggle_full_screen
    K("C-M-v"): [K("C-k"), K("C-v")],           # paste_from_history
    K("C-up"): pass_through_key,                # cancel scroll_lines up
    K("C-M-up"): K("C-up"),                     # scroll_lines up
    K("C-down"): pass_through_key,              # cancel scroll_lines down
    K("C-M-down"): K("C-down"),                 # scroll_lines down
    K("Super-Shift-up"): K("M-Shift-up"),       # multi-cursor up
    K("Super-Shift-down"): K("M-Shift-down"),   # multi-cursor down
    K("C-PAGE_DOWN"): pass_through_key,         # cancel next_view
    K("C-PAGE_UP"): pass_through_key,           # cancel prev_view
    K("C-Shift-left_brace"): K("C-PAGE_DOWN"),  # next_view
    K("C-Shift-right_brace"): K("C-PAGE_UP"),   # prev_view
    K("C-M-right"): K("C-PAGE_DOWN"),           # next_view
    K("C-M-left"): K("C-PAGE_UP"),              # prev_view
    K("insert"): pass_through_key,              # cancel toggle_overwrite
    K("C-M-o"): K("insert"),                    # toggle_overwrite
    K("M-c"): pass_through_key,                 # cancel toggle_case_sensitive
    K("C-M-c"): K("M-c"),                       # toggle_case_sensitive
    K("C-h"): pass_through_key,                 # cancel replace
    K("C-M-f"): K("C-h"),                       # replace
    K("C-Shift-h"): pass_through_key,           # cancel replace_next
    K("C-M-e"): K("C-Shift-h"),                 # replace_next
    K("f3"): pass_through_key,                  # cancel find_next
    K("C-g"): K("f3"),                          # find_next
    K("Shift-f3"): pass_through_key,            # cancel find_prev
    K("C-Shift-g"): K("Shift-f3"),              # find_prev
    K("C-f3"): pass_through_key,                # cancel find_under
    K("Super-M-g"): K("C-f3"),                  # find_under
    K("C-Shift-f3"): pass_through_key,          # cancel find_under_prev
    K("Super-M-Shift-g"): K("C-Shift-f3"),      # find_under_prev
    K("M-f3"): pass_through_key,                # Default - cancel find_all_under
    # K("M-Refresh"): pass_through_key,           # Chromebook - cancel find_all_under
    # K("M-C-g"): K("M-Refresh"),                 # Chromebook - find_all_under
    K("Super-C-g"): K("M-f3"),                  # Default - find_all_under
    K("C-Shift-up"): pass_through_key,          # cancel swap_line_up
    K("Super-M-up"): K("C-Shift-up"),           # swap_line_up
    K("C-Shift-down"): pass_through_key,        # cancel swap_line_down
    K("Super-M-down"): K("C-Shift-down"),       # swap_line_down
    K("C-Pause"): pass_through_key,             # cancel cancel_build
    K("Super-c"): K("C-Pause"),                 # cancel_build
    K("f9"): pass_through_key,                  # cancel sort_lines case_s false
    K("f5"): K("f9"),                           # sort_lines case_s false
    K("Super-f9"): pass_through_key,            # cancel sort_lines case_s true
    K("Super-f5"): K("Super-f9"),               # sort_lines case_s true
    K("M-Shift-Key_1"): pass_through_key,       # cancel set_layout
    K("C-M-Key_1"): K("M-Shift-Key_1"),         # set_layout
    K("M-Shift-Key_2"): pass_through_key,       # cancel set_layout
    K("C-M-Key_2"): K("M-Shift-Key_2"),         # set_layout
    K("M-Shift-Key_3"): pass_through_key,       # cancel set_layout
    K("C-M-Key_3"): K("M-Shift-Key_3"),         # set_layout
    K("M-Shift-Key_4"): pass_through_key,       # cancel set_layout
    K("C-M-Key_4"): K("M-Shift-Key_4"),         # set_layout
    K("M-Shift-Key_8"): pass_through_key,       # cancel set_layout
    K("C-M-Shift-Key_2"): K("M-Shift-Key_8"),   # set_layout
    K("M-Shift-Key_9"): pass_through_key,       # cancel set_layout
    K("C-M-Shift-Key_3"): K("M-Shift-Key_9"),   # set_layout
    K("M-Shift-Key_5"): pass_through_key,       # cancel set_layout
    K("C-M-Shift-Key_5"): K("M-Shift-Key_5"),   # set_layout
    # K(""): pass_through_key,                    # cancel
    # K(""): K(""),                               #
}, "Sublime Text")