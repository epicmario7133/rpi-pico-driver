import machine
import utime
from machine import Pin, PWM

analog_value = machine.ADC(28)
buzzer = PWM(Pin(0))
  
while True:
    reading = analog_value.read_u16()
    print("Value: ",reading)
    if reading < 50000:
        print("Magnet detected")
        buzzer.freq(1980)
        buzzer.duty_u16(1000)
        utime.sleep(5)
        buzzer.duty_u16(0)
    else:
        print("Magnet not detected")
    utime.sleep(1.0)
