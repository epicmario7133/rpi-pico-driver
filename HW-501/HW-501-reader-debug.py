from machine import Pin
import utime

sensor = Pin(16, Pin.IN, Pin.PULL_UP)
while True:
    print(sensor.value())
    if sensor.value() == 0:
        print("The sensor found inclination")
    else:
        print("The sensor did not find inclination")
    utime.sleep(1)
