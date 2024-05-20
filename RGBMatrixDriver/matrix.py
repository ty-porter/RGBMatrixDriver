import time


def create_benchmarked_matrix(base):
    class BenchmarkedMatrix(base):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            self.base = base

            self.tick_start = None
            self.tick_stop = None
            self.fps = []

            self.refresh_rate_ms = 1000.0
            self.refreshed_at = 0

        def SwapOnVSync(self, canvas):
            result = super().SwapOnVSync(canvas)
            self.tick_stop = time.time()

            if self.tick_start is not None:
                self.fps.append(1 / (self.tick_stop - self.tick_start))

                if self.tick_stop >= self.refreshed_at + (self.refresh_rate_ms / 1000):
                    print(sum(self.fps) / len(self.fps))

                    self.fps = []
                    self.refreshed_at = time.time()

            self.tick_start = self.tick_stop

            return result

    return BenchmarkedMatrix
