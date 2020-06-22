"""
Stoyled

Standard Output Styled
"""


__version__ = "0.9"
__author__ = "naryal2580"


from .moreStyles import info, \
                        good, \
                        warn, \
                        bad, \
                        coolInput, \
                        takenInput, \
                        coolExit, \
                        fetchFormatedTime, \
                        bold, \
                        dim, \
                        italic, \
                        uline, \
                        blink, \
                        normal, \
                        invert, \
                        hidden, \
                        strike, \
                        red, \
                        green, \
                        yellow, \
                        blue, \
                        purple, \
                        cyan, \
                        white, \
                        red_l, \
                        green_l, \
                        yellow_l, \
                        blue_l, \
                        purple_l, \
                        cyan_l, \
                        white_l, \
                        rst


from os import name

# Adding ANSI Escape Sequence support to Windows devices, check will be made better after I'll enum all reutrn of `os.name`
if name != 'posix':
    from ctypes import windll
    windll.kernel32.SetConsoleMode(windll.kernel32.GetStdHandle(-11), 7)
    del windll


del generateStyles, moreStyles, escapeSequences, name