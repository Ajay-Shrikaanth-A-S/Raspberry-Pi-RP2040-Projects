from machine import Pin
from utime import sleep_ms
button1 = Pin(5,Pin.IN,Pin.PULL_UP)
led1 = Pin(2,Pin.OUT)
buzzer= Pin(6,Pin.OUT)
relay= Pin(7,Pin.OUT)
while True:
    if button1.value()==0:
        led1.value(1)
        buzzer.high()
        print("led1 on")
    else:
        led1.value(0)
        buzzer.low()
        relay.low()
        print("led1 off")
    
