from RGBMatrixDriver.logger import Logger

class LoggerMiddleware:
    @staticmethod
    def inject(driver):
        driver.logger = Logger
