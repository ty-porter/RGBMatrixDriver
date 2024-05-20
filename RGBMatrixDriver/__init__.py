import sys

from RGBMatrixDriver.driver import *

sys.modules["RGBMatrixDriver"] = RGBMatrixDriverWrapper()
