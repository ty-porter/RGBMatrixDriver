from RGBMatrixDriver.middleware.helper import HelperMiddleware
from RGBMatrixDriver.middleware.fps import FPSMiddleware
from RGBMatrixDriver.middleware.logger import LoggerMiddleware
from RGBMatrixDriver.middleware.screenshot import ScreenshotMiddleware


class Middleware:
    # Loaded in order!
    MIDDLEWARES = [
        LoggerMiddleware,  # Needs to come first, to initialize the logger
        HelperMiddleware,
        ScreenshotMiddleware,
        FPSMiddleware,  # Needs to come last, for an accurate benchmark
    ]

    @staticmethod
    def inject_all(driver):
        for middleware in Middleware.MIDDLEWARES:
            middleware.inject(driver)
