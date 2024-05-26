from RGBMatrixDriver.middleware.helper import HelperMiddleware
from RGBMatrixDriver.middleware.fps import FPSMiddleware
from RGBMatrixDriver.middleware.logger import LoggerMiddleware

class Middleware:
    # Loaded in order!
    MIDDLEWARES = [
        LoggerMiddleware,
        HelperMiddleware,
        FPSMiddleware
    ]

    @staticmethod
    def inject_all(driver):
        for middleware in Middleware.MIDDLEWARES:
            middleware.inject(driver)
