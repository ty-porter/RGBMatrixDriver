import argparse


defaults = argparse.ArgumentParser(add_help=False)

# rpi-rgb-led-matrix library options
defaults.add_argument(
    "--led-rows",
    action="store",
    help="Display rows. 16 for 16x32, 32 for 32x32. (Default: 32)",
    default=32,
    type=int,
)
defaults.add_argument(
    "--led-cols",
    action="store",
    help="Panel columns. Typically 32 or 64. (Default: 32)",
    default=32,
    type=int,
)
defaults.add_argument(
    "--led-chain",
    action="store",
    help="Daisy-chained boards. (Default: 1)",
    default=1,
    type=int,
)
defaults.add_argument(
    "--led-parallel",
    action="store",
    help="For Plus-models or RPi2: parallel chains. 1..3. (Default: 1)",
    default=1,
    type=int,
)
defaults.add_argument(
    "--led-pwm-bits",
    action="store",
    help="Bits used for PWM. Range 1..11. (Default: 11)",
    default=11,
    type=int,
)
defaults.add_argument(
    "--led-brightness",
    action="store",
    help="Sets brightness level. Range: 1..100. (Default: 100)",
    default=100,
    type=int,
)
defaults.add_argument(
    "--led-gpio-mapping",
    help="Hardware Mapping: regular, adafruit-hat, adafruit-hat-pwm",
    choices=["regular", "adafruit-hat", "adafruit-hat-pwm"],
    type=str,
)
defaults.add_argument(
    "--led-scan-mode",
    action="store",
    help="Progressive or interlaced scan. 0 = Progressive, 1 = Interlaced. (Default: 1)",
    default=1,
    choices=range(2),
    type=int,
)
defaults.add_argument(
    "--led-pwm-lsb-nanoseconds",
    action="store",
    help="Base time-unit for the on-time in the lowest significant bit in nanoseconds. (Default: 130)",
    default=130,
    type=int,
)
defaults.add_argument(
    "--led-show-refresh",
    action="store_true",
    help="Shows the current refresh rate of the LED panel.",
)
defaults.add_argument(
    "--led-slowdown-gpio",
    action="store",
    help="Slow down writing to GPIO. Range: 0..4. (Default: 1)",
    choices=range(5),
    type=int,
)
defaults.add_argument(
    "--led-no-hardware-pulse",
    action="store",
    help="Don't use hardware pin-pulse generation.",
)
defaults.add_argument(
    "--led-rgb-sequence",
    action="store",
    help="Switch if your matrix has led colors swapped. (Default: RGB)",
    default="RGB",
    type=str,
)
defaults.add_argument(
    "--led-pixel-mapper",
    action="store",
    help='Apply pixel mappers. e.g "Rotate:90"',
    default="",
    type=str,
)
defaults.add_argument(
    "--led-row-addr-type",
    action="store",
    help="0 = default; 1 = AB-addressed panels; 2 = direct row select; 3 = ABC-addressed panels. (Default: 0)",
    default=0,
    type=int,
    choices=[0, 1, 2, 3],
)
defaults.add_argument(
    "--led-multiplexing",
    action="store",
    help="Multiplexing type: 0 = direct; 1 = strip; 2 = checker; 3 = spiral; 4 = Z-strip; 5 = ZnMirrorZStripe;"
    "6 = coreman; 7 = Kaler2Scan; 8 = ZStripeUneven. (Default: 0)",
    default=0,
    type=int,
)
defaults.add_argument(
    "--led-limit-refresh",
    action="store",
    help="Limit refresh rate to this frequency in Hz. Useful to keep a constant refresh rate on loaded system. "
    "0=no limit. Default: 0",
    default=0,
    type=int,
)
defaults.add_argument(
    "--led-pwm-dither-bits",
    action="store",
    help="Time dithering of lower bits (Default: 0)",
    default=0,
    type=int,
)
defaults.add_argument(
    "--led-panel-type",
    action="store",
    help="Needed to initialize special panels. Supported: 'FM6126A'",
    default="",
    type=str,
)
defaults.add_argument(
    "--led-drop-privileges",
    dest="drop_privileges",
    help="Force the matrix to drop privileges from 'root' after initializing the hardware.",
    action="store_true",
)


class RGBMatrixArguments(argparse.ArgumentParser):
    def __init__(self, *args, **kwargs):
        if "parents" in kwargs:
            kwargs["parents"].insert(0, defaults)
        else:
            kwargs["parents"] = [defaults]

        super().__init__(self, *args, **kwargs)
