import machine
from machine import Pin, PWM
import utime

analog_value = machine.ADC(28)
buzzer = PWM(Pin(0))

while True:
    reading = analog_value.read_u16()
    print("Value: ",reading)
    if reading < 50000:
        print("The sensor has been touched")
        buzzer.freq(1980)
        buzzer.duty_u16(1000)
        utime.sleep(5)
        buzzer.duty_u16(0)
    else:
        print("The sensor was not touched")
    utime.sleep(1.0)
