# `RGBMatrixDriver`

[![pypi Badge](https://img.shields.io/pypi/v/RGBMatrixDriver)](https://pypi.org/project/RGBMatrixDriver/)

`RGBMatrixDriver` is a driver middleware for `rpi-rgb-led-matrix`/`RGBMatrixEmulator` compatible display scripts.

Write your display script once, then run it on either real hardware or via software emulation. Out of the box, the middleware lets you get off the ground with a sensible default configuration while allowing extensibility and additional features.

## Installation

`RGBMatrixDriver` is in the [Python Package Index (PyPI)](http://pypi.python.org/pypi/RGBMatrixDriver/).
Installing with `pip` is recommended for all systems.

```sh
pip install RGBMatrixDriver
```

## Setup

Projects that are compatible with `RGBMatrixDriver` will rely on importing classes from `rpi-rgb-led-matrix`. These will need to be replaced by equivalent `RGBMatrixDriver` classes.

For example, usage on a Rasberry Pi might look like this:

```python
from rgbmatrix import RGBMatrix, RGBMatrixOptions
```

Using the driver middleware, you will need to use `RGBMatrixDriver` classes:

```python
from RGBMatrixDriver import RGBMatrix, RGBMatrixOptions
```

To take full advantage of the driver middleware, you will need to parse arguments using the `RGBMatrixArguments` class instead of a standard `argparse.ArgumentParser`. You can run this example in `/samples/quick_start.py`.

```python
from random import randint as r
from RGBMatrixDriver import RGBMatrix, RGBMatrixArguments, prefilled_matrix_options


# Support all the defaults that RGBMatrixDriver includes
args = RGBMatrixArguments().parse_args()

# Fill out an RGBMatrixOptions instance with all the arguments
options = prefilled_matrix_options(args)

# Create a matrix and canvas
matrix = RGBMatrix(options=options)
canvas = matrix.CreateFrameCanvas()

# Push the pixels!
while True:
  # Simulate static -- Set R, G, B equal to each other at random
  for y in range(matrix.height):
    for x in range(matrix.width):
      canvas.SetPixel(x, y, *tuple([r(0, 255)] * 3))

  canvas = matrix.SwapOnVSync(canvas)
```

You can also set a driver log level if you want, which is useful if you use any reporting middleware (such as the `--driver-fps=log` flag).

```python
import logging, RGBMatrixDriver


RGBMatrixDriver.logger.setLevel(logging.INFO)
```

## Usage

For the most part, startup of the existing script will be unchanged, unless you want to pass additional driver flags, as listed in the [Flags](#flags) section below.

The driver can handle both hardware and software emulation display modes.

### Hardware Mode

By default the driver tries to load in hardware mode. This is the mode end users will typically want to run as, so there are no additional flags needed to work on Raspberry Pi.

### Software Emulation Mode

If hardware loading fails for any reason, the driver will fallback to software emulation via `RGBMatrixEmulator`. A command line flag `--emulated` can also be used to force emulation.

See [`RGBMatrixEmulator` README](https://github.com/ty-porter/RGBMatrixEmulator/blob/main/README.md) for customization options when running software emulation mode.

## Flags

You can pass the `-h` / `--help` flags at any time to show a list of arguments that your script supports. This will be a default list of arguments provided for `rpi-rgb-led-matrix`, driver flags provided by this library, and finally, any custom flags you have implemented for your own script.

You should reference the [project README](https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/README.md) for `rpi-rgb-led-matrix` library when necessary.

### Driver Flags

```
--driver-fps {log,overlay}
  Calculate FPS and display via selected method: log, overlay
--driver-screenshots
  Enable screenshot capture via the PrintScreen key. Captures will be saved to the 'screenshots' directory (created if does not exist)
--emulated
  Run the script in software emulation mode via RGBMatrixEmulator
```

## Contributing
If you want to help develop RGBMatrixDriver, you must also install the dev dependencies, which can be done by running `pip install -e .[dev]` from within the directory.

Before submitting a PR, please open an issue to help us track development. All development should be based off of the `dev` branch. This branch is kept up-to-date with `main` after releases. 

## Contact

Tyler Porter

tyler.b.porter@gmail.com
