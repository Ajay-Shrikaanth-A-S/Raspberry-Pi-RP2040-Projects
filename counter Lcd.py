from machine import Pin
from gpio_lcd import GpioLcd
import time
count=0
lcd=GpioLcd(rs_pin= Pin(8),
    enable_pin= Pin(9),
    d4_pin= Pin(10),
    d5_pin= Pin(11),
    d6_pin= Pin(12),
    d7_pin= Pin(13))
lcd.move_to(0,0)
lcd.putstr("person counter")
lcd.move_to(0,1)
lcd.putstr("total count")
while(1):
    count=count+1
    lcd.move_to(11,1)
    lcd.putstr(str(count))
    time.sleep(1)
            