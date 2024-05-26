import sys

from enum import Enum

from RGBMatrixDriver.middleware import Middleware


class RGBMatrixDriverMode(Enum):
    UNINITIALIZED = 0
    HARDWARE = 1
    SOFTWARE_EMULATION = 2


class RGBMatrixDriverWrapper:
    class UninitializedDriver(Exception):
        pass

    NO_OVERRIDE = ["is_uninitialized", "is_hardware", "is_emulated"]

    def __init__(self):
        self.hardware_load_failed = False
        self.mode = RGBMatrixDriverMode.UNINITIALIZED

        self.__initialize()

    @property
    def __name__(self):
        return "RGBMatrixDriver"

    def is_uninitialized(self):
        return self.mode == RGBMatrixDriverMode.UNINITIALIZED

    def is_hardware(self):
        return self.mode == RGBMatrixDriverMode.HARDWARE

    def is_emulated(self):
        return self.mode == RGBMatrixDriverMode.SOFTWARE_EMULATION

    def __initialize(self):
        if self.__found_emulated_flag():
            self.mode = RGBMatrixDriverMode.SOFTWARE_EMULATION
        else:
            self.mode = RGBMatrixDriverMode.HARDWARE

        if self.is_hardware():
            try:
                import rgbmatrix

                self.driver = rgbmatrix
            except ImportError:
                import RGBMatrixEmulator

                self.mode = RGBMatrixDriverMode.SOFTWARE_EMULATION
                self.driver = RGBMatrixEmulator
                self.hardware_load_failed = True
        elif self.is_emulated():
            import RGBMatrixEmulator

            self.driver = RGBMatrixEmulator
        else:
            raise RGBMatrixDriverWrapper.UninitializedDriver()

        Middleware.inject_all(self.driver)

        for name in self.NO_OVERRIDE:
            setattr(self.driver, name, getattr(self, name))

    def __found_emulated_flag(self):
        """
        This gets around a nasty chicken-and-egg problem:
            1. When imported, RGBMD needs the args to know whether to load the hardware or software driver
            2. To get the arg wrapper class, RGBMD needs to be imported
            3. Arguments can be added via argparse after RGBMD classes are imported, and passing those args
               via CLI will raise exceptions until they are added

        This method looks for any flag in sys.argv and removes it if found -- bypassing argparse.
        """
        found = False

        for arg in sys.argv:
            if "emulated" in arg:
                sys.argv.remove(arg)
                found = True

        return found

    def __getattr__(self, name):
        return getattr(self.driver, name)
