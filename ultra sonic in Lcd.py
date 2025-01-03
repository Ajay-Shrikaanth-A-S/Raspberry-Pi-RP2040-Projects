from machine import Pin
import utime 
from gpio_lcd import GpioLcd
count=0
lcd=GpioLcd(rs_pin= Pin(8),
    enable_pin= Pin(9),
    d4_pin= Pin(10),
    d5_pin= Pin(11),
    d6_pin= Pin(12),
    d7_pin= Pin(13))
trigger= Pin(15,Pin.OUT)
echo= Pin(14,Pin.IN)
relay= Pin(7,Pin.OUT)
buzzer= Pin(6,Pin.OUT)
led1= Pin(3,Pin.OUT)
lcd.move_to(0,0)
lcd.putstr("Distance:")
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
    timepassed = signalon-signaloff
    distance = (timepassed*0.0343)/2
    print("total distance",distance,'cm')
    print("sensor")
    utime.sleep_us(1)
    if distance<30:
        buzzer.value(1)
        relay.value(1)
        utime.sleep(0.1)
        led1.value(1)
        utime.sleep(0.5)
        lcd.move_to(2,1)
        lcd.putstr(str(distance))        
        print("detected")
    else:
        buzzer.value(0)
        relay.value(0)
        utime.sleep(1)
        led1.value(0)
        utime.sleep(0.5)
        lcd.move_to(2,1)
        lcd.putstr(str(distance))
        print("not detected")
       
        

            
