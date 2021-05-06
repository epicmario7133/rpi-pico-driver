import machine
import utime

analog_value = machine.ADC(28)

while True:
    reading = analog_value.read_u16()
    print("Value: ",reading)
    if reading < 50000:
        print("The sensor has been touched")
    else:
        print("The sensor was not touched")
    utime.sleep(1.0)
