from machine import Pin, ADC
import time
import utime
import network
import urequests
import _thread
import ufirebase as firebase
from gpio_lcd import GpioLcd
conversion_factor= 3.3/65536
adc2= machine.ADC(27)
firebase.setURL("https://auspicious-lead-367303-default-rtdb.firebaseio.com")

relay1=Pin(2,Pin.OUT)
relay1.low()

relay2=Pin(3,Pin.OUT)
relay2.low()


ssid='Galaxy A237FAC'
password='ajayshri'

wlan=network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid,password)
wait=10
while wait>0:
    if wlan.status()<0 or wlan.status()>3:
        break
    wait-=1
    print('waiting for connection...')
    time.sleep(1)

if wlan.status() != 3:
    raise RuntimeError('network connection failed')
    lcd.move_to(0,0)
    lcd.putstr("Wifi not connected")
    time.sleep(2)
else:
    print('connected')
    status=wlan.ifconfig()
    print('ip='+status[0])
    
while True:
    time.sleep(3)
    print("put")
    val2=adc2.read_u16()
    temp=(val2*conversion_factor)*100
    temp1=int(temp)
    temp2=str(temp1)
    
    print("============================")
    print("temperature:",temp1)
    time.sleep(0.8)
    firebase.put("FirebaseIOT/temperature",temp1, bg=0, id=3)
    
    print("get")
    firebase.get("FirebaseIOT","led", bg=0, id=0)
    words=firebase.led
    d=words['led']
    direct=d
    print(direct)
    if(direct==1):
        relay1.high()
    if(direct==0):
        relay1.low()
        
    print("GET")
    firebase.get("FirebaseIOT","led1", bg=0, id=0)
    words=firebase.led
    d1=words['led1']
    direct1=d1
    print(direct1)
    if(direct==1):
        relay2.high()
    if(direct==0):
        relay2.low()
   

    