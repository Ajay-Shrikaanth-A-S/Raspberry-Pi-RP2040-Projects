from machine import Pin
from utime import sleep_ms
button1 = Pin(5,Pin.IN,Pin.PULL_UP)
button2 = Pin(4,Pin.IN,Pin.PULL_UP)
led1 = Pin(2,Pin.OUT)
led2 = Pin(3,Pin.OUT)
while True:
    if button1.value()==0:
        led1.value(1)
        print("led1 on")
    else:
        led1.value(0)
        print("led1 off")
    if button2.value()==0:
        led2.value(1)
        print("led2 on")
    else:
        led2.value(0)
        print("led2 off")    
            

