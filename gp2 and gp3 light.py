from machine import Pin
import time
led1 = Pin(2,Pin.OUT)
led2 = Pin(3,Pin.OUT)
while True:
    led1.high()
    led2.low()
    time.sleep(1)
    led1.low()
    led2.high()
    time.sleep(1)
    