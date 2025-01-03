from machine import Pin
import time
counter=0
sw_btN1 = Pin(5,Pin.IN,Pin.PULL_UP)
sw_btN2 = Pin(4,Pin.IN,Pin.PULL_UP)
while True:
    if sw_btN2.value()==0:
        print("button pressed 1 ")
        counter+=1
        print("count:",counter)
        while(1):
            if sw_btN2.value()==1:
                time.sleep(0.1)
                break
    if sw_btN1.value()==0:
        print("button pressed 2 ")
        counter-=1
        print("count:",counter)
        while(1):
            if sw_btN1.value()==1:
                time.sleep(0.1)
                break
         
       