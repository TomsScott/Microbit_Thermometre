serial.redirect_to_usb()

def on_forever():
    serial.write_string("   " + "\r")
    serial.write_string("" + convert_to_text(input.light_level()))
    # basic.show_string(convert_to_text(input.light_level()))
    basic.pause(200)
basic.forever(on_forever)
