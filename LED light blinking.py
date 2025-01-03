from machine import Pin
import time
led1 = Pin('LED',Pin.OUT)
while True:
    led1.value(1)
    time.sleep(1)
    led1.value(0)
    time.sleep(0.1)