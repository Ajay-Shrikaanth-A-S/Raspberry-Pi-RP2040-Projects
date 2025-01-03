from machine import Pin
import time
buzzer = Pin(6,Pin.OUT)
while True:
    buzzer.value(1)
    print("buzzer on")
    time.sleep(0.5)
    buzzer.value(0)
    print("buzzer off")
    time.sleep(0.5)