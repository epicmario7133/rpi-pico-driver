import machine
import utime

analog_value = machine.ADC(28)

while True:
    reading = analog_value.read_u16()     
    if reading < 50000:
        print("Fire Dectected");
    else:
        print("No fire or smoke detected");
    utime.sleep(1.0)
