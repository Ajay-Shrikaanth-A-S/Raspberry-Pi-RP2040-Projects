from machine import Pin
import utime
trigger= Pin(15,Pin.OUT)
echo= Pin(14,Pin.IN)
relay= Pin(7,Pin.OUT)
buzzer= Pin(6,Pin.OUT)
led1= Pin(3,Pin.OUT)
while True:
    trigger.low()
    utime.sleep_us(5)
    trigger.high()
    utime.sleep_us(10)
    trigger.low()
    while echo.value()==0:
        signaloff= utime.ticks_us()
    while echo.value()==1:
        signalon= utime.ticks_us()
    timepassed = signalon - signaloff
    distance = (timepassed*0.0343)/2
    print("total distance",distance,'cm')
    print("sensor")
    utime.sleep_us(1)
    if distance<30:
        buzzer.value(1)
        relay.value(1)
        utime.sleep(1)
        led1.value(1)
        utime.sleep(0.5)
        print("detected")
    else:
        buzzer.value(0)
        relay.value(0)
        utime.sleep(1)
        led1.value(0)
        utime.sleep(0.5)
        print("not detected")
        