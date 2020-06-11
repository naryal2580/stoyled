from .nGenStyls import info, \
                       good, \
                       warn, \
                       bad, \
                       coolInput, \
                       takenInput, \
                       coolExit, \
                       fetchFormatedTime


from .nGenStyls import *
from os import name

if name != 'posix':
    from ctypes import windll
    windll.kernel32.SetConsoleMode(windll.kernel32.GetStdHandle(-11), 7)

__version__ = "0.7"
__author__ = "naryal2580"

del escSeqs, genStyls, nGenStyls, func, formats, STYLS, COLRS, genEscSeqs, retnFunc
