def prefilled_matrix_options(args):
    from RGBMatrixDriver import RGBMatrixOptions

    options = RGBMatrixOptions()

    if args.led_gpio_mapping is not None:
        options.hardware_mapping = args.led_gpio_mapping

    options.rows = args.led_rows
    options.cols = args.led_cols
    options.chain_length = args.led_chain
    options.parallel = args.led_parallel
    options.row_address_type = args.led_row_addr_type
    options.multiplexing = args.led_multiplexing
    options.pwm_bits = args.led_pwm_bits
    options.brightness = args.led_brightness
    options.scan_mode = args.led_scan_mode
    options.pwm_lsb_nanoseconds = args.led_pwm_lsb_nanoseconds
    options.led_rgb_sequence = args.led_rgb_sequence
    options.pixel_mapper_config = args.led_pixel_mapper
    options.pwm_dither_bits = args.led_pwm_dither_bits
    options.limit_refresh_rate_hz = args.led_limit_refresh
    options.disable_hardware_pulsing = args.led_no_hardware_pulse

    if args.led_show_refresh:
        options.show_refresh_rate = 1

    if args.led_slowdown_gpio is not None:
        options.gpio_slowdown = args.led_slowdown_gpio

    # Driver specific options
    options.driver_fps_mode = args.driver_fps

    return options
