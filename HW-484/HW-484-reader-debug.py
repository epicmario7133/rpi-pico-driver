import machine
import utime

analog_value = machine.ADC(28)

while True:
    reading = analog_value.read_u16()
    print("Value: ",reading)
    if reading < 1000:
        print("Magnet detected")
    else:
        print("Magnet not detected")
    utime.sleep(1.0)
