from machine import Pin
import utime
led1 = Pin(2,Pin.OUT)
led2 = Pin(3,Pin.OUT)
delay = 500
while True:
    led1.value(1)
    led2.value(0)
    print("led1 on")
    utime.sleep_ms(delay)
    led2.value(1)
    led1.value(0)
    print("led2 on")
    utime.sleep_ms(delay)
    led1.value(0)
    led2.value(0)
    print("led1 and led2 off")
    utime.sleep_ms(delay)
    led1.value(1)
    led2.value(1)
    print("led1 and led2 on")
    utime.sleep_ms(delay)
    break

    
    
    
    
