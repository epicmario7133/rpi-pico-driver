import machine
from machine import Pin, PWM
import utime

analog_value = machine.ADC(28)

while True:
    reading = analog_value.read_u16()
    print("Value: ",reading)
    if reading < 10000:
        print("Fire Dectected");
        buzzer = PWM(Pin(0))
        buzzer.freq(1980)
        buzzer.duty_u16(1000)
        utime.sleep(5)
        buzzer.duty_u16(0)
    else:
        print("No fire or smoke detected");
    utime.sleep(1.0)
