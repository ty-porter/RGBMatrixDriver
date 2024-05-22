import os, time

from RGBMatrixDriver.logger import Logger


def create_benchmarked_matrix(base, graphics):
    class BenchmarkedMatrix(base):
        EMIT_LOG="log"
        EMIT_OVERLAY="overlay"
        EMIT_MODES=[EMIT_LOG, EMIT_OVERLAY]

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.base = base

            self.tick_start = None
            self.tick_stop = None
            self.fps = []

            self.refresh_rate_ms = 1000.0
            self.refreshed_at = 0

            mode = kwargs["options"].driver_fps_mode
            self.mode = mode if mode in BenchmarkedMatrix.EMIT_MODES else None

            if mode == BenchmarkedMatrix.EMIT_OVERLAY:
                self.__load_overlay_mode()

        def SwapOnVSync(self, canvas):
            if self.mode is not None:
                self.__calculate_fps(canvas)

            return super().SwapOnVSync(canvas)
        
        def __calculate_fps(self, canvas):
            self.tick_stop = time.time()

            if self.tick_start is not None:
                self.fps.append(1 / (self.tick_stop - self.tick_start))

                should_refresh = self.__emit_fps(canvas)

                if should_refresh:
                    self.fps = []
                    self.refreshed_at = time.time()

            self.tick_start = self.tick_stop

        def __emit_fps(self, canvas):
            if self.mode == BenchmarkedMatrix.EMIT_LOG:
                return self.__emit_fps_to_log()
            elif self.mode == BenchmarkedMatrix.EMIT_OVERLAY:
                return self.__emit_fps_to_overlay(canvas)

            return False

        def __emit_fps_to_log(self):
            if self.__should_refresh():
                Logger.info(f"FPS: {self.__fps()}")

                return True
            
            return False

        def __emit_fps_to_overlay(self, canvas):
            # Draw background
            for y in range(0, 5):
                graphics.DrawLine(canvas, 0, y, 18, y, self.bg_color)
            
            # Draw FPS
            graphics.DrawText(canvas, self.font, 0, 5, self.text_color, str(self.__fps()))

            return self.__should_refresh()

        # TODO: If this is used in more places, it should be cached upstream on the driver object
        def __load_overlay_mode(self):
            driver_path = os.path.abspath(os.path.dirname(__file__))
            font_path = os.path.join(driver_path, 'fonts', '4x6.bdf')

            self.font = graphics.Font()
            self.font.LoadFont(font_path)

            self.text_color = graphics.Color(255, 255, 255)
            self.bg_color = graphics.Color(255, 0, 0)

        def __fps(self):
            return round(sum(self.fps) / len(self.fps), 2)
        
        def __should_refresh(self):
            return self.tick_stop >= self.refreshed_at + (self.refresh_rate_ms / 1000)

    return BenchmarkedMatrix
