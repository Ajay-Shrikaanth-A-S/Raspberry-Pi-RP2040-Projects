from machine import Pin
import time
import utime
conversion_factor= 3.3/65536
adc2= machine.ADC(27)
while True:
    val2=adc2.read_u16()
    temp=(val2*conversion_factor)*100
    temp1=int(temp)
    temp2=str(temp1)
    
    print("============================")
    print("temperature:",temp1)
    time.sleep(0.8)