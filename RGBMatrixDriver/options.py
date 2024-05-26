def prefilled_matrix_options(arglist):
    from RGBMatrixDriver import RGBMatrixOptions

    options = RGBMatrixOptions()

    if arglist.led_gpio_mapping is not None:
        options.hardware_mapping = arglist.led_gpio_mapping

    options.rows = arglist.led_rows
    options.cols = arglist.led_cols
    options.chain_length = arglist.led_chain
    options.parallel = arglist.led_parallel
    options.row_address_type = arglist.led_row_addr_type
    options.multiplexing = arglist.led_multiplexing
    options.pwm_bits = arglist.led_pwm_bits
    options.brightness = arglist.led_brightness
    options.scan_mode = arglist.led_scan_mode
    options.pwm_lsb_nanoseconds = arglist.led_pwm_lsb_nanoseconds
    options.led_rgb_sequence = arglist.led_rgb_sequence
    options.pixel_mapper_config = arglist.led_pixel_mapper
    options.pwm_dither_bits = arglist.led_pwm_dither_bits
    options.limit_refresh_rate_hz = arglist.led_limit_refresh
    options.disable_hardware_pulsing = arglist.led_no_hardware_pulse

    if arglist.led_show_refresh:
        options.show_refresh_rate = 1

    if arglist.led_slowdown_gpio is not None:
        options.gpio_slowdown = arglist.led_slowdown_gpio

    # Driver specific options
    options.driver_fps_mode = arglist.driver_fps
    options.driver_screenshots_enabled = arglist.driver_screenshots

    return options
