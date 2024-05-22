import logging

# Create a Logger
Logger = logging.getLogger("RGBMD")
Logger.setLevel(logging.INFO)

# Create console handler and set the log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter(
    "[%(asctime)s] [%(name)s] [%(levelname)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

# Add formatter to console handler
ch.setFormatter(formatter)

# Add console handler to Logger
Logger.addHandler(ch)
