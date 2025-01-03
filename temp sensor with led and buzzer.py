from machine import Pin
import time
conversion_factor= 3.3/65536
adc2= machine.ADC(27)
relay= Pin(7,Pin.OUT)
buzzer= Pin(6,Pin.OUT)
led1= Pin(3,Pin.OUT)
led2= Pin(2,Pin.OUT)
while True:
    val2=adc2.read_u16()
    temp=(val2*conversion_factor)*100
    temp1=int(temp)
    temp2=str(temp1)
    
    print("============================")
    print("temperature:",temp1)
    time.sleep(0.8)
    if temp1>28 and temp1<33:
        buzzer.value(1)
        time.sleep(1)
        relay.value(1)
        time.sleep(0.1)
        led1.value(1)
        time.sleep(0.5)
        led2.value(0)
        time.sleep(0.5)
        print("detected")
    else:
        buzzer.value(0)
        time.sleep(1)
        relay.value(0)
        time.sleep(1)
        led1.value(0)
        time.sleep(0.5)
        led2.value(1)
        time.sleep(0.5)
        print("not detected")