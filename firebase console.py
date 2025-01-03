from machine import Pin, I2C, ADC
import time
import utime
import network
import urequests
import _thread
import ufirebase as firebase
adc2= machine.ADC(28)
adc=""

firebase.setURL("https://auspicious-lead-367303-default-rtdb.firebaseio.com")

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
    time.sleep(2)
else:
    print('connected')
    status=wlan.ifconfig()
    print('ip='+status[0])
    #lcd.clear()
    
while True:
    time.sleep(3)
    print("put")
    val1 = adc2.read_u16()
    adc = str(val1)
    firebase.put("adc", adc, bg=0, id=3)
    
    

