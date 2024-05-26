from RGBMatrixDriver.arguments import RGBMatrixArguments
from RGBMatrixDriver.options import prefilled_matrix_options


class HelperMiddleware:
    @staticmethod
    def inject(driver):
        driver.RGBMatrixArguments = RGBMatrixArguments
        driver.prefilled_matrix_options = prefilled_matrix_options