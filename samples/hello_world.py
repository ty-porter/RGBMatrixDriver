import sys, time

from RGBMatrixDriver import (
    RGBMatrix,
    graphics,
    RGBMatrixArguments,
    prefilled_matrix_options,
)


class HelloWorld:
    def __init__(self, args):
        self.matrix = RGBMatrix(options=prefilled_matrix_options(args))
        self.canvas = self.matrix.CreateFrameCanvas()

        self.font = graphics.Font()
        self.font.LoadFont("./fonts/7x13.bdf")

        self.color = graphics.Color(255, 255, 0)

    def run(self):
        pos = self.canvas.width

        while True:
            self.canvas.Clear()
            len = graphics.DrawText(
                self.canvas, self.font, pos, 10, self.color, "Hello World!"
            )
            pos -= 1
            if pos + len < 0:
                pos = self.canvas.width

            self.canvas = self.matrix.SwapOnVSync(self.canvas)

            time.sleep(0.05)


if __name__ == "__main__":
    hw_args = RGBMatrixArguments().parse_args()
    hw = HelloWorld(hw_args)

    try:
        print("Press CTRL-C to stop sample")
        hw.run()
    except KeyboardInterrupt:
        print("Exiting")
        sys.exit(0)
