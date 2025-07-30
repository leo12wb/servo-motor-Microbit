def on_forever():
    pins.servo_write_pin(AnalogPin.P1, 0)
    basic.pause(2000)
    pins.servo_write_pin(AnalogPin.P1, 180)
    basic.pause(2000)
basic.forever(on_forever)
