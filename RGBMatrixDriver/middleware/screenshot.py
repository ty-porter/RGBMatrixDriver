import os, time
import numpy as np
from PIL import Image
import keyboard
from threading import Lock


class ScreenshotMiddleware:
    @staticmethod
    def inject(driver):
        class _ScreenshotInjectedMiddleware(driver.RGBMatrix):
            SCREENSHOT_PATH = "screenshots"

            def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)

                self.driver = driver

                self.enabled = kwargs["options"].driver_screenshots_enabled or False

                if self.enabled:
                    self.__start_keypress_listener()

                    self.mutex = Lock()
                    self.received_event = False

            def SwapOnVSync(self, canvas):
                if self.enabled and self.received_event:
                    # TODO: Add hardware screenshots
                    if self.driver.is_emulated():
                        self.__capture_emulated_screenshot(canvas)

                return super().SwapOnVSync(canvas)

            def __capture_emulated_screenshot(self, canvas):
                self.mutex.acquire()

                try:
                    path = os.path.join(os.getcwd(), self.SCREENSHOT_PATH)
                    filename = os.path.join(path, f"{int(time.time())}.png")

                    if not os.path.exists(path):
                        self.driver.logger.info(
                            f"Screenshot directory not found, creating empty directory ({path})"
                        )
                        os.makedirs(path)

                    # TODO: Fix using a private attribute. Fine for now, since RGBME / RGBMD are by the same author.
                    #       Will likely to need to do hacky things to get the raw pixels from the hardware version also
                    pixels = np.asarray(canvas._Canvas__pixels, dtype=np.uint8)
                    image = Image.fromarray(pixels, mode="RGB")
                    image.save(filename)

                    self.driver.logger.info(f"Screenshot captured ({filename})")
                except:
                    self.driver.logger.exception(
                        "Encountered an exception while capturing screenshot"
                    )
                finally:
                    self.received_event = False
                    self.mutex.release()

            def __start_keypress_listener(self):
                def on_hotkey(matrix):
                    matrix.mutex.acquire()
                    matrix.received_event = True
                    matrix.mutex.release()

                    # Debounce, can only screenshot once per second
                    time.sleep(1)

                keyboard.add_hotkey("print screen", lambda : on_hotkey(self))

        driver.RGBMatrix = _ScreenshotInjectedMiddleware
