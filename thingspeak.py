from machine import Pin, ADC
import utime
import machine
import urequests
import machine
from machine import Pin
import network, time

adc1=machine.ADC(28)
sensor_temp=machine.ADC(4)
conversion_factor=3.3/65535

HTTP_HEADERS={'Content-type':'application/json'}
THINGSPEAK_WRITE_API_KEY='CDZP2B608PBQ8GS4'

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
    
#handle connection error
if wlan.status()!=3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status=wlan.ifconfig()
    print('ip='+status[0])

while True:
    time.sleep(5)
    val1=adc1.read_u16()>>4
    print("=========================================")
    print("adc1:",val1)
    reading=sensor_temp.read_u16()*conversion_factor
    temperature=27-(reading-0.706)/0.001721
    print(temperature)
    time.sleep(2)
    temp_readings={'field1':temperature,'field2':val1}
    request=urequests.post('https://api.thingspeak.com/update?api_key='+THINGSPEAK_WRITE_API_KEY,json=temp_readings,headers=HTTP_HEADERS)
    request.close()
    print(request)
