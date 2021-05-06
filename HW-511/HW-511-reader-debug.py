from machine import Pin
import utime

sensor = Pin(16, Pin.IN, Pin.PULL_UP)
while True:
    print(sensor.value())
    if sensor.value() == 0:
        print("The sensor found something")
    else:
        print("The sensor did not find anything")
    utime.sleep(1)
