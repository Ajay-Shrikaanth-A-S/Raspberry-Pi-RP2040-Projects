import pcf8574
from machine import I2C, Pin
import time
import array as arr
count=0
mod=0
mod1=0

m = arr.array('i', [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7c,0x07,0x7f,0x67])
 
i2c = I2C(id=0,scl=Pin(21),sda=Pin(20),freq=100000)
pcf = pcf8574.PCF8574(i2c, 0x21)
pcf.port =0x00
pcf = pcf8574.PCF8574(i2c, 0x20)
pcf.port =0x00
for n in range(11):
    pcf.port =m[n]
    time.sleep(0.5)
while(1):
    if(count<=99):
        pcf = pcf8574.PCF8574(i2c, 0x21)
        count=count+1
        mod = count % 10
        mod1 = count / 10
        pcf.port =m[int(mod)]
        print(count)
